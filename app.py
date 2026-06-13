from flask import Flask, render_template, request, redirect, session, url_for
from ai import analyze_resume
from db import Base, engine, SessionLocal
import models
import PyPDF2
import docx
import json

app = Flask(__name__)
app.secret_key = "secret123"

Base.metadata.create_all(bind=engine)


@app.route("/")
def home():
    if "user" in session:
        return redirect(url_for("dashboard"))
    return redirect(url_for("login"))


@app.route("/signup", methods=["GET", "POST"])
def signup():
    db = SessionLocal()

    try:
        if request.method == "POST":
            email = request.form.get("email")
            password = request.form.get("password")

            existing_user = db.query(models.User).filter_by(email=email).first()

            if existing_user:
                return "User already exists"

            user = models.User(
                email=email,
                password=password
            )

            db.add(user)
            db.commit()

            return redirect(url_for("login"))

        return render_template("signup.html")

    finally:
        db.close()


@app.route("/login", methods=["GET", "POST"])
def login():
    db = SessionLocal()

    try:
        if request.method == "POST":
            email = request.form.get("email")
            password = request.form.get("password")

            user = db.query(models.User).filter_by(
                email=email,
                password=password
            ).first()

            if user:
                session["user"] = user.email
                return redirect(url_for("dashboard"))

            return "Invalid credentials"

        return render_template("login.html")

    finally:
        db.close()


@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():

    if "user" not in session:
        return redirect(url_for("login"))

    result = None
    resume_text = ""
    user_goal = ""

    if request.method == "POST":

        user_goal = request.form.get("role", "")
        resume_text = request.form.get("resume", "")

        file = request.files.get("file")

        if file and file.filename != "":

            if file.filename.lower().endswith(".pdf"):
                try:
                    pdf_reader = PyPDF2.PdfReader(file)

                    text = ""
                    for page in pdf_reader.pages:
                        text += page.extract_text() or ""

                    resume_text = text

                except Exception as e:
                    result = f"Error reading PDF file: {str(e)}"

            elif file.filename.lower().endswith(".docx"):
                try:
                    doc = docx.Document(file)

                    text = ""
                    for para in doc.paragraphs:
                        text += para.text + "\n"

                    resume_text = text

                except Exception as e:
                    result = f"Error reading DOCX file: {str(e)}"

        if resume_text and user_goal and result is None:

            try:
                result = analyze_resume(
                    resume_text,
                    user_goal
                )

                db = SessionLocal()

                try:
                    user = db.query(models.User).filter_by(
                        email=session["user"]
                    ).first()

                    report = models.Reports(
                        user_id=user.id,
                        resume_text=resume_text,
                        result=json.dumps(result)
                    )

                    db.add(report)
                    db.commit()

                finally:
                    db.close()

            except Exception as e:
                result = f"Error analyzing resume: {str(e)}"

    return render_template(
        "dashboard.html",
        user=session["user"],
        result=result
    )


@app.route("/history")
def history():

    if "user" not in session:
        return redirect(url_for("login"))

    db = SessionLocal()

    try:
        user = db.query(models.User).filter_by(
            email=session["user"]
        ).first()

        reports = db.query(models.Reports).filter_by(
            user_id=user.id
        ).all()

        parsed_reports = []

        for report in reports:

            try:
                parsed_result = json.loads(report.result)

            except json.JSONDecodeError:
                parsed_result = {
                    "error": "Invalid JSON format"
                }

            parsed_reports.append({
                "resume": report.resume_text,
                "result": parsed_result
            })

        return render_template(
            "history.html",
            reports=parsed_reports
        )

    finally:
        db.close()


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
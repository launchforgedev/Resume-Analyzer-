Resume Analyzer

An AI-powered Resume Analyzer built with Flask, Gemini AI, SQLAlchemy, and Jinja2. The application allows users to upload resumes, analyze their skills against a target career goal, identify missing skills, receive a personalized learning roadmap, generate interview questions, and visualize their career roadmap.

---

##  Features

* User Authentication (Signup/Login/Logout)
* Resume Upload Support

  * PDF (.pdf)
  * Word Documents (.docx)
  * Manual Resume Text Input
* AI-Powered Resume Analysis using Gemini
* Skill Extraction
* Missing Skill Identification
* Personalized Career Roadmap
* Interview Question Generation
* AI-Generated Career Roadmap Visualization
* Analysis History Tracking
* Space-Themed Modern User Interface
* Docker Support

---

## 🛠️ Tech Stack

### Backend

* Flask
* Python
* SQLAlchemy
* Gemini API

### Frontend

* HTML5
* CSS3
* Jinja2 Templates

### Database

* SQLite

### AI

* Google Gemini 2.5 Flash

### Deployment

* Docker

---

##  Project Structure

```text
project/
│
├── app.py
├── ai.py
├── db.py
├── models.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env
│
├── static/
│   ├── style.css
│   ├── dashboard.css
│   └── roadmap.png
│
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── signup.html
│   ├── dashboard.html
│   └── history.html
│
└── instance/
    └── database.db
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone <repository-url>
cd project
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

##  Gemini API Setup

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Get your API key from:

https://aistudio.google.com/

---

## ▶️ Running the Application

```bash
python app.py
```

Application will start at:

```text
http://127.0.0.1:5000
```

---

## 🐳 Docker Setup

### Build Image

```bash
docker build -t ai-resume-analyzer .
```

### Run Container

```bash
docker run -p 5000:5000 --env-file .env ai-resume-analyzer
```

Open:

```text
http://localhost:5000
```

---

## 📋 How It Works

1. User signs up or logs in.
2. Uploads a resume or pastes resume content.
3. Enters target career goal.
4. Gemini AI analyzes the resume.
5. Application extracts:

   * Existing Skills
   * Missing Skills
   * Learning Roadmap
   * Interview Questions
6. Results are displayed on the dashboard.
7. Analysis history is stored in the database.

---

## 📸 Screenshots

Add screenshots here:

```text
screenshots/
├── login.png
├── signup.png
├── dashboard.png
├── analysis.png
```

---

## 🚧 Future Improvements

* Resume Score Calculation
* ATS Compatibility Analysis
* Resume Improvement Suggestions
* Job Recommendations
* Roadmap PDF Export
* Email Reports
* Multi-Language Support
* User Profile Management
* Cloud Deployment

---

## 👨‍💻 Author

Prateek Patil

B.Tech Student | Aspiring Software Engineer | AI Enthusiast

---

## 📜 License

This project is for educational and learning purposes.

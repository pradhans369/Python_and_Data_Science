# Biswajeet Pradhan — Portfolio Website

A clean, modern, editorial portfolio website built for **Data Science & Machine Learning Engineering**. Designed with modern engineering aesthetics (inspired by Linear, Vercel, and Stripe developer portals), focusing on clarity, real architectural depth, and zero gimmicks.

Pre-configured for **Render** (both as a Python Web Service and as a Static Site).

---

## 🎨 Design Philosophy

- **Modern & Professional Aesthetic**:
  - Deep zinc/charcoal dark palette (`#09090b` and `#121215`) with subtle, refined border dividers (`rgba(255, 255, 255, 0.08)`).
  - No distracting bouncing canvas particles, no fake progress percentages ("92% Python"), and no toy simulator widgets.
  - Crisp typography using `Inter` for body reading and `JetBrains Mono` for code, tags, and metrics.
- **Bento Grid Core Focus**:
  - Highlights core engineering domains: Predictive Modeling, Deep Learning & Vision, Generative AI & NLP, and Production MLOps.
- **Curated Skills Catalog**:
  - Skills organized by actual real-world categories (Languages, Frameworks, NLP/GenAI, Data Wrangling, Infrastructure, and Methodologies).
- **Case-Study Style Projects**:
  - Filterable by *All*, *GenAI & RAG*, *Computer Vision*, and *Predictive ML*.
  - Realistic architectures, benchmark results, latency considerations, and tech stack tags.
- **Technical Writing & Notes Section**:
  - Highlighting engineering thought leadership and architectural trade-offs.
- **Direct & Functional Contact**:
  - Clean contact cards (Email, LinkedIn, GitHub, Location) + AJAX form with backend validation.

---

## 📁 Directory Structure

```text
7 PORTFOLIO WEBSITE/
├── app.py                     # Production Flask web server & contact API
├── index.html                 # Standalone static entry point (for static hosting)
├── requirements.txt           # Python dependencies (Flask, Gunicorn)
├── Procfile                   # Process file for Render web service
├── render.yaml                # Render Blueprint (Infrastructure as Code)
├── .gitignore                 # Git ignore rules
├── README.md                  # Setup & customization guide
├── templates/
│   └── index.html             # Flask template entry point
└── static/
    ├── css/
    │   └── style.css          # Editorial zinc-dark stylesheet & responsive layouts
    ├── js/
    │   └── main.js            # Smooth filters, mobile menu, and contact form AJAX
    └── images/
        ├── avatar.svg         # Clean minimalist profile placeholder badge
        └── favicon.svg        # Crisp modern monogram favicon
```

---

## 💻 Local Preview

### Running with Python & Flask:
```powershell
cd "d:\THE CODE\Python_and_Data_Science\7 PORTFOLIO WEBSITE"
python app.py
```
Open your browser at **`http://localhost:5000`**.

### Or Running Statically:
Double-click `index.html` or run:
```powershell
python -m http.server 8000
```
Then visit `http://localhost:8000`.

---

## 🚀 Deploying to Render

### Method A: Web Service (Python + Gunicorn)
1. Push this folder to a GitHub repository.
2. In Render Dashboard, click **New +** &rarr; **Web Service**.
3. Select your repository.
4. Settings:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
5. Click **Deploy Web Service**.

### Method B: Static Site (Zero Cost)
1. In Render Dashboard, click **New +** &rarr; **Static Site**.
2. Select your repository.
3. Set **Publish Directory** to `.`.
4. Click **Create Static Site**.

---

## ✏️ Customization Quick Reference

- **Profile Photo**: Put your photo in `static/images/avatar.jpg` and update the `src` attribute in `templates/index.html` and `index.html`.
- **Contact Details**: Update email and LinkedIn links in `templates/index.html` and `index.html`.
- **Projects**: Edit project titles, summaries, and GitHub links in the `<section id="projects">` block.

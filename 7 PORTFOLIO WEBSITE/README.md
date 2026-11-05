# Biswajeet Pradhan — Portfolio Website

A clean, modern, editorial portfolio website built for **Data Science & Machine Learning Engineering**. Designed with modern engineering aesthetics, focusing on clarity, real architectural depth, and zero gimmicks.

Configured for **Vercel** serverless deployment with full Python Flask API support (or zero-config static hosting).

---

## 📁 Project Structure

```text
7 PORTFOLIO WEBSITE/
├── api/
│   └── index.py                           # Vercel Serverless Function entry point
├── static/
│   ├── css/
│   │   └── style.css                      # Pastel & zinc editorial stylesheet & responsive layout
│   ├── js/
│   │   └── main.js                        # Smooth filtering, mobile navigation, and contact AJAX
│   ├── images/
│   │   ├── bull-logo.png                  # Custom Bull Logo (Hero & Footer)
│   │   ├── dp.png                         # Biswajeet Pradhan profile photograph
│   │   ├── cert-andrew-ng.png             # DeepLearning.AI / Stanford ML certificate
│   │   ├── cert-ibm.png                   # IBM Data Analytics Foundations certificate
│   │   └── favicon.svg                    # Monogram SVG favicon
│   └── docs/
│       ├── Biswajeet_Pradhan_Resume.pdf   # Resume PDF
│       ├── cert-andrew-ng.pdf             # DeepLearning.AI / Stanford ML certificate PDF
│       └── cert-ibm.pdf                   # IBM Data Analytics Foundations certificate PDF
├── templates/
│   └── index.html                         # Production Flask Jinja2 template
├── app.py                                 # Flask web application & /api/contact handler
├── index.html                             # Pre-compiled static HTML entry point
├── requirements.txt                       # Python dependencies (Flask>=3.0.0)
├── vercel.json                            # Vercel deployment rewrites configuration
├── .gitignore                             # Git ignore rules (including .vercel/)
└── README.md                              # Setup & deployment documentation
```

---

## 💻 Local Preview & Testing

### Option A: Running with Python & Flask
```powershell
cd "d:\THE CODE\Python_and_Data_Science\7 PORTFOLIO WEBSITE"
python app.py
```
Open your browser at **`http://localhost:5000`**.

### Option B: Running Statically
Double-click `index.html` or run:
```powershell
python -m http.server 8000
```
Then visit `http://localhost:8000`.

---

## 🚀 Deploying to Vercel

### Method 1: Deploy via GitHub (Recommended for automatic CI/CD)
1. Push your repository to **GitHub**:
   ```powershell
   git add .
   git commit -m "Configure portfolio for Vercel deployment"
   git push origin main
   ```
2. Log in to [Vercel](https://vercel.com).
3. Click **Add New...** &rarr; **Project**.
4. Select and import your GitHub repository.
5. In the project settings:
   - **Framework Preset**: *Other* (Vercel automatically detects `vercel.json` and Python `api/index.py`).
   - **Root Directory**: `7 PORTFOLIO WEBSITE` (if this folder is a subfolder in your repo, set the Root Directory to this path in Vercel settings; otherwise leave as `./`).
6. Click **Deploy**. Vercel will install dependencies from `requirements.txt` and launch your live site with an automatic HTTPS `*.vercel.app` domain.

### Method 2: Deploy via Vercel CLI
1. Install the Vercel CLI:
   ```powershell
   npm install -g vercel
   ```
2. Deploy directly from the project directory:
   ```powershell
   vercel
   ```
3. Follow the terminal prompts to select your account and project settings.
4. Deploy to production:
   ```powershell
   vercel --prod
   ```

---

## ⚙️ Key Backend Endpoints
- **`/`**: Renders the complete portfolio webpage with real-time copyright year.
- **`/resume`**: Serves `Biswajeet_Pradhan_Resume.pdf` (inline in browser on desktop, downloadable on mobile).
- **`/health`**: Serverless health check endpoint (`{"status": "healthy"}`).
- **`/api/contact`**: POST endpoint for handling AJAX contact form submissions safely.

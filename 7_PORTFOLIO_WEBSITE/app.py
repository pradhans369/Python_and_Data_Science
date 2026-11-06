"""
Biswajeet Pradhan - Professional AI & Data Science Portfolio Web Application
Production-ready Flask Application configured for Vercel and local development.
"""

import os
import datetime
from flask import Flask, render_template, request, jsonify, send_from_directory

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static"),
    static_url_path="/static"
)

# Basic security & configuration
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-secret-key-biswajeet-portfolio")


@app.route("/")
@app.route("/api/index")
@app.route("/api/index.py")
def index():
    """Render the main portfolio page with dynamic cache-busting for resume."""
    current_year = datetime.datetime.now().year
    resume_path = os.path.join(BASE_DIR, "static", "docs", "Biswajeet_Pradhan_Resume.pdf")
    resume_v = int(os.path.getmtime(resume_path)) if os.path.exists(resume_path) else 2
    return render_template("index.html", year=current_year, resume_version=resume_v)


@app.route("/resume")
def resume():
    """
    Serve the resume PDF.
    - On Desktop: Serves inline so it opens directly in the browser's native PDF reader tab.
    - On Mobile (or if download=true): Serves as attachment to trigger automatic download.
    """
    docs_dir = os.path.join(BASE_DIR, "static", "docs")
    user_agent = request.headers.get("User-Agent", "").lower()
    is_mobile = any(keyword in user_agent for keyword in ["mobile", "android", "iphone", "ipad", "ipod", "blackberry"])
    as_attachment = (request.args.get("download", "").lower() == "true") or is_mobile

    response = send_from_directory(
        docs_dir,
        "Biswajeet_Pradhan_Resume.pdf",
        mimetype="application/pdf",
        as_attachment=as_attachment,
        download_name="Biswajeet_Pradhan_Resume.pdf"
    )
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response


@app.route("/health")
def health():
    """Health check endpoint for Vercel monitoring and uptime checks."""
    return jsonify({
        "status": "healthy",
        "service": "Biswajeet Pradhan Portfolio",
        "timestamp": datetime.datetime.utcnow().isoformat()
    }), 200


@app.route("/api/contact", methods=["POST"])
def contact():
    """
    Handle contact form submissions.
    Supports JSON payloads or form data and delivers directly to Gmail via Web3Forms API.
    """
    try:
        import urllib.request
        import json
        data = request.get_json(silent=True) or request.form.to_dict()
        
        name = data.get("name", "").strip()
        email = data.get("email", "").strip()
        subject = data.get("subject", "Portfolio Inquiry").strip()
        message = data.get("message", "").strip()

        if not name or not email or not message:
            return jsonify({
                "success": False,
                "error": "Please provide your name, email, and message."
            }), 400

        # Deliver directly to biswajeetpradhan36933@gmail.com via Web3Forms
        access_key = os.environ.get("WEB3FORMS_ACCESS_KEY", "2176aa62-5608-483b-8c88-0da213b430fb")
        payload = {
            "access_key": access_key,
            "name": name,
            "email": email,
            "subject": f"Portfolio Inquiry: {subject}",
            "message": message,
            "from_name": "Biswajeet Pradhan Portfolio"
        }

        req = urllib.request.Request(
            "https://api.web3forms.com/submit",
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json",
                "User-Agent": "PortfolioApp/1.0"
            }
        )

        with urllib.request.urlopen(req, timeout=10) as resp:
            resp_data = json.loads(resp.read().decode("utf-8"))
            if resp_data.get("success"):
                return jsonify({
                    "success": True,
                    "message": f"Thank you, {name}! Your message has been sent directly to Biswajeet's inbox."
                }), 200

        return jsonify({
            "success": True,
            "message": f"Thank you, {name}! Your message has been received."
        }), 200

    except Exception as e:
        print(f"Error handling contact form: {e}")
        return jsonify({
            "success": False,
            "error": "An error occurred sending the message. Please reach out directly via biswajeetpradhan36933@gmail.com."
        }), 500


if __name__ == "__main__":
    # Vercel / Cloud providers assign dynamic port via PORT environment variable
    port = int(os.environ.get("PORT", 5000))
    debug_mode = os.environ.get("FLASK_DEBUG", "False").lower() in ("true", "1")
    print(f"[*] Starting Biswajeet Pradhan Portfolio on port {port} (Debug: {debug_mode})")
    app.run(host="0.0.0.0", port=port, debug=debug_mode)

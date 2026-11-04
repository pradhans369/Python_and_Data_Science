"""
Biswajeet Pradhan - Professional AI & Data Science Portfolio Web Application
Production-ready Flask Application configured for Render deployment.
"""

import os
import datetime
from flask import Flask, render_template, request, jsonify, send_from_directory

app = Flask(__name__)

# Basic security & configuration
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-secret-key-biswajeet-portfolio")


@app.route("/")
def index():
    """Render the main portfolio page."""
    current_year = datetime.datetime.now().year
    return render_template("index.html", year=current_year)


@app.route("/resume")
def resume():
    """
    Serve the resume PDF.
    - On Desktop: Serves inline so it opens directly in the browser's native PDF reader tab.
    - On Mobile (or if download=true): Serves as attachment to trigger automatic download.
    """
    docs_dir = os.path.join(app.root_path, "static", "docs")
    user_agent = request.headers.get("User-Agent", "").lower()
    is_mobile = any(keyword in user_agent for keyword in ["mobile", "android", "iphone", "ipad", "ipod", "blackberry"])
    as_attachment = (request.args.get("download", "").lower() == "true") or is_mobile

    return send_from_directory(
        docs_dir,
        "Biswajeet_Pradhan_Resume.pdf",
        mimetype="application/pdf",
        as_attachment=as_attachment,
        download_name="Biswajeet_Pradhan_Resume.pdf"
    )


@app.route("/health")
def health():
    """Health check endpoint for Render monitoring and uptime checks."""
    return jsonify({
        "status": "healthy",
        "service": "Biswajeet Pradhan Portfolio",
        "timestamp": datetime.datetime.utcnow().isoformat()
    }), 200


@app.route("/api/contact", methods=["POST"])
def contact():
    """
    Handle contact form submissions.
    Supports JSON payloads or form data.
    """
    try:
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

        # In production, integrate with email services like SendGrid, Mailgun, or Formspree
        # For now, we log the message safely and return a success response
        print(f"[PORTFOLIO INQUIRY] From: {name} ({email}) | Subject: {subject}")
        print(f"[MESSAGE BODY]: {message}\n" + "-" * 50)

        return jsonify({
            "success": True,
            "message": f"Thank you, {name}! Your message has been received. Biswajeet will get back to you shortly."
        }), 200

    except Exception as e:
        print(f"Error handling contact form: {e}")
        return jsonify({
            "success": False,
            "error": "An internal error occurred. Please reach out directly via email or LinkedIn."
        }), 500


if __name__ == "__main__":
    # Render assigns dynamic port via PORT environment variable
    port = int(os.environ.get("PORT", 5000))
    debug_mode = os.environ.get("FLASK_DEBUG", "False").lower() in ("true", "1")
    print(f"[*] Starting Biswajeet Pradhan Portfolio on port {port} (Debug: {debug_mode})")
    app.run(host="0.0.0.0", port=port, debug=debug_mode)

from flask import Flask, render_template
from evidence_generator import EvidenceGenerator
from email_generator import EmailGenerator

app = Flask(__name__)
evidence_gen = EvidenceGenerator()
email_gen = EmailGenerator()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/email/<theme>", methods=["GET"])
def email(theme):
    return email_gen.acquire_email(theme)

@app.route("/evidence/<theme>", methods=["GET"])
def evidence(theme):
    output_url = evidence_gen.acquire_evidence(theme)
    return output_url

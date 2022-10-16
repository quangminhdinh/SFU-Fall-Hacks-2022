from flask import Flask, render_template
from evidence_generator import EvidenceGenerator
from email_generator import EmailGenerator

app = Flask(__name__)
evidence_gen = EvidenceGenerator()
email_gen = EmailGenerator()

@app.route("/")
def hello_world():
    # output_url = evidence_gen.acquire_evidence()
    # return "<img src='" + output_url + "'/>"
    return render_template("index.html")

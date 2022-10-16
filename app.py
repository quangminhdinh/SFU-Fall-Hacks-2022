from flask import Flask, render_template, request
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

@app.route("/evidence", methods=["POST"])
def evidence():
    output_url = evidence_gen.acquire_evidence(request.get_data().decode('utf-8'))
    return "data:image/gif;base64," + output_url.decode('utf-8')

if __name__ == '__main__':
    app.run(debug=True)

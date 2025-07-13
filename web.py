from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    log_path = os.path.join(os.path.dirname(__file__), "../output/alerts.log")

    try:
        with open(log_path, 'r') as file:
            alerts = file.read().split('--------------------------------------------------\n')
            alerts = [a.strip() for a in alerts if a.strip()]
    except FileNotFoundError:
        alerts = ["No alerts found."]

    return render_template("dashboard.html", alerts=alerts)

if __name__ == "__main__":
    app.run(debug=True)

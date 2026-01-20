from flask import Flask, render_template, request, redirect, url_for, session
from datetime import datetime

app = Flask(__name__)
app.secret_key = "isp-secret-key"

# -------------------------------
# STATIC LOG DATA (Replace with DB later)
# -------------------------------
LOGS = [
    {
        "id": 1,
        "date": "2026-01-15",
        "time": "10:22:01",
        "ip": "103.12.45.10",
        "username": "pppoe01",
        "message": "User login successful"
    },
    {
        "id": 2,
        "date": "2026-01-15",
        "time": "11:05:12",
        "ip": "103.12.45.11",
        "username": "pppoe02",
        "message": "User disconnected"
    },
    {
        "id": 3,
        "date": "2026-01-16",
        "time": "09:45:44",
        "ip": "103.12.45.10",
        "username": "corpA",
        "message": "Authentication failed"
    },
]

# -------------------------------
# LOGIN
# -------------------------------
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session["user"] = request.form["username"]
        return redirect(url_for("dashboard"))
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

# -------------------------------
# DASHBOARD + FILTER
# -------------------------------
@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))

    date = request.args.get("date")
    ip = request.args.get("ip")
    message = request.args.get("message")

    filtered_logs = LOGS

    # AND LOGIC FILTERING
    if date:
        filtered_logs = [l for l in filtered_logs if l["date"] == date]
    if ip:
        filtered_logs = [l for l in filtered_logs if ip in l["ip"]]
    if message:
        filtered_logs = [l for l in filtered_logs if message.lower() in l["message"].lower()]

    return render_template("dashboard.html", logs=filtered_logs)

# -------------------------------
# LOG DETAIL VIEW
# -------------------------------
@app.route("/log/<int:log_id>")
def log_detail(log_id):
    if "user" not in session:
        return redirect(url_for("login"))

    log = next((l for l in LOGS if l["id"] == log_id), None)
    return render_template("log_detail.html", log=log)

if __name__ == "__main__":
    app.run(debug=True)

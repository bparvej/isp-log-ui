from flask import Flask, render_template, request, redirect, url_for, session
from db import get_connection

app = Flask(__name__)
app.secret_key = "log-sentry-secret"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session["user"] = request.form["username"]
        return redirect("/dashboard")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/")

    date = request.args.get("date")
    ip = request.args.get("ip")
    message = request.args.get("message")

    query = "SELECT * FROM isp_logs WHERE 1=1"
    params = []

    if date:
        query += " AND log_date = %s"
        params.append(date)
    if ip:
        query += " AND ip_address LIKE %s"
        params.append(f"%{ip}%")
    if message:
        query += " AND message ILIKE %s"
        params.append(f"%{message}%")

    conn = get_connection()
    cur = conn.cursor()
    cur.execute(query, params)
    logs = cur.fetchall()

    return render_template("dashboard.html", logs=logs)

@app.route("/log/<int:log_id>")
def log_detail(log_id):
    if "user" not in session:
        return redirect("/")

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM isp_logs WHERE id=%s", (log_id,))
    log = cur.fetchone()

    return render_template("log_detail.html", log=log)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

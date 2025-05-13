from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    message = ""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Very basic check (in real apps, check from DB and hash passwords)
        if username == "admin" and password == "1234":
            message = "Login successful!"
        else:
            message = "Invalid credentials. Try again."

    return render_template("login.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def profile():
    # Dynamic data to be passed to template
    return render_template("profile.html",
                           username="Aarav Desai",
                           email="aarav.desai@example.com",
                           bio="Lifelong learner. Python developer. Nature lover.")

if __name__ == "__main__":
    app.run(debug=True)

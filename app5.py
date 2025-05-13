from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def course_list():
    courses = [
        {"name": "Introduction to Python", "url": "https://example.com/python"},
        {"name": "Web Development", "url": "https://example.com/webdev"},
        {"name": "Data Science Basics", "url": "https://example.com/datascience"},
    ]
    return render_template("courses.html", courses=courses)

if __name__ == "__main__":
    app.run(debug=True)

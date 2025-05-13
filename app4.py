from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def student_list():
    students = [
        {"name": "Aarav", "age": 15, "grade": "10th"},
        {"name": "Diya", "age": 14, "grade": "9th"},
        {"name": "Kabir", "age": 16, "grade": "11th"},
    ]
    return render_template("students.html", students=students)

if __name__ == "__main__":
    app.run(debug=True)

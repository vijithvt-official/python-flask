
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Sending data to template
    name = "Vijith"
    languages = ["Python", "JavaScript", "C++"]
    return render_template("index.html", user=name, langs=languages)

if __name__ == '__main__':
    app.run(debug=True)

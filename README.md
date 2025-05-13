
# 🐍 Python Flask

Welcome to the **Python Flask Learning Repository**! This repository is curated to help beginners and enthusiasts get hands-on experience with the Flask web framework. It encompasses a variety of Python scripts, a Jupyter notebook, and a complete blog application built using Flask.

## 📁 Repository Structure

```
python-flask/
├── Flask.ipynb
├── hello.py
├── url-route.py
├── app.py
├── app1.py
├── app2.py
├── app3.py
├── app4.py
├── app5.py
├── app6.py
├── app7.py
├── api.py
├── sample.json
├── templates/
│   └── [HTML templates]
├── blog-app/
│   ├── static/
│   │   ├── css/
│   │   └── js/
│   ├── templates/
│   ├── main.py
│   └── [Other related files]
└── LICENSE
```

## 📘 Getting Started

### Prerequisites

- Python 3.6 or higher
- `pip` package manager
- Virtual environment tool (optional but recommended)

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/vijithvt-official/python-flask.git
   cd python-flask
   ```

2. **Create a Virtual Environment (Optional but Recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**

   If a `requirements.txt` file is present:

   ```bash
   pip install -r requirements.txt
   ```

   *Note: If `requirements.txt` is not available, you may need to install Flask manually:*

   ```bash
   pip install Flask
   ```

## 📝 Contents Overview

### 1. **Flask.ipynb**

A Jupyter Notebook that introduces the basics of Flask, including:

- Setting up a simple Flask application
- Understanding routing and view functions
- Rendering templates
- Handling HTTP methods

This notebook is ideal for interactive learning and experimentation.

### 2. **Standalone Python Scripts**

- **hello.py**: A minimal Flask application that returns "Hello, World!".
- **url-route.py**: Demonstrates dynamic URL routing and variable rules.
- **app.py** to **app7.py**: A series of scripts incrementally introducing more complex Flask concepts, such as:

  - Template rendering
  - Form handling
  - Session management
  - Error handling
  - Blueprint structuring

- **api.py**: Showcases building a simple RESTful API using Flask.

- **sample.json**: Contains sample data used in some of the applications.

### 3. **Templates Directory**

Contains HTML templates used by the Flask applications for rendering dynamic content. This includes:

- `base.html`: A base template to extend other templates.
- `index.html`: The homepage template.
- `about.html`, `contact.html`: Additional pages demonstrating template inheritance and routing.

### 4. **blog-app**

A comprehensive blog application built with Flask, demonstrating:

- Application factory pattern
- Blueprint structuring
- Static file management
- Template rendering
- Form handling and validation
- Database interactions (if implemented)

This project serves as a practical example of how to structure and build a full-fledged Flask application.

## 🚀 Running the Applications

To run any of the standalone Python scripts:

```bash
python app.py  # Replace with the desired script name
```

For the `blog-app`:

1. Navigate to the `blog-app` directory:

   ```bash
   cd blog-app
   ```

2. Run the application:

   ```bash
   python main.py
   ```

3. Open your browser and go to `http://127.0.0.1:5000/` to view the application.

*Note: Ensure that all necessary dependencies are installed before running the applications.*

## 📄 License

This project is licensed under the [GNU General Public License v3.0](LICENSE).

---

Happy Coding! 🚀

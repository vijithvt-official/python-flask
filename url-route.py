from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
	return 'You are at home page.'

@app.route('/students')
def student():
	return 'You are at students page.'

@app.route('/teachers')
def teacher():
	return 'You are at teachers page.'

if __name__ == '__main__':
	app.run(port=5001)
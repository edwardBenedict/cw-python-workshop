# Import Flask modules
from flask import Flask, render_template

# Create an object named app
app = Flask(__name__)

# Create a function named `home` which uses template file named `index.html` given under `templates` folder,
# send your name as template variable, and assign route of no path ('/')
@app.route('/')
def home():
	return render_template('index.html', name='Call')

# Write a function named `greet` which uses template file named `greet.html` given under `templates` folder
# and assign to the static route of ('/<name>')
@app.route('/<name>', methods=['GET'])
def greet(name):
	return render_template('greet.html', user=name)

# Write a function named `login` which uses `GET` and `POST` methods,
# and template files named `login.html` and `secure.html` given under `templates` folder
# and assign to the static route of ('login')

# Add a statement to run the Flask application which can be reached from any host on port 80.
if __name__ == '__main__':
	app.run(debug=True)
	#app.run('0.0.0.0', port=80)


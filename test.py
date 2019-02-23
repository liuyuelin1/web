from flask import Flask
from flask import request
from flask import redirect
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
	return redirect('http://www.example.com')
	
@app.route('/user_agent')
def user_agent():
	user_agent = request.headers.get('User-Agent')
	return '<p>Your browser is %s</p>' % user_agent
@app.route('/user/<name>')
def user(name):
	return render_template('test.html', name=name)

if __name__ == '__main__':
 app.run(debug=True)
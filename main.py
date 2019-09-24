from flask import Flask, request
import re
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/sign_up')
def display_form():
  template = jinja_env.get_template('form.html')
  return template.render(username="", username_error="", password="", password_error="", ver="", ver_error="", email="", email_error="")

@app.route('/sign_up', methods=['POST'])
def validate_form():

  template = jinja_env.get_template('form.html')
  template2 = jinja_env.get_template('success.html')

  username = request.form['username']
  password = request.form['password']
  ver = request.form['ver']
  email = request.form['email']

  username_error = ""
  password_error = ""
  ver_error = ""
  email_error = ""

  email_match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)

  if len(username) < 3 or len(username) > 20 or ' ' in username:
    username_error = "Your username is not invalid"  
    username = ""

  if len(password) < 3 or len(password) > 20 or ' ' in password:
    password_error = "Your password is not valid"

  if len(ver) < 3 or len(ver) > 20 or ' ' in ver:
    ver_error = "Your password verification is not valid"

  if len(password) > 2 and password != ver:
    password_error = ""
    ver_error = "Your password verification is not valid"

  
  if len(email) > 0:
    if len(email) < 3 or len(email) > 20 or email_match == None:
	    email_error = "Your email is not valid"
     
  if not username_error and not password_error and not ver_error and not email_error:
    return template2.render(username=username)

  else:
    return template.render(username=username, username_error=username_error, password='', password_error=password_error, ver='', ver_error=ver_error, email=email, email_error=email_error)

app.run()
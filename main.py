from flask import Flask, request
import re

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>User Signup</title>
    <style>
      @import url('https://fonts.googleapis.com/css?family=Poppins&display=swap');
      label {{
        cursor: pointer;
      }}
      .error {{
        color: red;
      }}
      body {{
        font-family: 'Poppins', sans-serif;
        background: #f2f2f2;
      }}
      h1 {{
        color: rgba(26, 98, 199, 1)
      }}
      .container {{
        height: 90vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
      }}
      .btn {{
        border-radius: 20px;
        width: 150px;
        height: 40px;
        font-size: 1.2rem;
        font-weight: bold;
        padding: 10px 15px;
        border: none;
        cursor: pointer;
        color: white;
  
        
        background : -moz-linear-gradient(98.05% 4.97% -152.89deg,rgba(46, 126, 255, 1) 0.56%,rgba(26, 98, 199, 1) 45.6%,rgba(0, 61, 127, 1) 100%);
        background : -webkit-linear-gradient(-152.89deg, rgba(46, 126, 255, 1) 0.56%, rgba(26, 98, 199, 1) 45.6%, rgba(0, 61, 127, 1) 100%);
        background : -webkit-gradient(linear,98.05% 4.97% ,3.52% 93.55% ,color-stop(0.0056,rgba(46, 126, 255, 1) ),color-stop(0.456,rgba(26, 98, 199, 1) ),color-stop(1,rgba(0, 61, 127, 1) ));
        background : -o-linear-gradient(-152.89deg, rgba(46, 126, 255, 1) 0.56%, rgba(26, 98, 199, 1) 45.6%, rgba(0, 61, 127, 1) 100%);
        background : -ms-linear-gradient(-152.89deg, rgba(46, 126, 255, 1) 0.56%, rgba(26, 98, 199, 1) 45.6%, rgba(0, 61, 127, 1) 100%);
        -ms-filter: "progid:DXImageTransform.Microsoft.gradient(startColorstr='#2E7EFF', endColorstr='#003D7F' ,GradientType=0)";
        background : linear-gradient(242.89deg, rgba(46, 126, 255, 1) 0.56%, rgba(26, 98, 199, 1) 45.6%, rgba(0, 61, 127, 1) 100%);
        filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#2E7EFF',endColorstr='#003D7F' , GradientType=1);
        /* background : -moz-linear-gradient(98.05% 4.97% -152.89deg,rgba(46, 126, 255, 1) 0.56%,rgba(26, 98, 199, 1) 45.6%,rgba(0, 61, 127, 1) 100%);
        background : -webkit-linear-gradient(-152.89deg, rgba(46, 126, 255, 1) 0.56%, rgba(26, 98, 199, 1) 45.6%, rgba(0, 61, 127, 1) 100%);
        background : -webkit-gradient(linear,98.05% 4.97% ,3.52% 93.55% ,color-stop(0.0056,rgba(46, 126, 255, 1) ),color-stop(0.456,rgba(26, 98, 199, 1) ),color-stop(1,rgba(0, 61, 127, 1) ));
        background : -o-linear-gradient(-152.89deg, rgba(46, 126, 255, 1) 0.56%, rgba(26, 98, 199, 1) 45.6%, rgba(0, 61, 127, 1) 100%);
        background : -ms-linear-gradient(-152.89deg, rgba(46, 126, 255, 1) 0.56%, rgba(26, 98, 199, 1) 45.6%, rgba(0, 61, 127, 1) 100%);
        -ms-filter: "progid:DXImageTransform.Microsoft.gradient(startColorstr='#2E7EFF', endColorstr='#003D7F' ,GradientType=0)";
        background : linear-gradient(242.89deg, rgba(46, 126, 255, 1) 0.56%, rgba(26, 98, 199, 1) 45.6%, rgba(0, 61, 127, 1) 100%);
        filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#2E7EFF',endColorstr='#003D7F' , GradientType=1); */
      }}
      .btn:hover {{
        color:#f2f2f2;
        font-size: 1.25rem;
        transition: 200ms;
        background : -moz-linear-gradient(100.55% 11.72% -152.89deg,rgba(243, 69, 239, 1) 0.56%,rgba(247, 76, 183, 1) 33.87%,rgba(255, 92, 63, 1) 100%);
        background : -webkit-linear-gradient(-152.89deg, rgba(243, 69, 239, 1) 0.56%, rgba(247, 76, 183, 1) 33.87%, rgba(255, 92, 63, 1) 100%);
        background : -webkit-gradient(linear,100.55% 11.72% ,1.11% 87.03% ,color-stop(0.0056,rgba(243, 69, 239, 1) ),color-stop(0.3387,rgba(247, 76, 183, 1) ),color-stop(1,rgba(255, 92, 63, 1) ));
        background : -o-linear-gradient(-152.89deg, rgba(243, 69, 239, 1) 0.56%, rgba(247, 76, 183, 1) 33.87%, rgba(255, 92, 63, 1) 100%);
        background : -ms-linear-gradient(-152.89deg, rgba(243, 69, 239, 1) 0.56%, rgba(247, 76, 183, 1) 33.87%, rgba(255, 92, 63, 1) 100%);
        -ms-filter: "progid:DXImageTransform.Microsoft.gradient(startColorstr='#F345EF', endColorstr='#FF5C3F' ,GradientType=0)";
        background : linear-gradient(242.89deg, rgba(243, 69, 239, 1) 0.56%, rgba(247, 76, 183, 1) 33.87%, rgba(255, 92, 63, 1) 100%);
        filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#F345EF',endColorstr='#FF5C3F' , GradientType=1);
        
      }}
      .button {{
        display: flex;
        justify-content: center;
      }}
   

    </style>
</head>
<body>
  <div class="container">
      <h1>Signup</h1>
  </br>
  <form action="/sign_up" method="POST">
    <table>
      <tbody>
        <tr>
          <td>
            <label for="username">Username:<span>&nbsp;</span></label>
          </td>
          <td>
            <input type="text" name="username" id="username" value='{username}'>
            <span class="error">{username_error}</span>
          </td>
        </tr>
        <tr>
          <td>
            <label for="password">Password:<span>&nbsp;</span></label>
          </td>
          <td>
            <input type="password" name="password" id="password" value='{password}'>
            <span class="error">{password_error}</span>
          </td>
        </tr>
        <tr>
            <td>
              <label for="ver">Confirm Password:<span>&nbsp;</span></label>
            </td>
            <td>
              <input type="password" name="ver" id="ver" value='{ver}'>
              <span class="error">{ver_error}</span>
            </td>
          </tr>
          <tr>
              <td>
                <label for="email">Email (Optional):<span>&nbsp;</span></label>
              </td>
              <td>
                <input type="text" name="email" id="email" value='{email}'>
                <span class="error">{email_error}</span>
              </td>
            </tr>
      </tbody>
    </table>
  </br>
  </br>
  </br>
    <div class="button">
    <input class="btn" type="submit">
    </div>
  </form>
  </div>
</body>
</html>

"""

# @app.route("/")
# def index():
#   return form

@app.route('/sign_up')
def display_form():
  return form.format(username="", username_error="", password="", password_error="", ver="", ver_error="", email="", email_error="")

# @app.route("/hello", methods=['POST'])
# def hello():
#   user_name = request.form['username']
#   return '<h1>Hello {}!</h1>'.format(user_name)


@app.route('/sign_up', methods=['POST'])
def validate_form():

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

    # return form.format(username=username, username_error=username_error, password=password, password_error=password_error, ver=ver, ver_error=ver_error, email=email, email_error=email_error)
     
  if not username_error and not password_error and not ver_error and not email_error:
    return 'A Success!'

  else:
    return form.format(username=username, username_error=username_error, password='', password_error=password_error, ver='', ver_error=ver_error, email=email, email_error=email_error)


app.run()
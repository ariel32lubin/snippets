from flask import Flask
from flask_basicauth import BasicAuth
from my_script import my_function  # Import your script's function

app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = 'your_username'
app.config['BASIC_AUTH_PASSWORD'] = 'your_password'

basic_auth = BasicAuth(app)

@app.route('/run-script')
@basic_auth.required
def run_script():
    my_function()  # Call your script's function here
    return 'Script executed'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

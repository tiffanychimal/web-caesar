from flask import Flask, request 
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form method ='POST'>
            <label>Rotate by:</label>
                <input name="rot" type="text" value="0" />
            <textarea name="text"></textarea>
            <input type="submit" />  
        </form> 
    </body>
</html>
"""

@app.route("/")
def index():
    return form

def is_integer(num):
    try: 
        int(num)
        return True
    except ValueError: 
        return False

@app.route("/", methods=['POST'])
def encrypt():
    rot = request.form['rot']
    text = request.form['text']

    rot_error = ''

    if not is_integer(rot):
        rot_error = 'Not a valid integer'
    else:
        rot = int(rot)

    if not rot_error: 
        encrypt_text = rotate_string(text, rot)
        return '<h1>' + encrypt_text + '</h1>'
    else:
        return form.format(rot=rot)

app.run()
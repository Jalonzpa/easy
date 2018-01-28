from flask import Flask, request, render_template
app = Flask(__name__)
 
@app.route("/")
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    button_name = text.upper()
    return ("Your new button is named %s.") % button_name
 
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

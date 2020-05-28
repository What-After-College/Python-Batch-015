from flask import Flask, render_template
app = Flask(__name__)

# @app.route("/thor")
# def greetingbkhbs():
#     return "hello Thor"

# @app.route("/thor")
# def hi():
#     return "hello world"


@app.route("/flask")
def chingchong():
    return "<h1 style=\"color:red\">Welcome to China</h1>"

@app.route('/thor')
def thor():
    return render_template("index.html")    

@app.route("/<name>")
def greetings(name):
    return "Hello! " + name.upper()

if __name__ == "__main__":
    app.run(debug=True, port=8000)

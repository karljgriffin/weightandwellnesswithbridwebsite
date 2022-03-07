from flask import Flask, render_template, g,  redirect, url_for, request

app = Flask(__name__)

# Welcome page
@app.route("/")
def index():
    return render_template("wwwbrid22.html")
    
@app.route("/legal")
def legal():
    return render_template("legal.html")

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
    

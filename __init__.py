from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("start.html")

@app.route('/articles')
def articles():
    return render_template("articles.html")

@app.route('/video')
def video():
    return render_template("video.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run()


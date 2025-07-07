from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/gallery')
def gallery():
    return render_template("gallery.html")

if __name__ == '__main__':
    # This will work both locally and on Render
    port = int(os.environ.get("PORT", 5000))  # Render sets this PORT
    app.run(host='0.0.0.0', port=port, debug=True)


from flask import Flask
from flask import render_template

app = Flask(__name__, static_folder='web/static', static_url_path='')
app.template_folder = "web"

@app.route("/")
def landing():
    return render_template('landing.html')
    
@app.route("/admin")
def admin():
    return render_template('admin.html')
    
@app.route("/vendor")
def vendor():
    return render_template('vendor.html')

if __name__ == "__main__":
    app.run()

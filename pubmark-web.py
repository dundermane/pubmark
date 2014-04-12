from flask import Flask, jsonify, render_template, request
from dblayer import DBlayer

pmdb = DBlayer()

app = Flask(__name__, static_folder='web/static', static_url_path='')
app.template_folder = "web"

@app.route("/")
def landing():
    return render_template('landing.html')


@app.route('/admin/_add_vendor')
def add_vendor():
    name = request.args.get('name', 0, type=str)
    tline = request.args.get('tagline', 0, type=str)
    handle = request.args.get('twitterhandle', 0, type=str)
    new = {'name': name, 'twitterhandle': handle, 'description': tline}
    added = pmdb.addmerchant(new)
    print 'yes'
    return jsonify(result=added)
    
@app.route("/admin")
def admin():
    return render_template('admin.html')
    
@app.route("/vendor")
def vendor():
    return render_template('vendor.html')

if __name__ == "__main__":
    app.run()

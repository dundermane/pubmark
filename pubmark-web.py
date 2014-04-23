import os
from datetime import datetime
from flask import Flask, jsonify, render_template, request
from dblayer import DBlayer
from tweetconsumer import TweetConsumer
from werkzeug.utils import secure_filename

pmdb = DBlayer()

app = Flask(__name__, static_folder='web/static', static_url_path='')
app.template_folder = "web"

app.config['CATEGORY_ICON_DIR'] = 'web/static/images/icn/'
app.config['TEMP_UPLOAD'] = 'web/static/temp/'
ALLOWED_IMAGES = set(['png','jpg'])

##START MAIN PAGE

@app.route("/")
def landing():
    return render_template('landing.html')

@app.route('/_get_tweets')
def get_tweets():
    filter = request.args.get('filter', type=str)
    n = request.args.get('n', 0, type=int)
    if (filter=='none'):
        result = pmdb.tweets.find().sort('created', -1)[n]
    else:
        result = pmdb.tweets.find({'merchanthandle':filter}).sort('created', -1)[n]
    return jsonify(text=result['text'],created=result['created'],merchant=result['merchanthandle'])

@app.route('/_get_merchant')
def get_merchant():
    name = request.args.get('handle', type=str) ##finds the most recently updated merchants
    result = pmdb.merchants.find_one({'twitterhandle':name})
    return jsonify(name=result['name'],description=result['description'],handle=result['twitterhandle'],tid=result['twitterid'],updated=result['lastupdated'],geo=result['lastgeo'],category=result['category'])

##END MAIN PAGE


##MAP

@app.route('/_recent_merchants')
def recent_merchants():
    n = request.args.get('n', 0, type=int) ##finds the most recently updated merchants
    result = pmdb.merchants.find().sort('lastupdated', -1)[n]
    print result
    return jsonify(name=result['name'],description=result['description'],handle=result['twitterhandle'],tid=result['twitterid'],updated=result['lastupdated'],geo=result['lastgeo'],category=result['category'])
    
##END MAP


##ADMIN PAGE

@app.route('/admin/_add_merchant')
def add_vendor():
    name = request.args.get('name', 0, type=str)
    tline = request.args.get('tagline', 0, type=str)
    handle = request.args.get('twitterhandle', 0, type=str)
    category = request.args.get('category',type=str)
    new = {'name': name, 'category': category, 'twitterhandle': handle, 'description': tline}
    print new
    added = pmdb.addmerchant(new)
    return jsonify(result=added)
    
#@app.route('/admin/_consume_tweets')
#def consume_tweets():
#    print 'im in'
#    cons = TweetConsumer()
#    print 'init'
#    new = cons.consume()
#    print 'nom'
#    return str(new)


@app.route('/admin/_add_category', methods=['POST'])
def catadd():
    if request.method == 'POST':
        name = request.form['catname']
        file = request.files['caticon']
        if not name: return jsonify({"success":False,"error":"No Name"})
        if not file: return jsonify({"success":False,"error":"No File"})
        if file and allowed_file(file.filename):
            filename = os.path.join(app.config['CATEGORY_ICON_DIR'], "%s.%s" % (name, file.filename.rsplit('.', 1)[1]))
            file.save(filename)
            new = {'name': name, 'filename':filename}
            pmdb.addcategory(new)
            return jsonify({"success":True})

@app.route('/admin/_preview_category', methods=['POST'])
def catpreview():
    if request.method == 'POST':
        file = request.files['caticon']
        if file and allowed_file(file.filename):
            filename = os.path.join(app.config['TEMP_UPLOAD'], "%s.%s" % (file.filename.rsplit('.', 1)[0], file.filename.rsplit('.', 1)[1]))
            file.save(filename)
            return jsonify({"success":('/temp/'+(file.filename.rsplit('.', 1)[0] + '.' + file.filename.rsplit('.', 1)[1]))})

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_IMAGES


@app.route('/_get_categories')
def get_categories():
    n = request.args.get('n', 0, type=int)
    result = pmdb.categories.find().sort('name', -1)[n]
    return jsonify(name=result['name'],filename=result['filename'])
    


@app.route("/admin")
def admin():
    return render_template('admin.html')

##END ADMIN PAGE

@app.route("/vendor")
def vendor():
    return render_template('vendor.html')

if __name__ == "__main__":
    app.run()

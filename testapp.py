from flask import Flask, current_app, request, flash, redirect, url_for, render_template
from lib.flask_pymongo import PyMongo
from dateutil.parser import parse

app = Flask(__name__)
app.secret_key = 'secret'
# 以下でMongoDBの場所を指定。testdb(データベース)やuser(コレクション、SQLでいうテーブル)はあらかじめ作る必要なし。
app.config['MONGO_HOST'] = '192.168.3.9'
app.config['MONGO_PORT'] = 27017
app.config['MONGO_DBNAME'] = 'testdb'
mongo = PyMongo(app, config_prefix='MONGO')

@app.route('/', methods=['GET'])
def show_entry():
    users = mongo.db.user.find()
    entries=[]
    for row in users:
        entries.append({"name": row['name'], "birthday": row['birthday'].strftime("%Y/%m/%d")})

    return render_template('toppage.html', entries=entries)
@app.route('add', methods=['POST'])
def add_entry():
    mongo.db.user.insert({"name":request.form['name'], "birthday": parse(request.form['birthday'])})
    flash('New entry was successfully posted')
    return redirect(url_for('show_entry'))
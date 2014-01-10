from flask import *
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient()
db=client.mydb
col=db.paintstore1

count=1
@app.route('/')
def home():
	return render_template('myPaintApp.html')

@app.route('/gallery/<filename>',methods=['GET'])
def load(filename=None):
	posts=[i for i in col.find({'title':filename})] 
	return render_template('picload.html',posts=posts)


@app.route('/<filename>',methods=['POST'])
def save(filename=None):
	global count
	col.insert({'title':request.form['name'],'imagedata':request.form['data'],'id':count})
	count+=1
	return render_template('myPaintApp.html')

@app.route('/gallery')
def gallery():
	posts=[i for i in col.find()] 	
	return render_template('gallery.html',posts=posts)

app.run(debug = True)





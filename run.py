from flask import *
import psycopg2
import database
import os
import urlparse

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def home():
	return render_template('myPaintApp.html')
@app.route('/gallery/<filename>',methods=['GET'])
def load(filename=None):
	urlparse.uses_netloc.append("postgres")
	url = urlparse.urlparse(os.environ["DATABASE_URL"])
	con = psycopg2.connect(database=url.path[1:],user=url.username,password=url.password,host=url.hostname,port=url.port)
	c = con.cursor()
	c.execute("SELECT * FROM paintstore1 WHERE title=%s",[filename])
	posts=[dict(id=i[0],title=i[1],imagedata=i[2]) for i in c.fetchall()]
	return render_template('picload.html',posts=posts)

@app.route('/<filename>',methods=['POST'])
def save(filename=None):
	urlparse.uses_netloc.append("postgres")
	url = urlparse.urlparse(os.environ["DATABASE_URL"])
	con = psycopg2.connect(database=url.path[1:],user=url.username,password=url.password,host=url.hostname,port=url.port)
	c = con.cursor()
	c.execute("INSERT INTO paintstore1 (title,imagedata) VALUES (%s,%s)",[request.form['name'],request.form['data']])
	con.commit()
	con.close()
	return render_template('myPaintApp.html')

@app.route('/gallery')
def gallery():
	urlparse.uses_netloc.append("postgres")
	url = urlparse.urlparse(os.environ["DATABASE_URL"])
	con = psycopg2.connect(database=url.path[1:],user=url.username,password=url.password,host=url.hostname,port=url.port)
	c = con.cursor()
	c.execute("SELECT * FROM paintstore1 ORDER BY id desc")
	posts=[dict(id=i[0],title=i[1]) for i in c.fetchall()]
	con.commit()
	con.close()	
	return render_template('gallery.html',posts=posts)

if __name__ == "__main__":
        port = int(os.environ.get("PORT", 5000))
        app.run(host='0.0.0.0', port=port)




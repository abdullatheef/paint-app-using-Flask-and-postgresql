import psycopg2
con = psycopg2.connect(database='firstdb') 
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS paintstore1")
cur.execute("CREATE TABLE paintstore1(id serial,title text,imagedata text)")
con.commit()
con.close()

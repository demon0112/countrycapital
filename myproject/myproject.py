from flask import Flask
from flask import url_for
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
from flask import request,redirect
from flask import current_app
from flask import jsonify
import os
import psycopg2
basedir = os.path.abspath(os.path.dirname(__file__))#connection with database
#connection with database
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:demon0112@localhost/testdb'
app.debug=True
db = SQLAlchemy(app)
conn = psycopg2.connect(database = 'testdb', user = 'postgres', password = 'demon0112', host = 'localhost')
curs = conn.cursor()
# Creating our database model
class Pos(db.Model):
    __tablename__ = "datag"
    country= db.Column(db.String(200),primary_key=True)
    capital= db.Column(db.String(200))
   
    def __init__(self,country,capital):
        self.country=country;
        self.capital=capital;
        
    def _repr_(self):
        return '<Pos %r>' % self.country
def render_with_context(template, url='/', **kw):
    with app.test_request_context(url):
        return render_template(template, **kw)
#@app.route('/')
#def index():
 #   return render_with_context('check.html')
@app.route('/capital',methods=['POST'])
def capital():
    place=request.form['country']  
    singlequery=Pos.query.filter_by(country=place).first()
    print(singlequery.capital)
    a=render_with_context('check.html',singlequery=singlequery)
    return a    
if __name__=="__main__":
    app.run()

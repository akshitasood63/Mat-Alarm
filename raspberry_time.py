import flask
import datetime
from app import db
import request

while(1):
    a=Alarm.query.all()
	for i in a:
		if(i==datetime.datetime.now().time()):
			request.get('http://0.0.0.0:80/asd')
			if(a.everyday==0):
				db.session.delete(i)
				db.session.commit()
				

from app import db
class Alarm(db.Model):
	__tablename__="time"	
	id=db.Column(db.Integer,primary_key=True)
	time=db.Column(db.Time,nullable=False)
	everyday=db.Column(db.Integer,nullable=False)
	def __init__(self, time,everyday):
		self.time = time
<<<<<<< HEAD
		self.everyday =everyday
		
=======
		self.everyday =everyday
>>>>>>> 416960eda6f0273fb47610604134bdcbf2c771a0

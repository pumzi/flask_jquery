from app import db

class User(db.Model): 
	firstname = db.Column(db.String(100))
	username = db.Column(db.String(120), unique =True)
	email = db.Column(db.String(50))
	password = db.Column(db.String(12))
	city = db.Column(db.String(100))
	post = db.relationship('Post', backref = 'architect') 


class Post(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	content = db.Column(db.Text)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #when you are refering to a class, it is lowercase

from db import db

class Member(db.Model):
	__tablename__="member"
	id = db.Column(db.Integer,primary_key=True)
	nama = db.Column(db.String(180))
	alamat = db.Column(db.String(180))

	def __init__(self,nama,alamat):
		self.nama=nama
		self.alamat=alamat
	def __repr__(self):
		return "<member{}>".format(self.nama)

class SocialMedia(db.Model):
	__tablename__="socialmedia"
	id = db.Column(db.Integer,primary_key=True)
	id_member =db.Column(db.Integer,db.ForeignKey("member.id"))
	member =db.relationship('Member',backref=db.backref("SocialMedia",lazy="dynamic"))
	facebook = db.Column(db.String(180))
	twitter = db.Column(db.String(180))
	
	def __init__(self,facebook,twitter):

		self.facebook = facebook
		self.twitter = twitter
	def __repr__(self):
		return"<socialmedia{}>".format(self.facebook)

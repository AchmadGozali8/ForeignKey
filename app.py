from flask import Flask,render_template,request
from db import db
from models import Member,SocialMedia

app = Flask(__name__)
app.config.from_object("config")
db.init_app(app)

@app.route("/",methods=["POST","GET"])
def index():
	if request.method=="POST":
		nama = request.form.get("nama",None)
		alamat = request.form.get("alamat",None)
		facebook = request.form.get("facebook",None)
		twitter = request.form.get("twitter",None)
	
		member = Member(nama,alamat)
		db.session.add(member)
		db.session.commit()
	
		socialmedia=SocialMedia(facebook,twitter)
		db.session.add(socialmedia)
		db.session.commit()
		return "thanks"
	return render_template("index.html",**locals())
if __name__=="__main__":
	app.run()

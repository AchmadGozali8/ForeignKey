from flask import Flask,render_template,request,redirect
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
		socialmedia = SocialMedia(facebook,twitter)
		socialmedia.member = member

		db.session.add(member)
		db.session.add(socialmedia)
		db.session.commit()
		return redirect("/data") 
	return render_template("index.html",**locals())

@app.route("/data")
def all_data():
	member = Member.query.all()
	
	return render_template("all_data.html",**locals())

@app.route("/data/<int:id>")
def data_by_id(id):
	member = Member.query.get(id)
	social = SocialMedia.query.get(id)

	return render_template("data_by_id.html",**locals())

@app.route("/data/update/<int:id>",methods=["POST","GET"])
def update(id):
	if request.method == "POST":
		socialmedia = SocialMedia.query.get(id)

		facebook = request.form.get("facebook",None)
		twitter = request.form.get("twitter",None)
	
		socialmedia.facebook = facebook
		socialmedia.twitter = twitter           
		db.session.add(socialmedia)
		db.session.commit()
		
		return redirect("/data")	
	socialmedia = SocialMedia.query.get(id)
	return render_template("update.html",**locals())
if __name__=="__main__":
	app.run()

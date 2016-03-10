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
	socialmedia = SocialMedia.query.get(id)

	return render_template("data_by_id.html",**locals())

if __name__=="__main__":
	app.run()

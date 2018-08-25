from flask import Flask,render_template,request,flash
import requests
import mysql.connector as mysql
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")




app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
	singup = "Sing Up"
	singin = "Sing In"
	if request.method == 'POST':

		location = request.form['location']
		res = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+location+"&APPID=8daef122aca4c4d9d40408fb5566bb65")
		data = res.json()
		co = data['main'] ['temp']
		nameofcity = data['name']
		hum = data['main'] ['humidity']
		temp_max = data['main'] ['temp_max']
		temp_min = data['main'] ['temp_min']
		conditions = data['weather'] [0] ['main']
		co = co - 273.15
		co = "%.2f" % co
		temp_min = temp_min - 273.15
		temp_max = temp_max - 273.15
		temp_min = "%.2f" % temp_min
		temp_max = "%.2f" % temp_max 
		
		return render_template("report.html",temp_min=temp_min,temp_max=temp_max,co=co,name=nameofcity,hum=hum)
	return render_template("index.html",singup=singup,singin=singin)

@app.route('/singup',methods=['GET','POST'])
def regis():
	error = ""
	if request.method == "POST":
		username = request.form['username']
		password = request.form['password']
		password = password
		email = request.form['email']

		if len(password) < 8:
			error =  "Use 8 or more characters"
			return render_template('singup.html',error=error)

		if len(password) >= 8:
			con = mysql.connect(  host="localhost",
  user="root",
  passwd="")
			c = con.cursor()

			c.execute("USE users")
			c.execute("INSERT INTO ask(Username,EmaiL,Password) VALUES(%s,%s,MD5(%s))",(username,email,password))
			con.commit()
			con.close()
			return render_template('singup.html')

	return render_template('singup.html')


@app.route('/login',methods=['GET','POST'])
def login():
	error = ''
	return render_template('login.html',error=error)
	

@app.errorhandler(404)
def error404(self):
	return render_template('404.html')


if __name__ == '__main__':
	app.run()
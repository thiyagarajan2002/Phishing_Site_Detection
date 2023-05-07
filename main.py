import Process as ps
from flask import Flask
from flask import render_template,redirect,request,url_for

app = Flask(__name__)
  
@app.route("/")
def index():
    return render_template("Home.html")

@app.route("/home")
def home():
    return render_template("Home.html")

@app.route("/sign up",methods = ['POST', 'GET'])
def sign_up():
    return render_template("Sign up.html",status=" ")


@app.route("/sign up process",methods = ['POST', 'GET'])
def sign_up_process():
    name=request.form['name']
    phone_number=request.form['phone_number']
    email=request.form['email'] 
    password=request.form['password']
    result=ps.sign_up(name,phone_number,email,password)
    if result:
        return redirect(url_for('sign_in'))
    else:
        return render_template('Sign_up.html',status="Invalid Details")
   

@app.route("/sign in",methods = ['POST', 'GET'])
def sign_in():
    return render_template("Sign in.html",status="")

@app.route("/prediction",methods = ['POST', 'GET'])
def prediction():
    email=request.form['email'] 
    password=request.form['password']
    result=ps.user_login(email,password)
    if result:
        return render_template("Root.html",result=result,status="")
    else:
        return render_template("Sign in.html",status="Invalid details")

@app.route("/result",methods = ['POST', 'GET'])
def result():
    url=request.form['url']
    user_id=request.form['id']
    predict=ps.predict(url)[1]
    result= "Yes" if predict=="This is a Phishing Site" else "No"; 
    ps.store(user_id,url,result)
    domain=ps.domain_info(url)
    return render_template("Result.html",url=url,predict=predict,domain=domain)

@app.route("/admin")
def admin():
    return render_template("Admin Sign in.html")

@app.route("/admin home",methods = ['POST', 'GET'])
def admin_login():
    email=request.form['email'] 
    password=request.form['password']
    result=ps.user_login(email,password)
    data=ps.get_data()
    if result:
        return render_template("Admin home.html",result=data)
    else:
        return render_template("Admin Sign in.html",status="Invalid details")

if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0')

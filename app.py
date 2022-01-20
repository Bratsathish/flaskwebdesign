from flask import Flask,render_template,url_for,request

app=Flask(__name__)


@app.route("/")
def index():
    return render_template("base.html")



@app.route("/markat")
def markat():
    return render_template("markat.html")



@app.route("/hero")
def hero():

    return render_template("hero.html")


@app.route("/login")
def login():
    return render_template("register.html")




@app.route("/car")
def car():
    return render_template("car.html")


@app.route("/home")
def home():
    return render_template("index.html")
@app.route("/Register" ,methods=["POST","GET"])
def Register():
    if request.method=="POST":
          name=request.form.get('name')
          age=request.form.get('age')
          birth_day=request.form.get('birth_day')
          address=request.form.get('address')
          contact=request.form.get('contact')
          email=request.form.get('email')
          return render_template("result.html",name=name,age=age,birth_day=birth_day,address=address,contact=contact,email=email)
     
if __name__=="__main__":
    app.run(debug=True)
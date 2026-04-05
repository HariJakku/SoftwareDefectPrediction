import numpy as np
from flask import Flask, request, jsonify, render_template
import joblib
import sqlite3

import numpy as np
import pandas as pd
from sklearn import metrics 
import warnings
import pickle
import pandas as pd
import numpy as np
import pickle
import sqlite3
import random

import smtplib 
from email.message import EmailMessage
from datetime import datetime

warnings.filterwarnings('ignore')



app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home1')
def home1():
	return render_template('home1.html')


@app.route('/logon')
def logon():
	return render_template('signup.html')

@app.route('/login')
def login():
	return render_template('signin.html')


@app.route('/home')
def home():
	return render_template('home.html')


@app.route("/signup")
def signup():
    global otp, username, name, email, number, password
    username = request.args.get('user','')
    name = request.args.get('name','')
    email = request.args.get('email','')
    number = request.args.get('mobile','')
    password = request.args.get('password','')
    con = sqlite3.connect('signup.db')
    cur = con.cursor()
    cur.execute("insert into `info` (`user`,`email`, `password`,`mobile`,`name`) VALUES (?, ?, ?, ?, ?)",(username,email,password,number,name))
    con.commit()
    con.close()
    return render_template("signin.html")
    

@app.route("/signin")
def signin():

    mail1 = request.args.get('user','')
    password1 = request.args.get('password','')
    con = sqlite3.connect('signup.db')
    cur = con.cursor()
    cur.execute("select `user`, `password` from info where `user` = ? AND `password` = ?",(mail1,password1,))
    data = cur.fetchone()

    if data == None:
        return render_template("signin.html")    

    elif mail1 == str(data[0]) and password1 == str(data[1]):
        return render_template("home.html")
    else:
        return render_template("signin.html")


@app.route('/predict',methods=['POST'])
def predict():
    int_features= [float(x) for x in request.form.values()]
    print(int_features,len(int_features))
    final4=[np.array(int_features)]
    model = joblib.load('model_cm1.sav')
    predict = model.predict(final4)

    if predict == 0:
        output = "Software is Not Defective!"
    elif predict == 1:
        output = "Software is Defective!"
    
    return render_template('prediction.html', output=output)


@app.route('/predict1',methods=['POST'])
def predict1():
    int_features= [float(x) for x in request.form.values()]
    print(int_features,len(int_features))
    final4=[np.array(int_features)]
    model = joblib.load('model_pc4.sav')
    predict = model.predict(final4)

    if predict == 0:
        output = "Software is Not Defective!"
    elif predict == 1:
        output = "Software is Defective!"
    
    return render_template('prediction.html', output=output)

@app.route("/notebook1")
def notebook1():
    return render_template("CM1.html")

@app.route("/notebook2")
def notebook2():
    return render_template("JM1.html")

@app.route("/notebook3")
def notebook3():
    return render_template("MC2.html")

@app.route("/notebook4")
def notebook4():
    return render_template("MW1.html")

@app.route("/notebook5")
def notebook5():
    return render_template("PC1.html")

@app.route("/notebook6")
def notebook6():
    return render_template("PC3.html")

@app.route("/notebook7")
def notebook7():
    return render_template("PC4.html")

@app.route("/about1")
def about1():
    return render_template("about1.html")

@app.route("/about2")
def about2():
    return render_template("about2.html")

@app.route("/about3")
def about3():
    return render_template("about3.html")

@app.route("/about4")
def about4():
    return render_template("about4.html")

@app.route("/about5")
def about5():
    return render_template("about5.html")

@app.route("/about6")
def about6():
    return render_template("about6.html")

@app.route("/about7")
def about7():
    return render_template("about7.html")



if __name__ == "__main__":
    app.run(debug=False)

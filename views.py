from flask import render_template,Flask, request,flash, redirect, url_for,session
import serial
import string
from app import app, db
from app.models import *
import datetime 
import os,time
from itertools import cycle
import RPi.GPIO as GPIO
from gpiozero import Buzzer
GPIO.setmode(GPIO.BCM)
but1=15
but2=16
but3=22
but4=19
led1=10
led2=11
led3=12
led4=13
buz=Buzzer(40)
#freq=100;


GPIO.setup(int(but1),GPIO.IN)
GPIO.setup(int(but2),GPIO.IN)
GPIO.setup(int(but3),GPIO.IN)
GPIO.setup(int(but4),GPIO.IN)
GPIO.setup(int(led1),GPIO.OUT)
GPIO.setup(int(led2),GPIO.OUT)
GPIO.setup(int(led3),GPIO.OUT)
GPIO.setup(int(led4),GPIO.OUT)
#GPIO.setup(
app = Flask(__name__)
app.secret_key='9\xc6u"\xad\xdb\x18\x81\x99e\xeac\x9d\'|\x02\xbe\xa3\xff\x87\x84*\xe3\xc1'
@app.route('/' )
def index():
       #return render_template('alarm.html')
	return 'adasd'
   

@app.route('/link',methods=["POST"])
def da():
	time=request.form['time']
    	everyday=request.form['everyday']
	db.session.add(Alarm(time,everyday))
	db.session.commit()
        return redirect(url_for('index')) 
@app.route('/asd')
def asd():
    GPIO.output(led1,GPIO.HIGH)
    buz.on()
    while(1):
		a=GPIO.Input(but1) 
		print a
		if(a==1):
			GPIO.output(led1,FALSE)
			break
    GPIO.output(led2,GPIO.HIGH)#digitalWrite(led2,HIGH);
    while(1):
		b=GPIO.Input(but2) 
		if(b==1):
			GPIO.output(led2,FALSE)
			break
    
    GPIO.output(led3,GPIO.HIGH)#digitalWrite(led3,HIGH);
    while(1):
		c=GPIO.Input(but3) 
		if(c==1):
			GPIO.output(led3,FALSE)
			break
    
    GPIO.output(led4,GPIO.HIGH)#digitalWrite(led3,HIGH);
    while(1):
		d=GPIO.Input(but4) 
		if(d==1):
			GPIO.output(led4,FALSE)
			break

    buz.off()
    return 'asd'

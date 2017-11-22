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
@app.route('/' )
def index():GPIO.output(led1,GPIO.HIGH)
	a=None
    return render_template('alarm.html',a=a)

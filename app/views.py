# -*- coding: utf-8 -*-

from app import app, db
from flask import render_template

@app.route('/')
def index():
	return render_template('index.html')





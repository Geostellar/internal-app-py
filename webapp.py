#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 11:26:24 2016

@author: mark
"""
from flask import Flask
from application import misc

app = Flask(__name__)

@app.route('/')
def hello_world():
    message = misc.message
    return message

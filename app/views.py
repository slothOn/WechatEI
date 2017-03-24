__author__ = 'zxc'

from app import app
from flask import render_template, request
from app.utils import xml2data

@app.route('/')
def index():
    return render_template("index.html", text="Hello World")

@app.route('/', methods=['POST', ])
def parsePost():
    content = request.data
    xml2data.parseResp(content)
    return ""

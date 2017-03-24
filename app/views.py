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
    xmldict = xml2data.parseResp(content)
    #$def with (toUser,fromUser,createTime,content)
    return render_template("txt_resp_template.xml", toUser=xmldict['fromUser'], fromUser=xmldict['toUser'],content=xmldict['content'])

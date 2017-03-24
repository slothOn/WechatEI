__author__ = 'zxc'

from app import app
from flask import render_template, request
from app.utils import xml2data
import time

@app.route('/abc')
def index():
    return render_template("index.html", text="Hello World")

@app.route('/', methods=['POST', 'GET'])
def parsePost():
    content = request.data
    #xmldict = xml2data.parseResp(content)
    #$def with (toUser,fromUser,createTime,content)
    xmldict = {}
    xmldict['fromUser'] = 'abc'
    xmldict['toUser'] = 'def'
    xmldict['content'] = 'abcdef'
    print(xmldict['fromUser'])
    return render_template("txt_resp_template.xml", toUser=xmldict['fromUser'], fromUser=xmldict['toUser'],content=xmldict['content'], createTime=int(time.time()))

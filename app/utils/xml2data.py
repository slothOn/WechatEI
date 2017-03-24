__author__ = 'zxc'
from xml.etree.ElementTree import parse

def parseResp(txtdata):
    xml = parse(txtdata)
    content = xml.find("Content").text
    msgType = xml.find("MsgType").text
    fromUser = xml.find("FromUserName").text
    toUser = xml.find("ToUserName").text
    print(content)

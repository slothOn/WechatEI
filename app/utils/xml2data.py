__author__ = 'zxc'
from xml.etree.ElementTree import parse, fromstring

def parseResp(txtdata):
    xml = fromstring(txtdata)
    content = xml.find("Content").text
    msgType = xml.find("MsgType").text
    fromUser = xml.find("FromUserName").text
    toUser = xml.find("ToUserName").text
    dictdata = {}
    dictdata['content'] = content
    dictdata['msgType'] = msgType
    dictdata['fromUser'] = fromUser
    dictdata['toUser'] = toUser
    return dictdata

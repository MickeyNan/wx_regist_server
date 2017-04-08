#coding:utf-8
import xml.etree.ElementTree as ET

class Msg(object):
	def __init__(self,xmlData):
		self.ToUserName = xmlData.find('ToUserName').text
		self.FromUserName = xmlData.find('FromUserName').text
		self.CreateTime = xmlData.find('CreateTime').text
		self.MsgType = xmlData.find('MsgType').text
		self.MsgId = xmlData.find('MsgId').text

class TextMsg(Msg):
	def __init__(self,xmlData):
		Msg.__init__(self,xmlData)
		self.Content = xmlData.find('Content').text.encode("utf-8")

class ImageMsg(Msg):
	def __int__(self,xmlData):
		Msg.__init__(self,xmlData)
		self.PicUrl = xmlData.find('PicUrl').text
		self.MediaId = xmlData.find('MediaId').text


def parse_xml(webdata):
	if len(webdata) == 0:
		return None

	xmlData = ET.fromstring(webdata)

	msg_type = xmlData.find('MsgType').text

	if msg_type == "text":
		return TextMsg(xmlData).FromUserName
	if msg_type == "image":
		return ImageMsg(xmlData).FromUserName



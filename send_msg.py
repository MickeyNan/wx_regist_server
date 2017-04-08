import xml.etree.ElementTree as ET
import time

class Msg(object):
	def __init__(self):
		pass
	def create(self):
		return "sucess"


class TextMsg(Msg):
	def __init__(self,ToUserName,FromUserName,MsgType):
		self.__dict = dict()
		self.__dict['ToUserName'] = ToUserName
		self.__dict['FromUserName'] = FromUserName
		self.__dict['CreateTime'] = int(time.time())
		self.__dict['MsgType'] = MsgType

	def create(self):
		XmlForm = """
<xml>
<ToUserName><![CDATA[{ToUserName}]]></ToUserName>
<FromUserName><![CDATA[{FromUserName}]]></FromUserName>
<CreateTime>{CreateTime}</CreateTime>
<MsgType><![CDATA[{MsgType}]]></MsgType>
</xml>
"""
		return XmlForm.format(**self.__dict)

if __name__ == "__main__":
	text_msg = TextMsg('1','2','3')
	print text_msg.create()








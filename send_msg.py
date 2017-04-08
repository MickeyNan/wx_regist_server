import xml.etree.ElementTree as ET
import time

class Msg(object):
	def __init__(self):
		pass
	def create(self):
		return "sucess"


class TextMsg(Msg):
	def __init__(self,ToUserName,FromUserName,MsgType,Content):
		self.__dict = dict()
		self.__dict['ToUserName'] = ToUserName
		self.__dict['FromUserName'] = FromUserName
		self.__dict['CreateTime'] = int(time.time())
		self.__dict['MsgType'] = MsgType
		self.__dict['Content'] = Content

	def create(self):
		XmlForm = """
		<xml>
		<ToUserName><![CDATA[{ToUserName}]]></ToUserName>
		<FromUserName><![CDATA[{FromUserName}]]></FromUserName>
		<CreateTime>{CreateTime}</CreateTime>
		<MsgType><![CDATA[{MsgType}]]></MsgType>
		<Content><![CDATA[{Content}]]></Content>
		</xml>
		"""
		return XmlForm.format(**self.__dict)

if __name__ == "__main__":
	text_msg = TextMsg('1','2','3','4')
	print text_msg.create()








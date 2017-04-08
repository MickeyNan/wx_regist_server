import os
import sys
import commands
import json

wx_url_create_button = 'https://api.weixin.qq.com/cgi-bin/menu/create?access_token='


def getJSON(json_file):
	json_data = {}
	with open(json_file,"r") as f:
		json_data = json.load(f)

	return json_data

def curlWX(json_data,access_token,wx_url_create_button):
	wx_url = wx_url_create_button + access_token
	curl_command = "curl -H 'Content-Type: application/json' %s -X POST --data '%s'" %(wx_url,str(json_data))
	print curl_command
	status,return_value = commands.getstatusoutput(curl_command)
	print return_value

if __name__ == "__main__":
	json_data = getJSON('test_button.json')
	access_token = sys.argv[1]
	curlWX(json.dumps(json_data,ensure_ascii=False).encode('utf-8'),access_token,wx_url_create_button)
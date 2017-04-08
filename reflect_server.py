#!/usr/bin/ python
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from tornado import httpserver
#import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import hashlib
from tornado.options import define, options
from xml.dom import minidom,Node
import xml.etree.ElementTree as ET
import receive_msg
import send_msg

define("port", default=80, help="run on the given port", type=int)

def get_token(file_name):
    token = ''
    with open(file_name,"r") as f:
        for line in f:
            token = line.strip("\n")
            break
    return token

def checkSignatureWX(signature = '',timestamp = '',nonce = '',token = ''):
    tempList = [token,timestamp,nonce]
    sorted_temp = sorted(tempList)
    str_ = sorted_temp[0] + sorted_temp[1] + sorted_temp[2]
    if (str(hashlib.sha1(str_).hexdigest()) == signature):
        return 1
    else:
        return 0


#def getParam(ServerRequest):
    #uri = ServerRequest.uri


class MainHandler(tornado.web.RequestHandler):

    def post(self):
        signature = self.request.arguments['signature'][0]
        timestamp = self.request.arguments['timestamp'][0]
        nonce = self.request.arguments['nonce'][0]
        token = get_token('access_token.json')

        if not checkSignatureWX(signature,timestamp,nonce,token):
            self.write("Not Regular Request")
        else:
            try:
                msg = receive_msg.parse_xml(self.request.body)
                fromuser = msg.ToUserName
                touser = msg.FromUserName
                xml_message = send_msg.TextMsg(touser,fromuser,'transfer_customer_service').create()
                self.write(xml_message)
            except Exception as e:
                print e

    def get(self):
        pass



def main():
    tornado.options.parse_command_line()
    application = tornado.web.Application([
        (r"/", MainHandler),
    ])
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
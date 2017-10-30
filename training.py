import httplib, urllib, base64

body = ''
def training(objectRequest):
 try:
     conn = httplib.HTTPSConnection(objectRequest['connect'])
     conn.request("POST", "/face/v1.0/persongroups/{0}/train?{1}".format(objectRequest['groupId'], objectRequest['params']), body, objectRequest['headers'])
     response = conn.getresponse()
     data = response.read()
     print(data)
     conn.close()
 except Exception as e:
     print("Error Traning")

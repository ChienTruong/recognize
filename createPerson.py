import httplib, urllib, base64, json

Content_Type = 'application/json'

def createPerson(name, userData, objectRequest):
 objectRequest['headers']['Content-Type'] = Content_Type
 try:
  conn = httplib.HTTPSConnection(objectRequest['connect'])
  body = "{'name':'%s','userData':'%s'}" % (name, userData)
  conn.request("POST", "/face/v1.0/persongroups/{0}/persons?{1}".format(objectRequest['groupId'], objectRequest['params']), body, objectRequest['headers'])
  response = conn.getresponse()
  data = response.read()
  conn.close()
  return json.loads(data)['personId']
 except Exception as e:
  return None

import httplib, urllib, base64

Content_Type = 'application/octet-stream'

def addPerson(url, personId, objectRequest):
 objectRequest['headers']['Content-Type'] = Content_Type
 try:
  conn = httplib.HTTPSConnection(objectRequest['connect'])
  #body = "{\"url\":\"%s\"}" % (url)
  #read file
  filename = url
  print filename
  f = open(filename, 'rb')
  body = f.read()
  f.close()

  conn.request("POST", "/face/v1.0/persongroups/{0}/persons/{1}/persistedFaces?{2}".format(objectRequest['groupId'], personId, objectRequest['params']), body, objectRequest['headers'])
  response = conn.getresponse()
  data = response.read()
  print(data)
  conn.close()
 except Exception as e:
  print 'Error'

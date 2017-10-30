import httplib, urllib, base64, json

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': '',
}
personGroupId = ''
params = urllib.urlencode({
})
def getPerson(personId, oask, perGro):
 personGroupId = perGro
 headers['Ocp-Apim-Subscription-Key'] = oask
 try:
  conn = httplib.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
  conn.request("GET", "/face/v1.0/persongroups/{0}/persons/{1}?{2}".format(personGroupId, str(personId), params), "{body}", headers)
  response = conn.getresponse()
  data = response.read()
  parse = json.loads(data)
  conn.close()
  return parse['name']
 except Exception as e:
  print 'Error'
  #print("[Errno {0}] {1}".format(e.errno, e.strerror))
 return ''

import httplib, urllib, base64, json

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '',
}

params = urllib.urlencode({
})
def identify(faceIds, oask, groupId):
 body = {    
     "personGroupId":groupId,
     "faceIds":faceIds,
     "maxNumOfCandidatesReturned":1,
     "confidenceThreshold": 0.5
 }
 headers['Ocp-Apim-Subscription-Key'] = oask
 try:
  conn = httplib.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
  conn.request("POST", "/face/v1.0/identify?%s" % params, str(body), headers)
  response = conn.getresponse()
  data = response.read()
  print(data)
  conn.close()
  return json.loads(data)
 except Exception as e:
  print 'Error Identify'
  #print("[Errno {0}] {1}".format(e.errno, e.strerror))
 return ''

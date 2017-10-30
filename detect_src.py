import httplib, urllib, base64, json

#subscription_key = 'b21ca23853d34294a10eebd5ec501380'

uri_base = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0'

headers = {
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': '',
}

params = urllib.urlencode({
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age'
    #'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
})

body = ""
def detect(pathImage, subscription_key):
 headers['Ocp-Apim-Subscription-Key'] = subscription_key
 try:
  filename = pathImage
  f = open(filename, 'rb')
  print(f)
  body = f.read()
  f.close()
  conn = httplib.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
  conn.request("POST", "/face/v1.0/detect?%s" % params, body, headers)
  response = conn.getresponse()
  data = response.read()

  parsed = json.loads(data)
  print ("Response:")
  print (json.dumps(parsed, sort_keys=True, indent=2))
  conn.close()
  #return parsed[0]['faceId']
  return parsed
 except Exception as e:
  print 'Error Detect'
  #print("[Errno {0}] {1}".format(e.errno, e.strerror))
 return ''

#test
#detect("/home/chien/Pictures/Webcam/2017-10-16-122221.jpg", subscription_key)


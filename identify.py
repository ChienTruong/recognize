import detect_src as detect, identify_faces2 as iden, getPerson
# init
subscription_key = 'b21ca23853d34294a10eebd5ec501380'
groupId = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1'

def getCandidateIsConfidenceHighest(model):
 maxConfidence = 0
 candidates = model['candidates']
 candidateId = ''
 if len(candidates) == 0:
  return ''
 else:
  for i in candidates:
   if i['confidence'] > maxConfidence:
    maxConfidence = i['confidence']
    candidateId = i['personId']
  else:
   return candidateId

def addNameToResultDetect(objects, s, faceId):
 for i in objects:
  if i['faceId'] == faceId:
   i['name'] = s
   break
 
def identifyFace(pathImage, key):
 resultDetect = detect.detect(pathImage, key)
 #resultDetect = detect.detect(pathImage, key)
 if resultDetect == '':
  print 'Error ! Not Find Face In Image'
 else:
  faceIds = [str(i['faceId']) for i in resultDetect]
  resultIdentify = iden.identify(faceIds, key, groupId)
  if resultIdentify == '':
   print 'Error ! Not Candidates For Image'
  else:
   for i in resultIdentify:
    getIdCadidateHighest = getCandidateIsConfidenceHighest(i)
    if getIdCadidateHighest == '':
     addNameToResultDetect(resultDetect, '', i['faceId'])
    else:
     person = getPerson.getPerson(getIdCadidateHighest, key, groupId)
     if person == '':
      print 'Error ! Not Found Person In Group'
      addNameToResultDetect(resultDetect, '', i['faceId'])
     else:
      addNameToResultDetect(resultDetect, person, i['faceId'])
   else:
    print resultDetect
#identify('/home/chien/Pictures/Webcam/2017-10-17-100612.jpg', subscription_key)

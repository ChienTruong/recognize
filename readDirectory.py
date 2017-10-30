import os
import json, httplib, time
import createPerson, addPersonFace, training
import detect_src as ds

def readDirectory(folderRoot, objectRequest):
 root = folderRoot
 folderFace_Cognitive = list(os.walk(root))
 peoples = list(folderFace_Cognitive[0][1])
 for i in peoples:
  # name
  flag = createPerson.createPerson(str(i), 'id{0}'.format(i), objectRequest)
  folderPeople = list(os.walk("{0}/{1}".format(root, i)))
  images = list(folderPeople[0][2])
  if len(images) != 0:
   for j in images:
    # image
    addPersonFace.addPerson("{0}/{1}/{2}".format(folderRoot, i, j), flag, objectRequest)
    time.sleep(5)
 training.training(objectRequest)

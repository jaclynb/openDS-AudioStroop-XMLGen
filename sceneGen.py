#!/usr/bin/env python

import sceneCoreXML
import sceneFuncs

version = raw_input("Version number? ")

print ("Remember to rename the file to scene.xml or change the file name in AudioStroop.xml before using.")

if version != "":
	filename = "scene-" + version + ".xml"
else:
	filename = "scene.xml"

fd = open(filename, "w")

fd.write(sceneCoreXML.prologue)
fd.write(sceneCoreXML.sounds)
fd.write(sceneCoreXML.modelsOpenTag)
fd.write(sceneCoreXML.grass)
fd.write(sceneCoreXML.car)

sceneFuncs.makeRoad(fd, -24990.0, 24990.0)
sceneFuncs.startObjects(fd, 24350.0)
sceneFuncs.endObjects(fd, 21400.0)

lane0 = ["correctLane", "wrongLane", "wrongLane"]
lane1 = ["wrongLane", "correctLane", "wrongLane"]
lane2 = ["wrongLane", "wrongLane", "correctLane"]

signList = [lane2, lane1, lane0, lane2, lane0, lane2, lane1, lane2, lane0, \
lane2, lane0, lane1, lane2, lane1, lane0, lane1, lane0, lane1]

placeList = [304.26, 445.96, 588.72, 738.52, 878.71, 1021.25, 1171.75, 1322.00, 1464.40, 1611.25, \
1763.29, 1915.87, 2059.67, 2228.43, 2416.43, 2560.00, 2701.51, 2849.52]

for i in range(18):
	place = 24500.0 - placeList[i]
	sign0 = signList[i][0]
	sign1 = signList[i][1]
	sign2 = signList[i][2]
	sceneFuncs.makeBridgeSigns(fd, i, place, sign0, sign1, sign2)

fd.write(sceneCoreXML.modelsCloseTag)
fd.write(sceneCoreXML.geometries)
fd.write(sceneCoreXML.resetPoints)
fd.write(sceneCoreXML.gravity)
fd.write(sceneCoreXML.lights)
fd.write(sceneCoreXML.skyTexture)
fd.write(sceneCoreXML.epilogue)

fd.close()
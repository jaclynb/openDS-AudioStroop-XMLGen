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
sceneFuncs.startObjects(fd, 24500.0)
sceneFuncs.endObjects(fd, 20250.0)

place = 24200.0
sign0 = "wrongLane"
sign1 = "correctLane"
sign2 = "wrongLane"

for i in range(20):
	sceneFuncs.makeBridgeSigns(fd, i, place, sign0, sign1, sign2)
	place = place - 200

fd.write(sceneCoreXML.modelsCloseTag)
fd.write(sceneCoreXML.geometries)
fd.write(sceneCoreXML.resetPoints)
fd.write(sceneCoreXML.gravity)
fd.write(sceneCoreXML.lights)
fd.write(sceneCoreXML.skyTexture)
fd.write(sceneCoreXML.epilogue)

fd.close()
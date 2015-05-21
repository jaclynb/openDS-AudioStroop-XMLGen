#!/usr/bin/env python

import sceneCoreXML

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

fd.write(sceneCoreXML.modelsCloseTag)
fd.write(sceneCoreXML.geometries)
fd.write(sceneCoreXML.resetPoints)
fd.write(sceneCoreXML.gravity)
fd.write(sceneCoreXML.lights)
fd.write(sceneCoreXML.skyTexture)
fd.write(sceneCoreXML.epilogue)

fd.close()
#!/usr/bin/env python

import sceneGen, interactionGen

name = raw_input("Scenario name? ")

if name != "":
    sceneFilename = "scene-" + name + ".xml"
    interactionFilename = "interaction-" + name + ".xml"
else:
    sceneFilename = "scene.xml"
    interactionFilename = "interaction.xml"

# Make scene file
scenefd = open(sceneFilename, "w")

scenefd.write(sceneGen.prologue)
scenefd.write(sceneGen.sounds)
scenefd.write(sceneGen.modelsOpenTag)
scenefd.write(sceneGen.grass)
scenefd.write(sceneGen.car)

scenefd.write(sceneGen.makeRoad(-24990.0, 24990.0))
scenefd.write(sceneGen.startObjects(24250.0))
scenefd.write(sceneGen.endObjects(21400.0))

lane0 = ["correctLane", "wrongLane", "wrongLane"]
lane1 = ["wrongLane", "correctLane", "wrongLane"]
lane2 = ["wrongLane", "wrongLane", "correctLane"]

signList = [lane2, lane1, lane0, lane2, lane0, lane2, lane1, lane2, lane0, \
lane2, lane0, lane1, lane2, lane1, lane0, lane1, lane0, lane1]

placeList = [304.26, 445.96, 588.72, 738.52, 878.71, 1021.25, 1171.75, 1322.00, 1464.40, 1611.25, \
1763.29, 1915.87, 2059.67, 2228.43, 2416.43, 2560.00, 2701.51, 2849.52]

bridges = ""
for i in range(18):
    place = 24500.0 - placeList[i]
    sign0 = signList[i][0]
    sign1 = signList[i][1]
    sign2 = signList[i][2]
    bridges += sceneGen.makeBridgeSigns(i, place, sign0, sign1, sign2)

scenefd.write(bridges)
scenefd.write(sceneGen.modelsCloseTag)
scenefd.write(sceneGen.geometries)
scenefd.write(sceneGen.resetPoints)
scenefd.write(sceneGen.gravity)
scenefd.write(sceneGen.lights)
scenefd.write(sceneGen.skyTexture)
scenefd.write(sceneGen.epilogue)

scenefd.close()

# Make interaction file
interactionfd = open(interactionFilename, "w")

interactionfd.write(interactionGen.prologue)
interactionfd.write(interactionGen.activitiesOpenTag)
interactionfd.write(interactionGen.startActivities)
interactionfd.write(interactionGen.makeSignTimerActivities())
interactionfd.write(interactionGen.activitiesCloseTag)
interactionfd.write(interactionGen.triggersOpenTag)
interactionfd.write(interactionGen.startTrig)
interactionfd.write(interactionGen.endTrig)
interactionfd.write(interactionGen.makeTriggerActivities())
interactionfd.write(interactionGen.triggerCloseTag)
interactionfd.write(interactionGen.epilogue)

interactionfd.close()
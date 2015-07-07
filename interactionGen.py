#!/usr/bin/env python

import interactionFuncs

version = raw_input("Version number? ")

print ("Remember to rename the file to scene.xml or change the file name in AudioStroop.xml before using.")

if version != "":
	filename = "interaction-" + version + ".xml"
else:
	filename = "interaction.xml"

code = '<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n'
code += '<interaction xmlns="http://opends.eu/drivingtask/interaction" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://opends.eu/drivingtask/interaction ../../Schema/interaction.xsd">\n'
code += '\t<activities>\n'
code += '\t\t<activity id="Start_startRM" ref="">\n'
code += '\t\t\t<action delay="0.0" id="startReactionMeasurement" repeat="1"/>\n'
code += '\t\t</activity>\n'
code += '\t\t<activity id="Start_startRecording" ref="">\n'
code += '\t\t\t<action delay="0.0" id="startRecording" repeat="4">\n'
code += '\t\t\t\t<parameter name="track" value="1"/>\n'
code += '\t\t\t</action>\n'
code += '\t\t</activity>\n'
code += '\t\t<activity id="End_stopRecording" ref="">\n'
code += '\t\t\t<action delay="0.0" id="stopRecording" repeat="4"/>\n'
code += '\t\t</activity>\n'
code += '\t\t<activity id="End_pauseSimulation" ref="">\n'
code += '\t\t\t<action delay="0.0" id="pauseSimulation" repeat="4">\n'
code += '\t\t\t\t<parameter name="duration" value="0"/>\n'
code += '\t\t\t</action>\n'
code += '\t\t</activity>\n'

targetLaneList = ["2", "1", "0", "2", "0", "2", "1", "2", "0", "2", "0", "1", "2", "1", "0", "1", "0", "1"]
startLaneList =  ["1", "2", "1", "0", "2", "0", "2", "1", "2", "0", "2", "0", "1", "2", "1", "0", "1", "0"]
soundIDList = ["left1", "right1", "right1", "left2", "right2", "left2", "right1", "left1", "right2", \
				"left2", "right2", "left1", "left1", "right1", "right1", "left1", "right1", "left1"]

for i in range(18):
	sign = "BLC_Test_Block0_Trial" + str(i) + "_ContainerElement0"
	params = interactionFuncs.makeParameter("visible", "true")
	params += interactionFuncs.makeParameter("id", sign)
	contents = interactionFuncs.makeAction("0.1", "manipulateObject", "4", params)
	
	sign = "BLC_Test_Block0_Trial" + str(i) + "_ContainerElement1"
	params = interactionFuncs.makeParameter("visible", "true")
	params += interactionFuncs.makeParameter("id", sign)
	contents += interactionFuncs.makeAction("0.1", "manipulateObject", "4", params)
	
	sign = "BLC_Test_Block0_Trial" + str(i) + "_ContainerElement2"
	params = interactionFuncs.makeParameter("visible", "true")
	params += interactionFuncs.makeParameter("id", sign)
	contents += interactionFuncs.makeAction("0.1", "manipulateObject", "4", params)
	
	activityId = "BLC_Test_Block0_Trial" + str(i) + "_Trigger0_makeVisible_BLC_Test_Block0_Trial" + str(i) + "_ContainerElements"
	code += interactionFuncs.makeActivity(activityId, "", contents)

	params = interactionFuncs.makeParameter("minSteeringAngle", "0")
	params += interactionFuncs.makeParameter("targetLane", targetLaneList[i])
	params += interactionFuncs.makeParameter("startLane", startLaneList[i])
	params += interactionFuncs.makeParameter("taskCompletionAfterDistance", "117")
	params += interactionFuncs.makeParameter("taskCompletionAfterTime", "7000")
	params += interactionFuncs.makeParameter("timerID", "timer1")
	params += interactionFuncs.makeParameter("allowBreak", "true")
	params += interactionFuncs.makeParameter("successSound", "good")
	params += interactionFuncs.makeParameter("congruenceClass", "LaneChange")
	params += interactionFuncs.makeParameter("holdLaneFor", "2000")
	params += interactionFuncs.makeParameter("failSound", "fail")
	contents = interactionFuncs.makeAction("0.0", "setupLaneChangeReactionTimer", "1", params)
	
	activityId = "BLC_Test_Block0_Trial" + str(i) + "_Trigger0_setupBrakeLaneChangeReactionTimer"
	code += interactionFuncs.makeActivity(activityId, "", contents)

	params = interactionFuncs.makeParameter("soundID", soundIDList[i]);
	contents += interactionFuncs.makeAction("0.0", "playSound", "1", params);
	activityId = "BLC_Test_Block0_Trial" + str(i) + "_Trigger0_Sound_Stimulus"
	code += interactionFuncs.makeActivity(activityId, "", contents)

code += '\t</activities>\n'
code += '\t<triggers>\n'
code += '\t\t<trigger id="BLC_Test_Start_Trigger" priority="1">\n'
code += '\t\t\t<activities>\n'
code += '\t\t\t\t<activity ref="Start_startRM"/>\n'
code += '\t\t\t\t<activity ref="Start_startRecording"/>\n'
code += '\t\t\t</activities>\n'
code += '\t\t\t<condition>collideWith:BLC_Test_Start_Trigger</condition>\n'
code += '\t\t</trigger>\n'
code += '\t\t<trigger id="BLC_Test_End_Trigger" priority="1">\n'
code += '\t\t\t<activities>\n'
code += '\t\t\t\t<activity ref="End_stopRecording"/>\n'
code += '\t\t\t\t<activity ref="End_pauseSimulation"/>\n'
code += '\t\t\t</activities>\n'
code += '\t\t\t<condition>collideWith:BLC_Test_End_Trigger</condition>\n'
code += '\t\t</trigger>\n'

for i in range(18):
	refElements = "BLC_Test_Block0_Trial" + str(i) + "_Trigger0_makeVisible_BLC_Test_Block0_Trial" + str(i) + "_ContainerElements"
	refReactionTimer = "BLC_Test_Block0_Trial" + str(i) + "_Trigger0_setupBrakeLaneChangeReactionTimer"
	activities = "\t\t\t\t<activities>\n"
	activities += "\t\t\t\t\t" + interactionFuncs.makeActivtyRefOnly(refElements)
	activities += "\t\t\t\t\t" + interactionFuncs.makeActivtyRefOnly(refReactionTimer)
	activities += "\t\t\t\t</activities>\n"

	conditionContents = "collideWith:BLC_Test_Block0_Trial" + str(i) +"_Trigger0"
	conditions = "\t\t\t\t" + interactionFuncs.makeCondition(conditionContents)

	contents = interactionFuncs.makeTriggerContents(activities, conditions)
	
	triggerId = "BLC_Test_Block0_Trial" + str(i) + "_Trigger0"
	code += interactionFuncs.makeTrigger(triggerId, "1", contents)

	refStimulus = "BLC_Test_Block0_Trial" + str(i) + "_Trigger0_Sound_Stimulus"
	activities = "\t\t\t\t<activities>\n"
	activities += "\t\t\t\t\t" + interactionFuncs.makeActivtyRefOnly(refStimulus)
	activities += "\t\t\t\t</activities>\n"

	conditionContents = "collideWith:BLC_Test_Block0_Trial" + str(i) +"_Stimulus_Trigger0"
	conditions = "\t\t\t\t" + interactionFuncs.makeCondition(conditionContents)

	contents = interactionFuncs.makeTriggerContents(activities, conditions)
	
	triggerId = "BLC_Test_Block0_Trial" + str(i) + "_Stimulus_Trigger0"
	code += interactionFuncs.makeTrigger(triggerId, "1", contents)

code += '\t</triggers>\n'
code += '</interaction>\n'


fd = open(filename, "w")
fd.write(code)
fd.close()
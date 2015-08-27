#!/usr/bin/env python

import interactionFuncs

def makeActivity(triggerId, ref, contents):
	s = '\t\t<activity id="' + triggerId + '" ref="' + ref + '">\n'
	s += contents
	s += '\t\t</activity>\n'
	return s

def makeActivtyRefOnly(ref):
	return '<activity ref="' + ref + '"/>\n'

def makeActionNoParam(delay, triggerId, repeat):
	return '\t\t\t<action delay="' + delay + '" id="' + triggerId + '" repeat="' + repeat + '"/>\n'

def makeAction(delay, triggerId, repeat, params):
	s = '\t\t\t<action delay="' + delay + '" id="' + triggerId + '" repeat="' + repeat + '">\n'
	s += params
	s += '\t\t\t</action>\n'
	return s

def makeParameter(name, value):
	s = '\t\t\t\t<parameter name="' + name + '" value="' + value + '"/>\n'
	return s

def makeTrigger(triggerId, priority, contents):
	s = '\t\t\t<trigger id="' + triggerId + '" priority="' + priority + '">\n'
	s += contents
	s += '\t\t\t</trigger>\n'
	return s

def makeTriggerContents(activities, conditions):
	return activities + conditions

def makeCondition(contents):
	return '<condition>' + contents + '</condition>\n'

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
	params = makeParameter("visible", "true")
	params += makeParameter("id", sign)
	contents = makeAction("0.0", "manipulateObject", "1", params)
	
	sign = "BLC_Test_Block0_Trial" + str(i) + "_ContainerElement1"
	params = makeParameter("visible", "true")
	params += makeParameter("id", sign)
	contents += makeAction("0.0", "manipulateObject", "1", params)
	
	sign = "BLC_Test_Block0_Trial" + str(i) + "_ContainerElement2"
	params = makeParameter("visible", "true")
	params += makeParameter("id", sign)
	contents += makeAction("0.0", "manipulateObject", "1", params)
	
	activityId = "BLC_Test_Block0_Trial" + str(i) + "_Trigger0_makeVisible_BLC_Test_Block0_Trial" + str(i) + "_ContainerElements"
	code += makeActivity(activityId, "", contents)

	params = makeParameter("minSteeringAngle", "0")
	params += makeParameter("targetLane", targetLaneList[i])
	params += makeParameter("startLane", startLaneList[i])
	params += makeParameter("taskCompletionAfterDistance", "117")
	params += makeParameter("taskCompletionAfterTime", "7000")
	params += makeParameter("timerID", "timer1")
	params += makeParameter("allowBreak", "true")
	params += makeParameter("successSound", "good")
	params += makeParameter("congruenceClass", "LaneChange")
	params += makeParameter("holdLaneFor", "2000")
	params += makeParameter("failSound", "fail")
	contents = makeAction("0.0", "setupLaneChangeReactionTimer", "1", params)
	
	activityId = "BLC_Test_Block0_Trial" + str(i) + "_Trigger0_setupBrakeLaneChangeReactionTimer"
	code += makeActivity(activityId, "", contents)

	"""
	params = makeParameter("soundID", soundIDList[i]);
	contents = makeAction("0.0", "playSound", "1", params);
	activityId = "BLC_Test_Block0_Trial" + str(i) + "_Trigger0_Sound_Stimulus"
	code += makeActivity(activityId, "", contents)
	"""

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
	activities += "\t\t\t\t\t" + makeActivtyRefOnly(refElements)
	activities += "\t\t\t\t\t" + makeActivtyRefOnly(refReactionTimer)
	activities += "\t\t\t\t</activities>\n"

	conditionContents = "collideWith:BLC_Test_Block0_Trial" + str(i) +"_Trigger0"
	conditions = "\t\t\t\t" + makeCondition(conditionContents)

	contents = makeTriggerContents(activities, conditions)
	
	triggerId = "BLC_Test_Block0_Trial" + str(i) + "_Trigger0"
	code += makeTrigger(triggerId, "1", contents)

	"""
	refStimulus = "BLC_Test_Block0_Trial" + str(i) + "_Trigger0_Sound_Stimulus"
	activities = "\t\t\t\t<activities>\n"
	activities += "\t\t\t\t\t" + makeActivtyRefOnly(refStimulus)
	activities += "\t\t\t\t</activities>\n"

	conditionContents = "collideWith:BLC_Test_Block0_Trial" + str(i) +"_Stimulus_Trigger0"
	conditions = "\t\t\t\t" + makeCondition(conditionContents)

	contents = makeTriggerContents(activities, conditions)
	
	triggerId = "BLC_Test_Block0_Trial" + str(i) + "_Stimulus_Trigger0"
	code += makeTrigger(triggerId, "1", contents)
	"""

code += '\t</triggers>\n'
code += '</interaction>\n'


fd = open(filename, "w")
fd.write(code)
fd.close()
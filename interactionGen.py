#!/usr/bin/env python

prologue = '<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n' + \
'<interaction xmlns="http://opends.eu/drivingtask/interaction" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://opends.eu/drivingtask/interaction ../../Schema/interaction.xsd">\n'

activitiesOpenTag = '\t<activities>\n'

startActivities = '\t\t<activity id="Start_startRM" ref="">\n\
\t\t\t<action delay="0.0" id="startReactionMeasurement" repeat="1"/>\n\
\t\t</activity>\n\
\t\t<activity id="Start_startRecording" ref="">\n\
\t\t\t<action delay="0.0" id="startRecording" repeat="4">\n\
\t\t\t\t<parameter name="track" value="1"/>\n\
\t\t\t</action>\n\
\t\t</activity>\n\
\t\t<activity id="End_stopRecording" ref="">\n\
\t\t</activity>\n\
\t\t<activity id="End_pauseSimulation" ref="">\n\
\t\t\t<action delay="0.0" id="pauseSimulation" repeat="4">\n\
\t\t\t\t<parameter name="duration" value="0"/>\n\
\t\t\t</action>\n\
\t\t</activity>\n'

activitiesCloseTag = '\t</activities>\n'

triggersOpenTag = '\t<triggers>\n'

startTrig = '\t\t<trigger id="BLC_Test_Start_Trigger" priority="1">\n \
\t\t\t<activities>\n\
\t\t\t\t<activity ref="Start_startRM"/>\n\
\t\t\t\t<activity ref="Start_startRecording"/>\n\
\t\t\t</activities>\n\
\t\t\t<condition>collideWith:BLC_Test_Start_Trigger</condition>\n\
\t\t</trigger>\n'

endTrig = '\t\t<trigger id="BLC_Test_End_Trigger" priority="1">\n\
\t\t\t<activities>\n\
\t\t\t\t<activity ref="End_stopRecording"/>\n\
\t\t\t\t<activity ref="End_pauseSimulation"/>\n\
\t\t\t</activities>\n\
\t\t\t<condition>collideWith:BLC_Test_End_Trigger</condition>\n\
\t\t</trigger>\n'

triggerCloseTag = '\t</triggers>\n'

epilogue = '</interaction>\n'

targetLaneList = ["2", "1", "0", "2", "0", "2", "1", "2", "0", "2", "0", "1", "2", "1", "0", "1", "0", "1"]

startLaneList =  ["1", "2", "1", "0", "2", "0", "2", "1", "2", "0", "2", "0", "1", "2", "1", "0", "1", "0"]

soundIDList = ["left1", "right1", "right1", "left2", "right2", "left2", "right1", "left1", "right2", \
                "left2", "right2", "left1", "left1", "right1", "right1", "left1", "right1", "left1"]

def makeActivity(triggerId, ref, contents):
    activity = '\t\t<activity id="' + triggerId + '" ref="' + ref + '">\n'
    activity += contents
    activity += '\t\t</activity>\n'
    return activity

def makeActivtyRefOnly(ref):
    return '<activity ref="' + ref + '"/>\n'

def makeActionNoParam(delay, triggerId, repeat):
    return '\t\t\t<action delay="' + delay + '" id="' + triggerId + '" repeat="' + repeat + '"/>\n'

def makeAction(delay, triggerId, repeat, params):
    action = '\t\t\t<action delay="' + delay + '" id="' + triggerId + '" repeat="' + repeat + '">\n'
    action += params
    action += '\t\t\t</action>\n'
    return action

def makeParameter(name, value):
    param = '\t\t\t\t<parameter name="' + name + '" value="' + value + '"/>\n'
    return param

def makeTrigger(triggerId, priority, contents):
    trig = '\t\t<trigger id="' + triggerId + '" priority="' + priority + '">\n'
    trig += contents
    trig += '\t\t</trigger>\n'
    return trig

def makeTriggerContents(activities, conditions):
    return activities + conditions

def makeCondition(contents):
    return '<condition>' + contents + '</condition>\n'

def makeSignTimerActivities():
    activities = ""
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
        activities += makeActivity(activityId, "", contents)

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
        activities += makeActivity(activityId, "", contents)

        """
        params = makeParameter("soundID", soundIDList[i]);
        contents = makeAction("0.0", "playSound", "1", params);
        activityId = "BLC_Test_Block0_Trial" + str(i) + "_Trigger0_Sound_Stimulus"
        activities += makeActivity(activityId, "", contents)
        """
    return activities

def makeTriggerActivities():
    triggers = ""
    for i in range(18):
        refElements = "BLC_Test_Block0_Trial" + str(i) + "_Trigger0_makeVisible_BLC_Test_Block0_Trial" + str(i) + "_ContainerElements"
        refReactionTimer = "BLC_Test_Block0_Trial" + str(i) + "_Trigger0_setupBrakeLaneChangeReactionTimer"
        activities = "\t\t\t<activities>\n"
        activities += "\t\t\t\t" + makeActivtyRefOnly(refElements)
        activities += "\t\t\t\t" + makeActivtyRefOnly(refReactionTimer)
        activities += "\t\t\t</activities>\n"

        conditionContents = "collideWith:BLC_Test_Block0_Trial" + str(i) +"_Trigger0"
        conditions = "\t\t\t" + makeCondition(conditionContents)

        contents = makeTriggerContents(activities, conditions)
        
        triggerId = "BLC_Test_Block0_Trial" + str(i) + "_Trigger0"
        triggers += makeTrigger(triggerId, "1", contents)

        """
        refStimulus = "BLC_Test_Block0_Trial" + str(i) + "_Trigger0_Sound_Stimulus"
        activities = "\t\t\t<activities>\n"
        activities += "\t\t\t\t" + makeActivtyRefOnly(refStimulus)
        activities += "\t\t\t</activities>\n"

        conditionContents = "collideWith:BLC_Test_Block0_Trial" + str(i) +"_Stimulus_Trigger0"
        conditions = "\t\t\t" + makeCondition(conditionContents)

        contents = makeTriggerContents(activities, conditions)
        
        triggerId = "BLC_Test_Block0_Trial" + str(i) + "_Stimulus_Trigger0"
        triggers += makeTrigger(triggerId, "1", contents)
        """
    return triggers

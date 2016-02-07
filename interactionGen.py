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
\t\t\t<action delay="0.0" id="stopRecording" repeat="4"/>\n\
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


track0Sounds = ["toneL1", "toneR1", "toneR1", "toneL2", "ttsR2panright", "ttsL2panleft", "ttsL1panright", "ttsR1panleft", "ttsR2panleft", "ttsL2panright", "ttsL2panleft", "ttsR1panright", "toneL1", "toneR1", "ttsL1panright", "ttsL1panleft", "ttsR1panleft", "ttsR1panright"]
track1Sounds = ["toneL1", "toneR1", "toneR1", "toneR2", "toneR2", "toneL2", "toneL1", "toneL1", "toneR2", "toneL2", "toneR2", "toneR1", "toneR1", "toneR1", "toneR1", "toneL1", "toneL1", "toneL1"]
track2Sounds = ["toneR1", "toneL1", "toneL1", "toneL2", "toneL2", "toneR2", "toneR1", "toneR1", "toneL2", "toneR2", "toneL2", "toneL1", "toneL1", "toneL1", "toneL1", "toneR1", "toneR1", "toneR1"]
track3Sounds = ["ttsL1panleft", "ttsR1panright", "ttsR1panright", "ttsR2panright", "ttsR2panright", "ttsL2panleft", "ttsL1panleft", "ttsL1panleft", "ttsR2panright", "ttsL2panleft", "ttsR2panright", "ttsR1panright", "ttsR1panright", "ttsR1panright", "ttsR1panright", "ttsL1panleft", "ttsL1panleft", "ttsL1panleft"]
track4Sounds = ["ttsR1panleft", "ttsL1panright", "ttsL1panright", "ttsL2panleft", "ttsL2panright", "ttsR2panleft", "ttsR1panright", "ttsR1panleft", "ttsL2panright", "ttsR2panleft", "ttsL2panright", "ttsL1panleft", "ttsL1panleft", "ttsL1panright", "ttsL1panright", "ttsR1panleft", "ttsR1panright", "ttsR1panleft"]
track5Sounds = ["ttsL1panright", "ttsR1panleft", "ttsR1panleft", "ttsL2panleft", "ttsR2panleft", "ttsL2panright", "ttsR1panright", "ttsL1panright", "ttsR2panleft", "ttsL2panright", "ttsR2panleft", "ttsL1panleft", "ttsL1panleft", "ttsR1panleft", "ttsR1panleft", "ttsL1panright", "ttsR1panright", "ttsL1panright"]
track6Sounds = ["toneL1", "toneR1", "toneR1", "toneR2", "toneR2", "toneL2", "toneL1", "toneL1", "toneR2", "toneL2", "toneR2", "toneR1", "toneR1", "toneR1", "toneR1", "toneL1", "toneL1", "toneL1"]
track7Sounds = ["toneR1", "toneL1", "toneL1", "toneL2", "toneL2", "toneR2", "toneR1", "toneR1", "toneL2", "toneR2", "toneL2", "toneL1", "toneL1", "toneL1", "toneL1", "toneR1", "toneR1", "toneR1"]
track8Sounds = ["ttsL1panleft", "ttsR1panright", "ttsR1panright", "ttsR2panright", "ttsR2panright", "ttsL2panleft", "ttsL1panleft", "ttsL1panleft", "ttsR2panright", "ttsL2panleft", "ttsR2panright", "ttsR1panright", "ttsR1panright", "ttsR1panright", "ttsR1panright", "ttsL1panleft", "ttsL1panleft", "ttsL1panleft"]
track9Sounds = ["ttsR1panleft", "ttsL1panright", "ttsL1panright", "ttsL2panleft", "ttsL2panright", "ttsR2panleft", "ttsR1panright", "ttsR1panleft", "ttsL2panright", "ttsR2panleft", "ttsL2panright", "ttsL1panleft", "ttsL1panleft", "ttsL1panright", "ttsL1panright", "ttsR1panleft", "ttsR1panright", "ttsR1panleft"]
track10Sounds = ["ttsL1panright", "ttsR1panleft", "ttsR1panleft", "ttsL2panleft", "ttsR2panleft", "ttsL2panright", "ttsR1panright", "ttsL1panright", "ttsR2panleft", "ttsL2panright", "ttsR2panleft", "ttsL1panleft", "ttsL1panleft", "ttsR1panleft", "ttsR1panleft", "ttsL1panright", "ttsR1panright", "ttsL1panright"]
track11Sounds = ["ttsR1panright", "ttsL1panleft", "ttsL1panleft", "ttsL2panleft", "ttsL2panleft", "ttsR2panright", "ttsR1panright", "ttsR1panright", "ttsL2panleft", "ttsR2panright", "ttsL2panleft", "ttsL1panleft", "ttsL1panleft", "ttsL1panleft", "ttsL1panleft", "ttsR1panright", "ttsR1panright", "ttsR1panright"]
track12Sounds = ["ttsR1panright", "ttsL1panleft", "ttsL1panleft", "ttsL2panleft", "ttsL2panleft", "ttsR2panright", "ttsR1panright", "ttsR1panright", "ttsL2panleft", "ttsR2panright", "ttsL2panleft", "ttsL1panleft", "ttsL1panleft", "ttsL1panleft", "ttsL1panleft", "ttsR1panright", "ttsR1panright", "ttsR1panright"]
#track13 is visual only, no sounds

soundIDList = track0Sounds
startLaneList = [1, 2, 1, 0, 2, 0, 2, 1, 2, 0, 2, 0, 1, 2, 1, 0, 1, 0]
targetLaneList = [2, 1, 0, 2, 0, 2, 1, 2, 0, 2, 0, 1, 2, 1, 0, 1, 0, 1]

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

def makeSignTimerActivities(sound):
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
        params += makeParameter("targetLane", str(targetLaneList[i]))
        params += makeParameter("startLane", str(startLaneList[i]))
        params += makeParameter("taskCompletionAfterDistance", "120") #Used to be 117 for 60 kph
        params += makeParameter("taskCompletionAfterTime", "4000") #Used to be 7000 for 60 kph
        params += makeParameter("timerID", "timer1")
        params += makeParameter("allowBrake", "true")
        params += makeParameter("successSound", "good")
        params += makeParameter("congruenceClass", "LaneChange")
        params += makeParameter("holdLaneFor", "800") #Used to be 1000 for 60 kph
        params += makeParameter("failSound", "fail")
        params += makeParameter("comment", "Sign " + str(i+1))
        contents = makeAction("0.0", "setupLaneChangeReactionTimer", "1", params)
        
        activityId = "BLC_Test_Block0_Trial" + str(i) + "_Trigger0_setupBrakeLaneChangeReactionTimer"
        activities += makeActivity(activityId, "", contents)

        if sound == True:
            params = makeParameter("soundID", soundIDList[i]);
            contents = makeAction("0.0", "playSound", "1", params);
            activityId = "BLC_Test_Block0_Trial" + str(i) + "_Trigger0_Sound_Stimulus"
            activities += makeActivity(activityId, "", contents)
        
    return activities

def makeTriggerActivities(sound):
    triggers = ""
    for i in range(18):
        refElements = "BLC_Test_Block0_Trial" + str(i) + "_Trigger0_makeVisible_BLC_Test_Block0_Trial" + str(i) + "_ContainerElements"
        activities = "\t\t\t<activities>\n"
        activities += "\t\t\t\t" + makeActivtyRefOnly(refElements)
        if sound == False:
            refReactionTimer = "BLC_Test_Block0_Trial" + str(i) + "_Trigger0_setupBrakeLaneChangeReactionTimer"
            activities += "\t\t\t\t" + makeActivtyRefOnly(refReactionTimer)
        activities += "\t\t\t</activities>\n"

        conditionContents = "collideWith:BLC_Test_Block0_Trial" + str(i) +"_Trigger0"
        conditions = "\t\t\t" + makeCondition(conditionContents)

        contents = makeTriggerContents(activities, conditions)
        
        triggerId = "BLC_Test_Block0_Trial" + str(i) + "_Trigger0"
        triggers += makeTrigger(triggerId, "1", contents)

        if sound == True:
            refStimulus = "BLC_Test_Block0_Trial" + str(i) + "_Trigger0_Sound_Stimulus"
            refReactionTimer = "BLC_Test_Block0_Trial" + str(i) + "_Trigger0_setupBrakeLaneChangeReactionTimer"
            activities = "\t\t\t<activities>\n"
            activities += "\t\t\t\t" + makeActivtyRefOnly(refStimulus)
            activities += "\t\t\t\t" + makeActivtyRefOnly(refReactionTimer)
            activities += "\t\t\t</activities>\n"

            conditionContents = "collideWith:BLC_Test_Block0_Trial" + str(i) +"_Stimulus_Trigger0"
            conditions = "\t\t\t" + makeCondition(conditionContents)

            contents = makeTriggerContents(activities, conditions)
            
            triggerId = "BLC_Test_Block0_Trial" + str(i) + "_Stimulus_Trigger0"
            triggers += makeTrigger(triggerId, "1", contents)
            
    return triggers

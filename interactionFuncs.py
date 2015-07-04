#!/usr/bin/env python

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
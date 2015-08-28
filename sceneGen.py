#!/usr/bin/env python

prologue = '<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n' + \
'<scene xmlns="http://opends.eu/drivingtask/scene" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"' \
' xsi:schemaLocation="http://opends.eu/drivingtask/scene ../../Schema/scene.xsd">\n'

sounds = '\t<sounds>\n\
\t\t<sound id="good" key="Sounds/Effects/Beep.ogg">\n\
\t\t\t<positional value="false"/>\n\
\t\t\t<directional value="false"/>\n\
\t\t\t<loop>false</loop>\n\
\t\t\t<volume>0.5</volume>\n\
\t\t\t<pitch>1.0</pitch>\n\
\t\t</sound>\n\
\t\t<sound id="fail" key="Sounds/Effects/Beep.ogg">\n\
\t\t\t<positional value="false"/>\n\
\t\t\t<directional value="false"/>\n\
\t\t\t<loop>false</loop>\n\
\t\t\t<volume>0.5</volume>\n\
\t\t\t<pitch>1.0</pitch>\n\
\t\t</sound>\n\
\t\t<sound id="left1" key="Sounds/AudioStroop/toneleft350msec.wav">\n\
\t\t\t<positional value="false"/>\n\
\t\t\t<directional value="false"/>\n\
\t\t\t<loop>false</loop>\n\
\t\t\t<volume>0.5</volume>\n\
\t\t\t<pitch>1.0</pitch>\n\
\t\t</sound>\n\
\t\t<sound id="right1" key="Sounds/AudioStroop/toneright350msec.wav">\n\
\t\t\t<positional value="false"/>\n\
\t\t\t<directional value="false"/>\n\
\t\t\t<loop>false</loop>\n\
\t\t\t<volume>0.5</volume>\n\
\t\t\t<pitch>1.0</pitch>\n\
\t\t</sound>\n\
\t\t<sound id="left2" key="Sounds/AudioStroop/consecutiveleft.wav">\n\
\t\t\t<positional value="false"/>\n\
\t\t\t<directional value="false"/>\n\
\t\t\t<loop>false</loop>\n\
\t\t\t<volume>0.5</volume>\n\
\t\t\t<pitch>1.0</pitch>\n\
\t\t</sound>\n\
\t\t<sound id="right2" key="Sounds/AudioStroop/consecutiveright.wav">\n\
\t\t\t<positional value="false"/>\n\
\t\t\t<directional value="false"/>\n\
\t\t\t<loop>false</loop>\n\
\t\t\t<volume>0.5</volume>\n\
\t\t\t<pitch>1.0</pitch>\n\
\t\t</sound>\n\
\t</sounds>\n'

modelsOpenTag = '\t<models>\n'

grass = '\t\t<model id="grass" key="Scenes/land_plain_50x5/land_plain.scene" ref="">\n\
\t\t\t<mass>0</mass>\n\
\t\t\t<visible>true</visible>\n\
\t\t\t<collisionShape>meshShape</collisionShape>\n\
\t\t\t<scale>\n\
\t\t\t\t<vector jtype="java_lang_Float" size="3">\n\
\t\t\t\t\t<entry>1.0</entry>\n\
\t\t\t\t\t<entry>1.0</entry>\n\
\t\t\t\t\t<entry>1.0</entry>\n\
\t\t\t\t</vector>\n\
\t\t\t</scale>\n\
\t\t\t<rotation quaternion="false">\n\
\t\t\t\t<vector jtype="java_lang_Float" size="3">\n\
\t\t\t\t\t<entry>0.0</entry>\n\
\t\t\t\t\t<entry>0.0</entry>\n\
\t\t\t\t\t<entry>0.0</entry>\n\
\t\t\t\t</vector>\n\
\t\t\t</rotation>\n\
\t\t\t<translation>\n\
\t\t\t\t<vector jtype="java_lang_Float" size="3">\n\
\t\t\t\t\t<entry>0.0</entry>\n\
\t\t\t\t\t<entry>0.0</entry>\n\
\t\t\t\t\t<entry>0.0</entry>\n\
\t\t\t\t</vector>\n\
\t\t\t</translation>\n\
\t\t</model>\n'

car = '\t\t<model id="Ferrari" key="Models/Cars/drivingCars/Ferrari/Car.scene" ref="">\n\
\t\t\t<mass>800</mass>\n\
\t\t\t<visible>true</visible>\n\
\t\t\t<collisionShape>meshShape</collisionShape>\n\
\t\t\t<scale>\n\
\t\t\t\t<vector jtype="java_lang_Float" size="3">\n\
\t\t\t\t\t<entry>1.0</entry>\n\
\t\t\t\t\t<entry>1.0</entry>\n\
\t\t\t\t\t<entry>1.0</entry>\n\
\t\t\t\t</vector>\n\
\t\t\t</scale>\n\
\t\t\t<rotation quaternion="false">\n\
\t\t\t\t<vector jtype="java_lang_Float" size="3">\n\
\t\t\t\t\t<entry>0.0</entry>\n\
\t\t\t\t\t<entry>0.0</entry>\n\
\t\t\t\t\t<entry>0.0</entry>\n\
\t\t\t\t</vector>\n\
\t\t\t</rotation>\n\
\t\t\t<translation>\n\
\t\t\t\t<vector jtype="java_lang_Float" size="3">\n\
\t\t\t\t\t<entry>0.0</entry>\n\
\t\t\t\t\t<entry>0.0</entry>\n\
\t\t\t\t\t<entry>24500.0</entry>\n\
\t\t\t\t</vector>\n\
\t\t\t</translation>\n\
\t\t</model>\n'

modelsCloseTag = '\t</models>\n'

geometries = '\t<geometries>\n\
\t\t<point id="idealPoint1">\n\
\t\t\t<translation>\n\
\t\t\t\t<vector jtype="java_lang_Float" size="3">\n\
\t\t\t\t\t<entry>0.0</entry>\n\
\t\t\t\t\t<entry>0.0</entry>\n\
\t\t\t\t\t<entry>24400.0</entry>\n\
\t\t\t\t</vector>\n\
\t\t\t</translation>\n\
\t\t</point>\n\
\t\t<point id="idealPoint2">\n\
\t\t\t<translation>\n\
\t\t\t\t<vector jtype="java_lang_Float" size="3">\n\
\t\t\t\t\t<entry>0.0</entry>\n\
\t\t\t\t\t<entry>0.0</entry>\n\
\t\t\t\t\t<entry>20250.0</entry>\n\
\t\t\t\t</vector>\n\
\t\t\t</translation>\n\
\t\t</point>\n\
\t</geometries>\n'

resetPoints = '\t<resetPoints>\n\
\t\t<resetPoint id="reset1">\n\
\t\t\t<translation>\n\
\t\t\t\t<vector jtype="java_lang_Float" size="3">\n\
\t\t\t\t\t<entry>0</entry>\n\
\t\t\t\t\t<entry>0</entry>\n\
\t\t\t\t\t<entry>4995</entry>\n\
\t\t\t\t</vector>\n\
\t\t\t</translation>\n\
\t\t\t<rotation quaternion="false">\n\
\t\t\t\t<vector jtype="java_lang_Float" size="3">\n\
\t\t\t\t\t<entry>0</entry>\n\
\t\t\t\t\t<entry>0</entry>\n\
\t\t\t\t\t<entry>0</entry>\n\
\t\t\t\t</vector>\n\
\t\t\t</rotation>\n\
\t\t</resetPoint>\n\
\t</resetPoints>\n'

gravity = '\t<gravity>9.81</gravity>\n'

lights = '\t<lights>\n\
\t\t<directionalLight>\n\
\t\t\t<direction>\n\
\t\t\t\t<vector jtype="java_lang_Float" size="3">\n\
\t\t\t\t\t<entry>0.5</entry>\n\
\t\t\t\t\t<entry>-0.5</entry>\n\
\t\t\t\t\t<entry>0.5</entry>\n\
\t\t\t\t</vector>\n\
\t\t\t</direction>\n\
\t\t\t<color>\n\
\t\t\t\t<vector jtype="java_lang_Float" size="4">\n\
\t\t\t\t\t<entry>0.7</entry>\n\
\t\t\t\t\t<entry>0.7</entry>\n\
\t\t\t\t\t<entry>0.7</entry>\n\
\t\t\t\t\t<entry>0.7</entry>\n\
\t\t\t\t</vector>\n\
\t\t\t</color>\n\
\t\t</directionalLight>\n\
\t\t<directionalLight>\n\
\t\t\t<direction>\n\
\t\t\t\t<vector jtype="java_lang_Float" size="3">\n\
\t\t\t\t\t<entry>-0.5</entry>\n\
\t\t\t\t\t<entry>-0.5</entry>\n\
\t\t\t\t\t<entry>0.5</entry>\n\
\t\t\t\t</vector>\n\
\t\t\t</direction>\n\
\t\t\t<color>\n\
\t\t\t\t<vector jtype="java_lang_Float" size="4">\n\
\t\t\t\t\t<entry>0.7</entry>\n\
\t\t\t\t\t<entry>0.7</entry>\n\
\t\t\t\t\t<entry>0.7</entry>\n\
\t\t\t\t\t<entry>0.7</entry>\n\
\t\t\t\t</vector>\n\
\t\t\t</color>\n\
\t\t</directionalLight>\n\
\t\t<directionalLight>\n\
\t\t\t<direction>\n\
\t\t\t\t<vector jtype="java_lang_Float" size="3">\n\
\t\t\t\t\t<entry>0.5</entry>\n\
\t\t\t\t\t<entry>-0.5</entry>\n\
\t\t\t\t\t<entry>-0.5</entry>\n\
\t\t\t\t</vector>\n\
\t\t\t</direction>\n\
\t\t\t<color>\n\
\t\t\t\t<vector jtype="java_lang_Float" size="4">\n\
\t\t\t\t\t<entry>0.7</entry>\n\
\t\t\t\t\t<entry>0.7</entry>\n\
\t\t\t\t\t<entry>0.7</entry>\n\
\t\t\t\t\t<entry>0.7</entry>\n\
\t\t\t\t</vector>\n\
\t\t\t</color>\n\
\t\t</directionalLight>\n\
\t\t<directionalLight>\n\
\t\t\t<direction>\n\
\t\t\t\t<vector jtype="java_lang_Float" size="3">\n\
\t\t\t\t\t<entry>-0.5</entry>\n\
\t\t\t\t\t<entry>-0.5</entry>\n\
\t\t\t\t\t<entry>-0.5</entry>\n\
\t\t\t\t</vector>\n\
\t\t\t</direction>\n\
\t\t\t<color>\n\
\t\t\t\t<vector jtype="java_lang_Float" size="4">\n\
\t\t\t\t\t<entry>0.7</entry>\n\
\t\t\t\t\t<entry>0.7</entry>\n\
\t\t\t\t\t<entry>0.7</entry>\n\
\t\t\t\t\t<entry>0.7</entry>\n\
\t\t\t\t</vector>\n\
\t\t\t</color>\n\
\t\t</directionalLight>\n\
\t</lights>\n'

skyTexture = '\t<skyTexture>Textures/Sky/Bright/hills.dds</skyTexture>\n'

epilogue = '</scene>'

def roadSeg(tvector3):
    roadSeg = '\t\t<model id="road_3lane" key="Models/road_segments/road_3lane/road_3lane.scene" ref="">\n' + \
    '\t\t\t<mass>0</mass>\n' + \
    '\t\t\t<visible>true</visible>\n' + \
    '\t\t\t<collisionShape>meshShape</collisionShape>\n' + \
    '\t\t\t<scale>\n' + \
    '\t\t\t\t<vector jtype="java_lang_Float" size="3">\n' + \
    '\t\t\t\t\t<entry>1.0</entry>\n' + \
    '\t\t\t\t\t<entry>1.0</entry>\n' + \
    '\t\t\t\t\t<entry>1.0</entry>\n' + \
    '\t\t\t\t</vector>\n' + \
    '\t\t\t</scale>\n' + \
    '\t\t\t<rotation quaternion="false">\n' + \
    '\t\t\t\t<vector jtype="java_lang_Float" size="3">\n' + \
    '\t\t\t\t\t<entry>0.0</entry>\n' + \
    '\t\t\t\t\t<entry>0.0</entry>\n' + \
    '\t\t\t\t\t<entry>0.0</entry>\n' + \
    '\t\t\t\t</vector>\n' + \
    '\t\t\t</rotation>\n' + \
    '\t\t\t<translation>\n' + \
    '\t\t\t\t<vector jtype="java_lang_Float" size="3">\n' + \
    '\t\t\t\t\t<entry>0.0</entry>\n' + \
    '\t\t\t\t\t<entry>0.0</entry>\n' + \
    '\t\t\t\t\t<entry>' + str(tvector3) + '</entry>\n' + \
    '\t\t\t\t</vector>\n' + \
    '\t\t\t</translation>\n' + \
    '\t\t</model>\n'
    return roadSeg

def makeRoad(startPoint, endPoint):
    road = ""
    currTVector3 = startPoint
    increment = 20
    for i in range (int(startPoint), int(endPoint), increment):
        road += roadSeg(currTVector3)
        currTVector3 += increment
    return road

def startObjects(place):
    startObs = '\t\t<model id="Exp_BLC_150_StartPosition_Trigger" key="Models/trigger/trigger.scene" ref="">\n' + \
    '\t\t\t<mass>0</mass>\n' + \
    '\t\t\t<visible>false</visible>\n' + \
    '\t\t\t<collisionShape>none</collisionShape>\n' + \
    '\t\t\t<scale>\n' + \
    '\t\t\t\t<vector jtype="java_lang_Float" size="3">\n' + \
    '\t\t\t\t\t<entry>1.0</entry>\n' + \
    '\t\t\t\t\t<entry>1.0</entry>\n' + \
    '\t\t\t\t\t<entry>1.0</entry>\n' + \
    '\t\t\t\t</vector>\n' + \
    '\t\t\t</scale>\n' + \
    '\t\t\t<rotation quaternion="false">\n' + \
    '\t\t\t\t<vector jtype="java_lang_Float" size="3">\n' + \
    '\t\t\t<entry>0.0</entry>\n' + \
    '\t\t\t<entry>0.0</entry>\n' + \
    '\t\t\t<entry>0.0</entry>\n' + \
    '\t\t\t\t</vector>\n' + \
    '\t\t\t</rotation>\n' + \
    '\t\t\t<translation>\n' + \
    '\t\t\t\t<vector jtype="java_lang_Float" size="3">\n' + \
    '\t\t\t<entry>0.0</entry>\n' + \
    '\t\t\t<entry>0.0</entry>\n' + \
    '\t\t\t<entry>' + str(place + 100) + '</entry>\n' + \
    '\t\t\t\t</vector>\n' + \
    '\t\t\t</translation>\n' + \
    '\t\t</model>\n' + \
    '\t\t<model id="BLC_Test_Start_Trigger" key="Models/trigger/trigger.scene" ref="">\n' + \
    '\t\t\t<mass>0</mass>\n' + \
    '\t\t\t<visible>false</visible>\n' + \
    '\t\t\t<collisionShape>none</collisionShape>\n' + \
    '\t\t\t<scale>\n' + \
    '\t\t\t\t<vector jtype="java_lang_Float" size="3">\n' + \
    '\t\t\t\t\t<entry>1.0</entry>\n' + \
    '\t\t\t\t\t<entry>1.0</entry>\n' + \
    '\t\t\t\t\t<entry>1.0</entry>\n' + \
    '\t\t\t\t</vector>\n' + \
    '\t\t\t</scale>\n' + \
    '\t\t\t<rotation quaternion="false">\n' + \
    '\t\t\t\t<vector jtype="java_lang_Float" size="3">\n' + \
    '\t\t\t\t\t<entry>0.0</entry>\n' + \
    '\t\t\t\t\t<entry>0.0</entry>\n' + \
    '\t\t\t\t\t<entry>0.0</entry>\n' + \
    '\t\t\t\t</vector>\n' + \
    '\t\t\t</rotation>\n' + \
    '\t\t\t<translation>\n' + \
    '\t\t\t\t<vector jtype="java_lang_Float" size="3">\n' + \
    '\t\t\t\t\t<entry>0.0</entry>\n' + \
    '\t\t\t\t\t<entry>0.0</entry>\n' + \
    '\t\t\t\t\t<entry>' + str(place) + '</entry>\n' + \
    '\t\t\t\t</vector>\n' + \
    '\t\t\t</translation>\n' + \
    '\t\t</model>\n' + \
    '\t\t<model id="BLC_Test_StartSignBridge" key="Models/sign_bridges/bridge_3lane/bridge_3lane.scene" ref="">\n' + \
    '\t\t\t<mass>0</mass>\n' + \
    '\t\t\t<visible>true</visible>\n' + \
    '\t\t\t<collisionShape>none</collisionShape>\n' + \
    '\t\t\t<scale>\n' + \
    '\t\t\t\t<vector jtype="java_lang_Float" size="3">\n' + \
    '\t\t\t\t\t<entry>1.0</entry>\n' + \
    '\t\t\t\t\t<entry>1.0</entry>\n' + \
    '\t\t\t\t\t<entry>1.0</entry>\n' + \
    '\t\t\t\t</vector>\n' + \
    '\t\t\t</scale>\n' + \
    '\t\t\t<rotation quaternion="false">\n' + \
    '\t\t\t\t<vector jtype="java_lang_Float" size="3">\n' + \
    '\t\t\t\t\t<entry>0.0</entry>\n' + \
    '\t\t\t\t\t<entry>0.0</entry>\n' + \
    '\t\t\t\t\t<entry>0.0</entry>\n' + \
    '\t\t\t\t</vector>\n' + \
    '\t\t\t</rotation>\n' + \
    '\t\t\t<translation>\n' + \
    '\t\t\t\t<vector jtype="java_lang_Float" size="3">\n' + \
    '\t\t\t\t\t<entry>0.0</entry>\n' + \
    '\t\t\t\t\t<entry>0.0</entry>\n' + \
    '\t\t\t\t\t<entry>' + str(place) + '</entry>\n' + \
    '\t\t\t\t</vector>\n' + \
    '\t\t\t</translation>\n' + \
    '\t\t</model>\n' + \
    '\t\t<model id="BLC_Test_StartSignPanel" key="Models/sign_panels/Start/panel_sign.scene" ref="">\n' + \
    '\t\t\t<mass>0</mass>\n' + \
    '\t\t\t<visible>true</visible>\n' + \
    '\t\t\t<collisionShape>none</collisionShape>\n' + \
    '\t\t\t<scale>\n' + \
    '\t\t\t\t<vector jtype="java_lang_Float" size="3">\n' + \
    '\t\t\t\t\t<entry>1.0</entry>\n' + \
    '\t\t\t\t\t<entry>1.0</entry>\n' + \
    '\t\t\t\t\t<entry>1.0</entry>\n' + \
    '\t\t\t\t</vector>\n' + \
    '\t\t\t</scale>\n' + \
    '\t\t\t<rotation quaternion="false">\n' + \
    '\t\t\t\t<vector jtype="java_lang_Float" size="3">\n' + \
    '\t\t\t\t\t<entry>0.0</entry>\n' + \
    '\t\t\t\t\t<entry>0.0</entry>\n' + \
    '\t\t\t\t\t<entry>0.0</entry>\n' + \
    '\t\t\t\t</vector>\n' + \
    '\t\t\t</rotation>\n' + \
    '\t\t\t<translation>\n' + \
    '\t\t\t\t<vector jtype="java_lang_Float" size="3">\n' + \
    '\t\t\t\t\t<entry>0.0</entry>\n' + \
    '\t\t\t\t\t<entry>0.0</entry>\n' + \
    '\t\t\t\t\t<entry>' + str(place) + '</entry>\n' + \
    '\t\t\t\t</vector>\n' + \
    '\t\t\t</translation>\n' + \
    '\t\t</model>\n'
    return startObs

def endObjects(place):
    endObs = '\t\t<model id="BLC_Test_End_Trigger" key="Models/trigger/trigger.scene" ref="">\n' + \
    '\t\t\t<mass>0</mass>\n' + \
    '\t\t\t<visible>false</visible>\n' + \
    '\t\t\t<collisionShape>none</collisionShape>\n' + \
    '\t\t\t<scale>\n' + \
    '\t\t\t\t<vector jtype="java_lang_Float" size="3">\n' + \
    '\t\t\t\t\t<entry>1.0</entry>\n' + \
    '\t\t\t\t\t<entry>1.0</entry>\n' + \
    '\t\t\t\t\t<entry>1.0</entry>\n' + \
    '\t\t\t\t</vector>\n' + \
    '\t\t\t</scale>\n' + \
    '\t\t\t<rotation quaternion="false">\n' + \
    '\t\t\t\t<vector jtype="java_lang_Float" size="3">\n' + \
    '\t\t\t\t\t<entry>0.0</entry>\n' + \
    '\t\t\t\t\t<entry>0.0</entry>\n' + \
    '\t\t\t\t\t<entry>0.0</entry>\n' + \
    '\t\t\t\t</vector>\n' + \
    '\t\t\t</rotation>\n' + \
    '\t\t\t<translation>\n' + \
    '\t\t\t\t<vector jtype="java_lang_Float" size="3">\n' + \
    '\t\t\t\t\t<entry>0.0</entry>\n' + \
    '\t\t\t\t\t<entry>0.0</entry>\n' + \
    '\t\t\t\t\t<entry>' + str(place) + '</entry>\n' + \
    '\t\t\t\t</vector>\n' + \
    '\t\t\t</translation>\n' + \
    '\t\t</model>\n' + \
    '\t\t<model id="BLC_Test_FinishSignBridge" key="Models/sign_bridges/bridge_3lane/bridge_3lane.scene" ref="">\n' + \
    '\t\t\t<mass>0</mass>\n' + \
    '\t\t\t<visible>true</visible>\n' + \
    '\t\t\t<collisionShape>none</collisionShape>\n' + \
    '\t\t\t<scale>\n' + \
    '\t\t\t\t<vector jtype="java_lang_Float" size="3">\n' + \
    '\t\t\t\t\t<entry>1.0</entry>\n' + \
    '\t\t\t\t\t<entry>1.0</entry>\n' + \
    '\t\t\t\t\t<entry>1.0</entry>\n' + \
    '\t\t\t\t</vector>\n' + \
    '\t\t\t</scale>\n' + \
    '\t\t\t<rotation quaternion="false">\n' + \
    '\t\t\t\t<vector jtype="java_lang_Float" size="3">\n' + \
    '\t\t\t\t\t<entry>0.0</entry>\n' + \
    '\t\t\t\t\t<entry>0.0</entry>\n' + \
    '\t\t\t\t\t<entry>0.0</entry>\n' + \
    '\t\t\t\t</vector>\n' + \
    '\t\t\t</rotation>\n' + \
    '\t\t\t<translation>\n' + \
    '\t\t\t\t<vector jtype="java_lang_Float" size="3">\n' + \
    '\t\t\t\t\t<entry>0.0</entry>\n' + \
    '\t\t\t\t\t<entry>0.0</entry>\n' + \
    '\t\t\t\t\t<entry>' + str(place) + '</entry>\n' + \
    '\t\t\t\t</vector>\n' + \
    '\t\t\t</translation>\n' + \
    '\t\t</model>\n' + \
    '\t\t<model id="BLC_Test_FinishSignPanel" key="Models/sign_panels/Finish/panel_sign.scene" ref="">\n' + \
    '\t\t\t<mass>0</mass>\n' + \
    '\t\t\t<visible>true</visible>\n' + \
    '\t\t\t<collisionShape>none</collisionShape>\n' + \
    '\t\t\t<scale>\n' + \
    '\t\t\t\t<vector jtype="java_lang_Float" size="3">\n' + \
    '\t\t\t\t\t<entry>1.0</entry>\n' + \
    '\t\t\t\t\t<entry>1.0</entry>\n' + \
    '\t\t\t\t\t<entry>1.0</entry>\n' + \
    '\t\t\t\t</vector>\n' + \
    '\t\t\t</scale>\n' + \
    '\t\t\t<rotation quaternion="false">\n' + \
    '\t\t\t\t<vector jtype="java_lang_Float" size="3">\n' + \
    '\t\t\t\t\t<entry>0.0</entry>\n' + \
    '\t\t\t\t\t<entry>0.0</entry>\n' + \
    '\t\t\t\t\t<entry>0.0</entry>\n' + \
    '\t\t\t\t</vector>\n' + \
    '\t\t\t</rotation>\n' + \
    '\t\t\t<translation>\n' + \
    '\t\t\t\t<vector jtype="java_lang_Float" size="3">\n' + \
    '\t\t\t\t\t<entry>0.0</entry>\n' + \
    '\t\t\t\t\t<entry>0.0</entry>\n' + \
    '\t\t\t\t\t<entry>' + str(place) + '</entry>\n' + \
    '\t\t\t\t</vector>\n' + \
    '\t\t\t</translation>\n' + \
    '\t\t</model>\n'
    return endObs

def makeBridgeSignsTriggers(num, place, sign0, sign1, sign2, stimTrig):
    bridgeSigns = ""
    if stimTrig == True:
        bridgeSigns += makeStimulusTrigger(num, place+53.3)
    #bridgeSigns += makeSignTrigger(num, place+40)
    bridgeSigns += makeSignTrigger(num, place+53.3)
    bridgeSigns += makeBridge(num, place)
    bridgeSigns += makeSign(num, place, 0, sign0)
    bridgeSigns += makeSign(num, place, 1, sign1)
    bridgeSigns += makeSign(num, place, 2, sign2)
    return bridgeSigns

def makeSignTrigger(num, place):
    num = str(num)
    place = str(place)
    signTrig = '\t\t<model id="BLC_Test_Block0_Trial' + num + '_Trigger0" key="Models/trigger/trigger.scene" ref="">\n' + \
    '\t\t\t<mass>0</mass>\n' + \
    '\t\t\t<visible>false</visible>\n' + \
    '\t\t\t<collisionShape>none</collisionShape>\n' + \
    '\t\t\t<scale>\n' + \
    '\t\t\t\t<vector jtype="java_lang_Float" size="3">\n' + \
    '\t\t\t\t\t<entry>1.0</entry>\n' + \
    '\t\t\t\t\t<entry>1.0</entry>\n' + \
    '\t\t\t\t\t<entry>1.0</entry>\n' + \
    '\t\t\t\t</vector>\n' + \
    '\t\t\t</scale>\n' + \
    '\t\t\t<rotation quaternion="false">\n' + \
    '\t\t\t\t<vector jtype="java_lang_Float" size="3">\n' + \
    '\t\t\t\t\t<entry>0.0</entry>\n' + \
    '\t\t\t\t\t<entry>0.0</entry>\n' + \
    '\t\t\t\t\t<entry>0.0</entry>\n' + \
    '\t\t\t\t</vector>\n' + \
    '\t\t\t</rotation>\n' + \
    '\t\t\t<translation>\n' + \
    '\t\t\t\t<vector jtype="java_lang_Float" size="3">\n' + \
    '\t\t\t\t\t<entry>0.0</entry>\n' + \
    '\t\t\t\t\t<entry>0.0</entry>\n' + \
    '\t\t\t\t\t<entry>' + place + '</entry>\n' + \
    '\t\t\t\t</vector>\n' + \
    '\t\t\t</translation>\n' + \
    '\t\t</model>\n'
    return signTrig

def makeStimulusTrigger(num, place):
    num = str(num)
    place = str(place)
    stimTrig = '\t\t<model id="BLC_Test_Block0_Trial' + num + '_Stimulus_Trigger0" key="Models/trigger/trigger.scene" ref="">\n' + \
    '\t\t\t<mass>0</mass>\n' + \
    '\t\t\t<visible>false</visible>\n' + \
    '\t\t\t<collisionShape>none</collisionShape>\n' + \
    '\t\t\t<scale>\n' + \
    '\t\t\t\t<vector jtype="java_lang_Float" size="3">\n' + \
    '\t\t\t\t\t<entry>1.0</entry>\n' + \
    '\t\t\t\t\t<entry>1.0</entry>\n' + \
    '\t\t\t\t\t<entry>1.0</entry>\n' + \
    '\t\t\t\t</vector>\n' + \
    '\t\t\t</scale>\n' + \
    '\t\t\t<rotation quaternion="false">\n' + \
    '\t\t\t\t<vector jtype="java_lang_Float" size="3">\n' + \
    '\t\t\t\t\t<entry>0.0</entry>\n' + \
    '\t\t\t\t\t<entry>0.0</entry>\n' + \
    '\t\t\t\t\t<entry>0.0</entry>\n' + \
    '\t\t\t\t</vector>\n' + \
    '\t\t\t</rotation>\n' + \
    '\t\t\t<translation>\n' + \
    '\t\t\t\t<vector jtype="java_lang_Float" size="3">\n' + \
    '\t\t\t\t\t<entry>0.0</entry>\n' + \
    '\t\t\t\t\t<entry>0.0</entry>\n' + \
    '\t\t\t\t\t<entry>' + place + '</entry>\n' + \
    '\t\t\t\t</vector>\n' + \
    '\t\t\t</translation>\n' + \
    '\t\t</model>\n'
    return stimTrig

def makeBridge(num, place):
    num = str(num)
    place = str(place)
    bridge = '\t\t<model id="BLC_Test_Block0_Trial' + num + '_Container" key="Models/sign_bridges/bridge_3lane/bridge_3lane.scene" ref="">\n' + \
    '\t\t\t<mass>0</mass>\n' + \
    '\t\t\t<visible>true</visible>\n' + \
    '\t\t\t<collisionShape>none</collisionShape>\n' + \
    '\t\t\t<scale>\n' + \
    '\t\t\t\t<vector jtype="java_lang_Float" size="3">\n' + \
    '\t\t\t\t\t<entry>1.0</entry>\n' + \
    '\t\t\t\t\t<entry>1.0</entry>\n' + \
    '\t\t\t\t\t<entry>1.0</entry>\n' + \
    '\t\t\t\t</vector>\n' + \
    '\t\t\t</scale>\n' + \
    '\t\t\t<rotation quaternion="false">\n' + \
    '\t\t\t\t<vector jtype="java_lang_Float" size="3">\n' + \
    '\t\t\t\t\t<entry>0.0</entry>\n' + \
    '\t\t\t\t\t<entry>0.0</entry>\n' + \
    '\t\t\t\t\t<entry>0.0</entry>\n' + \
    '\t\t\t\t</vector>\n' + \
    '\t\t\t</rotation>\n' + \
    '\t\t\t<translation>\n' + \
    '\t\t\t\t<vector jtype="java_lang_Float" size="3">\n' + \
    '\t\t\t\t\t<entry>0.0</entry>\n' + \
    '\t\t\t\t\t<entry>0.0</entry>\n' + \
    '\t\t\t\t\t<entry>' + place + '</entry>\n' + \
    '\t\t\t\t</vector>\n' + \
    '\t\t\t</translation>\n' + \
    '\t\t</model>\n'
    return bridge

def makeSign(num, place, signNum, kind):
    num = str(num)
    place = str(place)

    if (kind == "wrongLane"):
        signType = 'Models/sign_panels/Brake/panel_sign.scene'
    else: # "correctLane"
        signType = 'Models/sign_panels/LaneChange/panel_sign.scene'

    horizPosList = [3.7, 0.0, -3.7]
    horizPos = str(horizPosList[signNum])
    sign = '\t\t<model id="BLC_Test_Block0_Trial' + num + '_ContainerElement' + str(signNum) + '" key="' + signType + '" ref="">\n' + \
    '\t\t\t<mass>0</mass>\n' + \
    '\t\t\t<visible>false</visible>\n' + \
    '\t\t\t<collisionShape>none</collisionShape>\n' + \
    '\t\t\t<scale>\n' + \
    '\t\t\t\t<vector jtype="java_lang_Float" size="3">\n' + \
    '\t\t\t\t\t<entry>1.0</entry>\n' + \
    '\t\t\t\t\t<entry>1.0</entry>\n' + \
    '\t\t\t\t\t<entry>1.0</entry>\n' + \
    '\t\t\t\t</vector>\n' + \
    '\t\t\t</scale>\n' + \
    '\t\t\t<rotation quaternion="false">\n' + \
    '\t\t\t\t<vector jtype="java_lang_Float" size="3">\n' + \
    '\t\t\t\t\t<entry>0.0</entry>\n' + \
    '\t\t\t\t\t<entry>0.0</entry>\n' + \
    '\t\t\t\t\t<entry>0.0</entry>\n' + \
    '\t\t\t\t</vector>\n' + \
    '\t\t\t</rotation>\n' + \
    '\t\t\t<translation>\n' + \
    '\t\t\t\t<vector jtype="java_lang_Float" size="3">\n' + \
    '\t\t\t\t\t<entry>' +  horizPos + '</entry>\n' + \
    '\t\t\t\t\t<entry>0.0</entry>\n' + \
    '\t\t\t\t\t<entry>' + place + '</entry>\n' + \
    '\t\t\t\t</vector>\n' + \
    '\t\t\t</translation>\n' + \
    '\t\t\t<ambientLight>\n' + \
    '\t\t\t<color>\n' + \
    '\t\t\t\t<vector jtype="java_lang_Float" size="4">\n' + \
    '\t\t\t\t\t<entry>1.5</entry>\n' + \
    '\t\t\t\t\t<entry>1.5</entry>\n' + \
    '\t\t\t\t\t<entry>1.5</entry>\n' + \
    '\t\t\t\t\t<entry>1.5</entry>\n' + \
    '\t\t\t\t</vector>\n' + \
    '\t\t\t</color>\n' + \
    '\t\t\t</ambientLight>\n' + \
    '\t\t</model>\n'
    return sign
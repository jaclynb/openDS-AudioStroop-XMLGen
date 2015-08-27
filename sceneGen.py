#!/usr/bin/env python

def roadSeg(fd, tvector3):
    road = '    <model id="road_3lane" key="Models/road_segments/road_3lane/road_3lane.scene" ref="">\n\
        <mass>0</mass>\n\
        <visible>true</visible>\n\
        <collisionShape>meshShape</collisionShape>\n\
        <scale>\n\
            <vector jtype="java_lang_Float" size="3">\n\
                <entry>1.0</entry>\n\
                <entry>1.0</entry>\n\
                <entry>1.0</entry>\n\
            </vector>\n\
        </scale>\n\
        <rotation quaternion="false">\n\
            <vector jtype="java_lang_Float" size="3">\n\
                <entry>0.0</entry>\n\
                <entry>0.0</entry>\n\
                <entry>0.0</entry>\n\
            </vector>\n\
        </rotation>\n\
        <translation>\n\
            <vector jtype="java_lang_Float" size="3">\n\
                <entry>0.0</entry>\n\
                <entry>0.0</entry>\n\
                <entry>' + str(tvector3) + '</entry>\n\
            </vector>\n\
        </translation>\n\
    </model>\n'
    fd.write(road)

def makeRoad(fd, startPoint, endPoint):
    currTVector3 = startPoint
    increment = 20
    for i in range (int(startPoint), int(endPoint), increment):
        roadSeg(fd, currTVector3)
        currTVector3 += increment

def startObjects(fd, place):
    startObs = '        <model id="Exp_BLC_150_StartPosition_Trigger" key="Models/trigger/trigger.scene" ref="">\n\
                <mass>0</mass>\n\
                <visible>false</visible>\n\
                <collisionShape>none</collisionShape>\n\
                <scale>\n\
                    <vector jtype="java_lang_Float" size="3">\n\
                        <entry>1.0</entry>\n\
                        <entry>1.0</entry>\n\
                        <entry>1.0</entry>\n\
                    </vector>\n\
                </scale>\n\
                <rotation quaternion="false">\n\
                    <vector jtype="java_lang_Float" size="3">\n\
                        <entry>0.0</entry>\n\
                        <entry>0.0</entry>\n\
                        <entry>0.0</entry>\n\
                    </vector>\n\
                </rotation>\n\
                <translation>\n\
                    <vector jtype="java_lang_Float" size="3">\n\
                        <entry>0.0</entry>\n\
                        <entry>0.0</entry>\n\
                        <entry>' + str(place + 100) + '</entry>\n\
                    </vector>\n\
                </translation>\n\
            </model>\n\
            <model id="BLC_Test_Start_Trigger" key="Models/trigger/trigger.scene" ref="">\n\
                <mass>0</mass>\n\
                <visible>false</visible>\n\
                <collisionShape>none</collisionShape>\n\
                <scale>\n\
                    <vector jtype="java_lang_Float" size="3">\n\
                        <entry>1.0</entry>\n\
                        <entry>1.0</entry>\n\
                        <entry>1.0</entry>\n\
                    </vector>\n\
                </scale>\n\
                <rotation quaternion="false">\n\
                    <vector jtype="java_lang_Float" size="3">\n\
                        <entry>0.0</entry>\n\
                        <entry>0.0</entry>\n\
                        <entry>0.0</entry>\n\
                    </vector>\n\
                </rotation>\n\
                <translation>\n\
                    <vector jtype="java_lang_Float" size="3">\n\
                        <entry>0.0</entry>\n\
                        <entry>0.0</entry>\n\
                        <entry>' + str(place) + '</entry>\n\
                    </vector>\n\
                </translation>\n\
            </model>\n\
            <model id="BLC_Test_StartSignBridge" key="Models/sign_bridges/bridge_3lane/bridge_3lane.scene" ref="">\n\
                <mass>0</mass>\n\
                <visible>true</visible>\n\
                <collisionShape>none</collisionShape>\n\
                <scale>\n\
                    <vector jtype="java_lang_Float" size="3">\n\
                        <entry>1.0</entry>\n\
                        <entry>1.0</entry>\n\
                        <entry>1.0</entry>\n\
                    </vector>\n\
                </scale>\n\
                <rotation quaternion="false">\n\
                    <vector jtype="java_lang_Float" size="3">\n\
                        <entry>0.0</entry>\n\
                        <entry>0.0</entry>\n\
                        <entry>0.0</entry>\n\
                    </vector>\n\
                </rotation>\n\
                <translation>\n\
                    <vector jtype="java_lang_Float" size="3">\n\
                        <entry>0.0</entry>\n\
                        <entry>0.0</entry>\n\
                        <entry>' + str(place) + '</entry>\n\
                    </vector>\n\
                </translation>\n\
            </model>\n\
            <model id="BLC_Test_StartSignPanel" key="Models/sign_panels/Start/panel_sign.scene" ref="">\n\
                <mass>0</mass>\n\
                <visible>true</visible>\n\
                <collisionShape>none</collisionShape>\n\
                <scale>\n\
                    <vector jtype="java_lang_Float" size="3">\n\
                        <entry>1.0</entry>\n\
                        <entry>1.0</entry>\n\
                        <entry>1.0</entry>\n\
                    </vector>\n\
                </scale>\n\
                <rotation quaternion="false">\n\
                    <vector jtype="java_lang_Float" size="3">\n\
                        <entry>0.0</entry>\n\
                        <entry>0.0</entry>\n\
                        <entry>0.0</entry>\n\
                    </vector>\n\
                </rotation>\n\
                <translation>\n\
                    <vector jtype="java_lang_Float" size="3">\n\
                        <entry>0.0</entry>\n\
                        <entry>0.0</entry>\n\
                        <entry>' + str(place) + '</entry>\n\
                    </vector>\n\
                </translation>\n\
            </model>\n'
    fd.write(startObs)

def endObjects(fd, place):
    endObs = '        <model id="BLC_Test_End_Trigger" key="Models/trigger/trigger.scene" ref="">\n\
                <mass>0</mass>\n\
                <visible>false</visible>\n\
                <collisionShape>none</collisionShape>\n\
                <scale>\n\
                    <vector jtype="java_lang_Float" size="3">\n\
                        <entry>1.0</entry>\n\
                        <entry>1.0</entry>\n\
                        <entry>1.0</entry>\n\
                    </vector>\n\
                </scale>\n\
                <rotation quaternion="false">\n\
                    <vector jtype="java_lang_Float" size="3">\n\
                        <entry>0.0</entry>\n\
                        <entry>0.0</entry>\n\
                        <entry>0.0</entry>\n\
                    </vector>\n\
                </rotation>\n\
                <translation>\n\
                    <vector jtype="java_lang_Float" size="3">\n\
                        <entry>0.0</entry>\n\
                        <entry>0.0</entry>\n\
                        <entry>' + str(place) + '</entry>\n\
                    </vector>\n\
                </translation>\n\
            </model>\n\
            <model id="BLC_Test_FinishSignBridge" key="Models/sign_bridges/bridge_3lane/bridge_3lane.scene" ref="">\n\
                <mass>0</mass>\n\
                <visible>true</visible>\n\
                <collisionShape>none</collisionShape>\n\
                <scale>\n\
                    <vector jtype="java_lang_Float" size="3">\n\
                        <entry>1.0</entry>\n\
                        <entry>1.0</entry>\n\
                        <entry>1.0</entry>\n\
                    </vector>\n\
                </scale>\n\
                <rotation quaternion="false">\n\
                    <vector jtype="java_lang_Float" size="3">\n\
                        <entry>0.0</entry>\n\
                        <entry>0.0</entry>\n\
                        <entry>0.0</entry>\n\
                    </vector>\n\
                </rotation>\n\
                <translation>\n\
                    <vector jtype="java_lang_Float" size="3">\n\
                        <entry>0.0</entry>\n\
                        <entry>0.0</entry>\n\
                        <entry>' + str(place) + '</entry>\n\
                    </vector>\n\
                </translation>\n\
            </model>\n\
            <model id="BLC_Test_FinishSignPanel" key="Models/sign_panels/Finish/panel_sign.scene" ref="">\n\
                <mass>0</mass>\n\
                <visible>true</visible>\n\
                <collisionShape>none</collisionShape>\n\
                <scale>\n\
                    <vector jtype="java_lang_Float" size="3">\n\
                        <entry>1.0</entry>\n\
                        <entry>1.0</entry>\n\
                        <entry>1.0</entry>\n\
                    </vector>\n\
                </scale>\n\
                <rotation quaternion="false">\n\
                    <vector jtype="java_lang_Float" size="3">\n\
                        <entry>0.0</entry>\n\
                        <entry>0.0</entry>\n\
                        <entry>0.0</entry>\n\
                    </vector>\n\
                </rotation>\n\
                <translation>\n\
                    <vector jtype="java_lang_Float" size="3">\n\
                        <entry>0.0</entry>\n\
                        <entry>0.0</entry>\n\
                        <entry>' + str(place) + '</entry>\n\
                    </vector>\n\
                </translation>\n\
            </model>\n'
    fd.write(endObs)

def makeBridgeSigns(fd, num, place, sign0, sign1, sign2):
    #makeStimulusTrigger(fd, num, place+53.3)
    #makeSignTrigger(fd, num, place+40)
    makeSignTrigger(fd, num, place+53.3)
    makeBridge(fd, num, place)
    makeSign(fd, num, place, 0, sign0)
    makeSign(fd, num, place, 1, sign1)
    makeSign(fd, num, place, 2, sign2)

def makeSignTrigger(fd, num, place):
    num = str(num)
    place = str(place)
    signTrig = '        <model id="BLC_Test_Block0_Trial' + num + '_Trigger0" key="Models/trigger/trigger.scene" ref="">\n\
                <mass>0</mass>\n\
                <visible>false</visible>\n\
                <collisionShape>none</collisionShape>\n\
                <scale>\n\
                    <vector jtype="java_lang_Float" size="3">\n\
                        <entry>1.0</entry>\n\
                        <entry>1.0</entry>\n\
                        <entry>1.0</entry>\n\
                    </vector>\n\
                </scale>\n\
                <rotation quaternion="false">\n\
                    <vector jtype="java_lang_Float" size="3">\n\
                        <entry>0.0</entry>\n\
                        <entry>0.0</entry>\n\
                        <entry>0.0</entry>\n\
                    </vector>\n\
                </rotation>\n\
                <translation>\n\
                    <vector jtype="java_lang_Float" size="3">\n\
                        <entry>0.0</entry>\n\
                        <entry>0.0</entry>\n\
                        <entry>' + place + '</entry>\n\
                    </vector>\n\
                </translation>\n\
            </model>\n'
    fd.write(signTrig)

def makeStimulusTrigger(fd, num, place):
    num = str(num)
    place = str(place)
    stimTrig = '        <model id="BLC_Test_Block0_Trial' + num + '_Stimulus_Trigger0" key="Models/trigger/trigger.scene" ref="">\n\
                <mass>0</mass>\n\
                <visible>false</visible>\n\
                <collisionShape>none</collisionShape>\n\
                <scale>\n\
                    <vector jtype="java_lang_Float" size="3">\n\
                        <entry>1.0</entry>\n\
                        <entry>1.0</entry>\n\
                        <entry>1.0</entry>\n\
                    </vector>\n\
                </scale>\n\
                <rotation quaternion="false">\n\
                    <vector jtype="java_lang_Float" size="3">\n\
                        <entry>0.0</entry>\n\
                        <entry>0.0</entry>\n\
                        <entry>0.0</entry>\n\
                    </vector>\n\
                </rotation>\n\
                <translation>\n\
                    <vector jtype="java_lang_Float" size="3">\n\
                        <entry>0.0</entry>\n\
                        <entry>0.0</entry>\n\
                        <entry>' + place + '</entry>\n\
                    </vector>\n\
                </translation>\n\
            </model>\n'
    fd.write(stimTrig)

def makeBridge(fd, num, place):
    num = str(num)
    place = str(place)
    bridge = '        <model id="BLC_Test_Block0_Trial' + num + '_Container" key="Models/sign_bridges/bridge_3lane/bridge_3lane.scene" ref="">\n\
                <mass>0</mass>\n\
                <visible>true</visible>\n\
                <collisionShape>none</collisionShape>\n\
                <scale>\n\
                    <vector jtype="java_lang_Float" size="3">\n\
                        <entry>1.0</entry>\n\
                        <entry>1.0</entry>\n\
                        <entry>1.0</entry>\n\
                    </vector>\n\
                </scale>\n\
                <rotation quaternion="false">\n\
                    <vector jtype="java_lang_Float" size="3">\n\
                        <entry>0.0</entry>\n\
                        <entry>0.0</entry>\n\
                        <entry>0.0</entry>\n\
                    </vector>\n\
                </rotation>\n\
                <translation>\n\
                    <vector jtype="java_lang_Float" size="3">\n\
                        <entry>0.0</entry>\n\
                        <entry>0.0</entry>\n\
                        <entry>' + place + '</entry>\n\
                    </vector>\n\
                </translation>\n\
            </model>\n'
    fd.write(bridge)

def makeSign(fd, num, place, signNum, kind):
    num = str(num)
    place = str(place)

    if (kind == "wrongLane"):
        signType = 'Models/sign_panels/Brake/panel_sign.scene'
    else: # "correctLane"
        signType = 'Models/sign_panels/LaneChange/panel_sign.scene'

    horizPosList = [3.7, 0.0, -3.7]
    horizPos = str(horizPosList[signNum])
    sign = '        <model id="BLC_Test_Block0_Trial' + num + '_ContainerElement' + str(signNum) + '" key="' + signType + '" ref="">\n\
                <mass>0</mass>\n\
                <visible>false</visible>\n\
                <collisionShape>none</collisionShape>\n\
                <scale>\n\
                    <vector jtype="java_lang_Float" size="3">\n\
                        <entry>1.0</entry>\n\
                        <entry>1.0</entry>\n\
                        <entry>1.0</entry>\n\
                    </vector>\n\
                </scale>\n\
                <rotation quaternion="false">\n\
                    <vector jtype="java_lang_Float" size="3">\n\
                        <entry>0.0</entry>\n\
                        <entry>0.0</entry>\n\
                        <entry>0.0</entry>\n\
                    </vector>\n\
                </rotation>\n\
                <translation>\n\
                    <vector jtype="java_lang_Float" size="3">\n\
                        <entry>' +  horizPos + '</entry>\n\
                        <entry>0.0</entry>\n\
                        <entry>' + place + '</entry>\n\
                    </vector>\n\
                </translation>\n\
                <ambientLight>\n\
                    <color>\n\
                        <vector jtype="java_lang_Float" size="4">\n\
                            <entry>1.5</entry>\n\
                            <entry>1.5</entry>\n\
                            <entry>1.5</entry>\n\
                            <entry>1.5</entry>\n\
                        </vector>\n\
                    </color>\n\
                </ambientLight>\n\
            </model>\n'
    fd.write(sign)


prologue = '<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n' + \
'<scene xmlns="http://opends.eu/drivingtask/scene" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"' \
' xsi:schemaLocation="http://opends.eu/drivingtask/scene ../../Schema/scene.xsd">\n'

sounds = '    <sounds>\n\
        <sound id="good" key="Sounds/Effects/Beep.ogg">\n\
            <positional value="false"/>\n\
            <directional value="false"/>\n\
            <loop>false</loop>\n\
            <volume>0.5</volume>\n\
            <pitch>1.0</pitch>\n\
        </sound>\n\
        <sound id="fail" key="Sounds/Effects/Beep.ogg">\n\
            <positional value="false"/>\n\
            <directional value="false"/>\n\
            <loop>false</loop>\n\
            <volume>0.5</volume>\n\
            <pitch>1.0</pitch>\n\
        </sound>\n\
        <sound id="left1" key="Sounds/AudioStroop/toneleft350msec.wav">\n\
            <positional value="false"/>\n\
            <directional value="false"/>\n\
            <loop>false</loop>\n\
            <volume>0.5</volume>\n\
            <pitch>1.0</pitch>\n\
        </sound>\n\
        <sound id="right1" key="Sounds/AudioStroop/toneright350msec.wav">\n\
            <positional value="false"/>\n\
            <directional value="false"/>\n\
            <loop>false</loop>\n\
            <volume>0.5</volume>\n\
            <pitch>1.0</pitch>\n\
        </sound>\n\
        <sound id="left2" key="Sounds/AudioStroop/consecutiveleft.wav">\n\
            <positional value="false"/>\n\
            <directional value="false"/>\n\
            <loop>false</loop>\n\
            <volume>0.5</volume>\n\
            <pitch>1.0</pitch>\n\
        </sound>\n\
        <sound id="right2" key="Sounds/AudioStroop/consecutiveright.wav">\n\
            <positional value="false"/>\n\
            <directional value="false"/>\n\
            <loop>false</loop>\n\
            <volume>0.5</volume>\n\
            <pitch>1.0</pitch>\n\
        </sound>\n\
    </sounds>\n'

modelsOpenTag = '    <models>\n'

grass = '        <model id="grass" key="Scenes/land_plain_50x5/land_plain.scene" ref="">\n\
            <mass>0</mass>\n\
            <visible>true</visible>\n\
            <collisionShape>meshShape</collisionShape>\n\
            <scale>\n\
                <vector jtype="java_lang_Float" size="3">\n\
                    <entry>1.0</entry>\n\
                    <entry>1.0</entry>\n\
                    <entry>1.0</entry>\n\
                </vector>\n\
            </scale>\n\
            <rotation quaternion="false">\n\
                <vector jtype="java_lang_Float" size="3">\n\
                    <entry>0.0</entry>\n\
                    <entry>0.0</entry>\n\
                    <entry>0.0</entry>\n\
                </vector>\n\
            </rotation>\n\
            <translation>\n\
                <vector jtype="java_lang_Float" size="3">\n\
                    <entry>0.0</entry>\n\
                    <entry>0.0</entry>\n\
                    <entry>0.0</entry>\n\
                </vector>\n\
            </translation>\n\
        </model>\n'

car = '        <model id="Ferrari" key="Models/Cars/drivingCars/Ferrari/Car.scene" ref="">\n\
            <mass>800</mass>\n\
            <visible>true</visible>\n\
            <collisionShape>meshShape</collisionShape>\n\
            <scale>\n\
                <vector jtype="java_lang_Float" size="3">\n\
                    <entry>1.0</entry>\n\
                    <entry>1.0</entry>\n\
                    <entry>1.0</entry>\n\
                </vector>\n\
            </scale>\n\
            <rotation quaternion="false">\n\
                <vector jtype="java_lang_Float" size="3">\n\
                    <entry>0.0</entry>\n\
                    <entry>0.0</entry>\n\
                    <entry>0.0</entry>\n\
                </vector>\n\
            </rotation>\n\
            <translation>\n\
                <vector jtype="java_lang_Float" size="3">\n\
                    <entry>0.0</entry>\n\
                    <entry>0.0</entry>\n\
                    <entry>24500.0</entry>\n\
                </vector>\n\
            </translation>\n\
        </model>\n'

modelsCloseTag = '    </models>\n'

geometries = '    <geometries>\n\
        <point id="idealPoint1">\n\
            <translation>\n\
                <vector jtype="java_lang_Float" size="3">\n\
                    <entry>0.0</entry>\n\
                    <entry>0.0</entry>\n\
                    <entry>24400.0</entry>\n\
                </vector>\n\
            </translation>\n\
        </point>\n\
        <point id="idealPoint2">\n\
            <translation>\n\
                <vector jtype="java_lang_Float" size="3">\n\
                    <entry>0.0</entry>\n\
                    <entry>0.0</entry>\n\
                    <entry>20250.0</entry>\n\
                </vector>\n\
            </translation>\n\
        </point>\n\
    </geometries>\n'

resetPoints = '    <resetPoints>\n\
        <resetPoint id="reset1">\n\
            <translation>\n\
                <vector jtype="java_lang_Float" size="3">\n\
                    <entry>0</entry>\n\
                    <entry>0</entry>\n\
                    <entry>4995</entry>\n\
                </vector>\n\
            </translation>\n\
            <rotation quaternion="false">\n\
                <vector jtype="java_lang_Float" size="3">\n\
                    <entry>0</entry>\n\
                    <entry>0</entry>\n\
                    <entry>0</entry>\n\
                </vector>\n\
            </rotation>\n\
        </resetPoint>\n\
    </resetPoints>\n'

gravity = '    <gravity>9.81</gravity>\n'

lights = '    <lights>\n\
        <directionalLight>\n\
            <direction>\n\
                <vector jtype="java_lang_Float" size="3">\n\
                    <entry>0.5</entry>\n\
                    <entry>-0.5</entry>\n\
                    <entry>0.5</entry>\n\
                </vector>\n\
            </direction>\n\
            <color>\n\
                <vector jtype="java_lang_Float" size="4">\n\
                    <entry>0.7</entry>\n\
                    <entry>0.7</entry>\n\
                    <entry>0.7</entry>\n\
                    <entry>0.7</entry>\n\
                </vector>\n\
            </color>\n\
        </directionalLight>\n\
        <directionalLight>\n\
            <direction>\n\
                <vector jtype="java_lang_Float" size="3">\n\
                    <entry>-0.5</entry>\n\
                    <entry>-0.5</entry>\n\
                    <entry>0.5</entry>\n\
                </vector>\n\
            </direction>\n\
            <color>\n\
                <vector jtype="java_lang_Float" size="4">\n\
                    <entry>0.7</entry>\n\
                    <entry>0.7</entry>\n\
                    <entry>0.7</entry>\n\
                    <entry>0.7</entry>\n\
                </vector>\n\
            </color>\n\
        </directionalLight>\n\
        <directionalLight>\n\
            <direction>\n\
                <vector jtype="java_lang_Float" size="3">\n\
                    <entry>0.5</entry>\n\
                    <entry>-0.5</entry>\n\
                    <entry>-0.5</entry>\n\
                </vector>\n\
            </direction>\n\
            <color>\n\
                <vector jtype="java_lang_Float" size="4">\n\
                    <entry>0.7</entry>\n\
                    <entry>0.7</entry>\n\
                    <entry>0.7</entry>\n\
                    <entry>0.7</entry>\n\
                </vector>\n\
            </color>\n\
        </directionalLight>\n\
        <directionalLight>\n\
            <direction>\n\
                <vector jtype="java_lang_Float" size="3">\n\
                    <entry>-0.5</entry>\n\
                    <entry>-0.5</entry>\n\
                    <entry>-0.5</entry>\n\
                </vector>\n\
            </direction>\n\
            <color>\n\
                <vector jtype="java_lang_Float" size="4">\n\
                    <entry>0.7</entry>\n\
                    <entry>0.7</entry>\n\
                    <entry>0.7</entry>\n\
                    <entry>0.7</entry>\n\
                </vector>\n\
            </color>\n\
        </directionalLight>\n\
    </lights>\n'

skyTexture = '    <skyTexture>Textures/Sky/Bright/hills.dds</skyTexture>\n'

epilogue = '</scene>'

# Begin console action
version = raw_input("Version number? ")

print("Remember to rename the file to scene.xml or change the file name in AudioStroop.xml before using.")

if version != "":
    filename = "scene-" + version + ".xml"
else:
    filename = "scene.xml"

fd = open(filename, "w")

fd.write(prologue)
fd.write(sounds)
fd.write(modelsOpenTag)
fd.write(grass)
fd.write(car)

makeRoad(fd, -24990.0, 24990.0)
startObjects(fd, 24250.0)
endObjects(fd, 21400.0)

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
    makeBridgeSigns(fd, i, place, sign0, sign1, sign2)

fd.write(modelsCloseTag)
fd.write(geometries)
fd.write(resetPoints)
fd.write(gravity)
fd.write(lights)
fd.write(skyTexture)
fd.write(epilogue)

fd.close()
#!/usr/bin/env python

prologue = '<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n' + \
'<scene xmlns="http://opends.eu/drivingtask/scene" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"' \
' xsi:schemaLocation="http://opends.eu/drivingtask/scene ../../Schema/scene.xsd">\n'

sounds = \
'\t<sounds>\n\
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
\t</sounds>\n\n'

modelsOpenTag = \
'\t<models>\n'

grass = \
'\t\t<model id="grass" key="Scenes/land_plain_50x5/land_plain.scene" ref="">\n\
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
\t\t</model>\n\n'

car = \
'\t\t<model id="Ferrari" key="Models/Cars/drivingCars/Ferrari/Car.scene" ref="">\n\
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
\t\t</model>\n\n'

modelsCloseTag = '\t</models>\n\n'

geometries = \
'\t<geometries>\n\
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
\t</geometries>\n\n'

resetPoints = \
'\t<resetPoints>\n\
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
\t</resetPoints>\n\n'

gravity = '\t<gravity>9.81</gravity>\n\n'

lights = \
'\t<lights>\n\
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
\t</lights>\n\n'

skyTexture = '\t<skyTexture>Textures/Sky/Bright/hills.dds</skyTexture>\n\n'

epilogue = '</scene>'
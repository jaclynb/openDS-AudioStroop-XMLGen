#!/usr/bin/env python

prologue = '<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n' + \
'<scene xmlns="http://opends.eu/drivingtask/scene" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"' \
' xsi:schemaLocation="http://opends.eu/drivingtask/scene ../../Schema/scene.xsd">\n'

sounds = \
'	<sounds>\n\
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
	</sounds>\n\n'

modelsOpenTag = \
'	<models>\n'

grass = \
'		<model id="grass" key="Scenes/land_plain_50x5/land_plain.scene" ref="">\n\
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
		</model>\n\n'

car = \
'		<model id="Ferrari" key="Models/Cars/drivingCars/Ferrari/Car.scene" ref="">\n\
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
		</model>\n\n'

modelsCloseTag = '	</models>\n\n'

geometries = \
'	<geometries>\n\
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
	</geometries>\n\n'

resetPoints = \
'	<resetPoints>\n\
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
	</resetPoints>\n\n'

gravity = '	<gravity>9.81</gravity>\n\n'

lights = \
'	<lights>\n\
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
	</lights>\n\n'

skyTexture = '	<skyTexture>Textures/Sky/Bright/hills.dds</skyTexture>\n\n'

epilogue = '</scene>'
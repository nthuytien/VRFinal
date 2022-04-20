import viz
import viztask
import vizact
import vizinfo
import vizproximity
import vizshape
import random


viz.setMultiSample(4)
viz.fov(60)
viz.go()

ground = viz.addChild('ground.osgb')
ground.setPosition(0,0,20)
ground = viz.addChild('ground.osgb')
ground.setPosition(0,0,40)
sky = viz.addChild('sky_day.osgb')

manager = vizproximity.Manager()
manager.setDebug(viz.ON)
debugEventHandle = vizact.onkeydown('d',manager.setDebug,viz.TOGGLE)

#Play background music
back_music = viz.addAudio('back_music.wav')
back_music.loop(viz.ON)
back_music.play()

########################Add Spheres ##############################
target = vizproximity.Target(viz.MainView)
manager.addTarget(target)
sphereSensors = []

sphere1 = vizshape.addSphere(radius=1)
sphere1.setPosition(0,1,10)
sphere2 = vizshape.addSphere(radius=1)
sphere2.setPosition(10,1,10)
sphere3 = vizshape.addSphere(radius=1)
sphere3.setPosition(0,1,25)
sphere4 = vizshape.addSphere(radius=1)
sphere4.setPosition(10,1,25)
sphere5 = vizshape.addSphere(radius=1)
sphere5.setPosition(0,1,40)
sphere6 = vizshape.addSphere(radius=1)
sphere6.setPosition(10,1,40)


sensor1 = vizproximity.addBoundingSphereSensor(sphere1,scale=1)
sensor2 = vizproximity.addBoundingSphereSensor(sphere2,scale=1)
sensor3 = vizproximity.addBoundingSphereSensor(sphere3,scale=1)
sensor4 = vizproximity.addBoundingSphereSensor(sphere4,scale=1)
sensor5 = vizproximity.addBoundingSphereSensor(sphere5,scale=1)
sensor6 = vizproximity.addBoundingSphereSensor(sphere6,scale=1)

manager.addSensor(sensor1)
manager.addSensor(sensor2)
manager.addSensor(sensor3)
manager.addSensor(sensor4)
manager.addSensor(sensor5)
manager.addSensor(sensor6)
######################################################
#Set up Logistics

correct = 0
hintpanel = vizinfo.InfoPanel(align = viz.ALIGN_RIGHT_TOP, icon=False,key=None)
hintpanel.setText("Press the key of the number of your question for a hint!")

pigeon = viz.addAvatar('pigeon.cfg')
pigeon.setPosition(4.5,0,10)

Q2Center = vizproximity.Sensor(vizproximity.CircleArea(1.5,center=(4.5,15)),None)
manager.addSensor(Q2Center)
Q3Center = vizproximity.Sensor(vizproximity.CircleArea(1.5,center=(4.5,30)),None)
manager.addSensor(Q3Center)
finalCenter = vizproximity.Sensor(vizproximity.CircleArea(1.5,center=(4.5,45)),None)
manager.addSensor(finalCenter)

#######################################################
#Set Up Avatars and Text


hintman1 = viz.addAvatar('vcc_male.cfg')
hintman2 = viz.addAvatar('vcc_male.cfg')
hintman3 = viz.addAvatar('vcc_male.cfg')
hintman1.setPosition(5,0,7)
hintman2.setPosition(4.5,0,7)
hintman3.setPosition(4,0,7)
hintman4 = viz.addAvatar('vcc_female.cfg')
hintman5 = viz.addAvatar('vcc_female.cfg')
hintman6 = viz.addAvatar('vcc_female.cfg')
hintman4.setPosition(5,0,22)
hintman5.setPosition(4.5,0,22)
hintman6.setPosition(4,0,22)
hintman7 = viz.addAvatar('vcc_male.cfg')
hintman8 = viz.addAvatar('vcc_male.cfg')
hintman9 = viz.addAvatar('vcc_male.cfg')
hintman7.setPosition(5,0,37)
hintman8.setPosition(4.5,0,37)
hintman9.setPosition(4,0,37)

number1 = random.randint(1,10)
number2 = random.randint(1,10)
correctSum = number1 + number2
incorrectSum = random.randint(2,20)

number3 = random.randint(10,20)
number4 = random.randint(1,10)
correctDifference = number3 - number4
incorrectDifference = random.randint(2,20)

number5 = random.randint(1,10)
number6 = random.randint(1,10)
correctProduct = number5 * number6
incorrectProduct = random.randint(1,100)

text1 = viz.addText3D(str(correctSum),pos=[-0.3,3,10])
text2 = viz.addText3D(str(incorrectSum),pos=[9.3,3,10])
text3 = viz.addText3D(str(incorrectDifference),pos=[-0.3,3,25])
text4 = viz.addText3D(str(correctDifference),pos=[9.3,3,25])
text5 = viz.addText3D(str(correctProduct),pos=[-0.3,3,40])
text6 = viz.addText3D(str(incorrectProduct),pos=[9.3,3,40])

duck1 = viz.addAvatar('duck.cfg')
duck2 = viz.addAvatar('duck.cfg')
duck3 = viz.addAvatar('duck.cfg')

duck1.setPosition(4,0,50)
duck2.setPosition(5,0,50)
duck3.setPosition(6,0,50)

duck1.visible(viz.OFF)
duck2.visible(viz.OFF)
duck3.visible(viz.OFF)

angle = 0
#crowd behavior
def rotateModel():
    global angle

    #Increment the angle by the rotation speed based on elapsed time
    angle = angle + (50 * viz.elapsed())

    #Update the models rotation
    duck1.setEuler([angle,0,0])
    duck2.setEuler([angle,0,0])
    duck3.setEuler([angle,0,0])

    
vizact.ontimer(0, rotateModel)

###############################################3
#Question 1


instructions = vizinfo.InfoPanel(icon=False,key=None)
instructions.setText("Question One: " + str(number1) + " + " + str(number2) + " = ")

def getHint1():
		hintman1.runAction(vizact.walkTo([1,0,9]))
		hintman2.runAction(vizact.walkTo([1,0,9]))
		hintman3.runAction(vizact.walkTo([1,0,9]))

vizact.onkeydown('1', getHint1)

def Q1(e):
	global correct
	if e.sensor == sensor1:
		#instructions.setText("Correct!")
		correct += 1
		print("correct" + str(correct))
	elif e.sensor == sensor2:
		print("incorrect")
		#instructions.setText("Incorrect!")

manager.onEnter(None,Q1)

####################################################
#Question 2


def Q2SetUp(e):
	hintpanel.visible(viz.OFF)
	if e.sensor == sensor1 or e.sensor == sensor2:
		instructions.setText("Please follow Pigeon to the next question")
		pigeon.runAction(vizact.walkTo([4.5,0,15], 5))
		

def Q2Start(e):
	if e.sensor == Q2Center:
		instructions.setText("Question Two: " + str(number3) + " - " + str(number4) + " = ")
		hintpanel.visible(viz.ON)


manager.onEnter(None,Q2SetUp)
manager.onEnter(None,Q2Start)



def getHint2():
	hintman4.runAction(vizact.walkTo([9,0,24]))
	hintman5.runAction(vizact.walkTo([9,0,24]))
	hintman6.runAction(vizact.walkTo([9,0,24]))

vizact.onkeydown('2', getHint2)
def Q2(e):
	global correct
	if e.sensor == sensor4:
		#instructions.setText("Correct!")
		correct+=1
		print("correct" + str(correct))
		
	elif e.sensor == sensor3:
		print("incorrect")
		#instructions.setText("Incorrect!")

manager.onEnter(None,Q2)

####################################################
#Question 3



def Q3SetUp(e):
	hintpanel.visible(viz.OFF)
	if e.sensor == sensor3 or e.sensor == sensor4:
		instructions.setText("Please follow Pigeon to the next question")
		pigeon.runAction(vizact.walkTo([4.5,0,30]))

		
		
def Q3Start(e):
	if e.sensor == Q3Center:
		instructions.setText("Question Three: " + str(number5) + " x " + str(number6) + " = ")
		hintpanel.visible(viz.ON)


manager.onEnter(None,Q3SetUp)
manager.onEnter(None,Q3Start)



def getHint3():
	hintman7.runAction(vizact.walkTo([1,0,39]))
	hintman8.runAction(vizact.walkTo([1,0,39]))
	hintman9.runAction(vizact.walkTo([1,0,39]))

vizact.onkeydown('3', getHint3)


def Q3(e):
	global correct
	if e.sensor == sensor5:
		#instructions.setText("Correct!")
		correct+=1
		print("correct" + str(correct))
		
	elif e.sensor == sensor6:
		print("incorrect")
		#instructions.setText("Incorrect!")

manager.onEnter(None,Q3)

###################################################

#Celebration Set Up

def CelSetUp(e):
	hintpanel.visible(viz.OFF)
	if e.sensor == sensor5 or e.sensor == sensor6:
		instructions.setText("Please follow Pigeon to the Judgement Zone")
		pigeon.runAction(vizact.walkTo([4.5,0,45]))

def celebration(e):
	if e.sensor == finalCenter:
		global correct
		print("Final is" + str(correct))
		if correct >= 3:
			duck1.visible(viz.ON)
			duck2.visible(viz.ON)
			duck3.visible(viz.ON)
			instructions.setText("Congrats! You have gotten all the questions right!")
			cheering = viz.addAudio('cheering.wav')
			back_music.play()
		else:
			instructions.setText(str(correct) + " correct. No Celebration for you :(")
			
manager.onEnter(None,CelSetUp)
manager.onEnter(None, celebration)



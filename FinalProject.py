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
sky = viz.addChild('sky_day.osgb')

manager = vizproximity.Manager()
manager.setDebug(viz.ON)
debugEventHandle = vizact.onkeydown('d',manager.setDebug,viz.TOGGLE)

########################Add Spheres ##############################3
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
#Set up

correct = 0
hintpanel = vizinfo.InfoPanel(align = viz.ALIGN_CENTER_TOP, icon=False,key=None)
hintpanel.setText("Press the 'h' key for a hint!")

pigeon = viz.addAvatar('pigeon.cfg')
pigeon.setPosition(4.5,0,10)

Q2Center = vizproximity.Sensor(vizproximity.CircleArea(1.5,center=(4.5,15)),None)
manager.addSensor(Q2Center)
#######################################################
#Question 1


instructions = vizinfo.InfoPanel(icon=False,key=None)
number1 = random.randint(1,10)
number2 = random.randint(1,10)
correctSum = number1 + number2
incorrectSum = random.randint(2,20)

instructions.setText("Question One: " + str(number1) + " + " + str(number2) + " = ")


text1 = viz.addText3D(str(correctSum),pos=[-0.3,3,10])
text2 = viz.addText3D(str(incorrectSum),pos=[9.3,3,10])

hintman1 = viz.addAvatar('vcc_male.cfg')
hintman2 = viz.addAvatar('vcc_male.cfg')
hintman3 = viz.addAvatar('vcc_male.cfg')
hintman1.setPosition(5,0,7)
hintman2.setPosition(4.5,0,7)
hintman3.setPosition(4,0,7)
def getHint1():
	hintman1.runAction(vizact.walkTo([1,0,9]))
	hintman2.runAction(vizact.walkTo([1,0,9]))
	hintman3.runAction(vizact.walkTo([1,0,9]))

vizact.onkeydown('h', getHint1)

def Q1(e):
	if e.sensor == sensor1:
		print("correct")
		instructions.setText("Correct!")
	elif e.sensor == sensor2:
		print("incorrect")
		instructions.setText("Incorrect!")

manager.onEnter(None,Q1)

####################################################
#Question 2



def Q2SetUp(e):
	hintpanel.visible(viz.OFF)
	hintman1.remove()
	hintman2.remove()
	hintman3.remove()
	if e.sensor == sensor1 or e.sensor == sensor2:
		instructions.setText("Please follow Pigeon to the next question")
		pigeon.runAction(vizact.walkTo([4.5,0,15]))
		
number3 = random.randint(10,20)
number4 = random.randint(1,10)
correctDifference = number3 - number4
incorrectDifference = random.randint(2,20)

text3 = viz.addText3D(str(incorrectDifference),pos=[-0.3,3,25])
text4 = viz.addText3D(str(correctDifference),pos=[9.3,3,25])

hintman4 = viz.addAvatar('vcc_male.cfg')
hintman5 = viz.addAvatar('vcc_male.cfg')
hintman6 = viz.addAvatar('vcc_male.cfg')
hintman4.setPosition(5,0,22)
hintman5.setPosition(4.5,0,22)
hintman6.setPosition(4,0,22)


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

vizact.onkeydown('h', getHint1)

def Q2(e):
	if e.sensor == sensor4:
		print("correct")
		instructions.setText("Correct!")
	elif e.sensor == sensor3:
		print("incorrect")
		instructions.setText("Incorrect!")

manager.onEnter(None,Q1)







import time
import math

x = 0.6
y = -0.6
z = 1.2

row_increment = 0.6
colum_increment = 0.6
increment_pause = 2

#determine the turret angle and vane angle of the blower based on xyz coordinates of target
#return these two angles as a list, turret first, then vane angle
def calculate_angles(x, y, z):
    #constant variables
    MAX_VANE_ANGLE = 25     #next version should be 45, current should be 25
    MAX_TURRET_ANGLE = 90

    #check if y is zero so we don't get an error
    is_y_zero = False
    if y == 0:
        is_y_zero = True

    #calculate hypotenuse to use in vane calculation
    h = math.sqrt((x*x) + (y*y))
    if is_y_zero:
        turret_angle = math.pi/2     #90 degrees in radians
        if x > 0:
            turret_angle = -math.pi/2

        else:
            turret_angle = math.pi/2
    else:
        turret_angle = math.atan(x/y)

    """
    h = math.sqrt((x*x)+(y*y))
    turret_angle = math.atan(x/y)
    """
    vane_angle = math.atan(h/z)

    #convert radian measurements to degrees
    turret_angle = turret_angle * 180/math.pi
    vane_angle = vane_angle * 180/math.pi

    #if vane_angle is greater than MAX_VANE_ANGLE the vane angle needs to be the max vane angle
    #Or else something will break
    if(vane_angle > MAX_VANE_ANGLE):
        vane_angle = MAX_VANE_ANGLE

    #ditto for the turret with the wires being pulled out
    #while the vane thing is likely to happen, this is just a safeguard
    if(turret_angle > MAX_TURRET_ANGLE):
        turret_angle = MAX_TURRET_ANGLE

    #Determining signage of turret/vane angles
    #+ -> clockwise
    #- -> counter-clockwise
    """
               (x)
    -turret     | +turret
    +vanes      | -vanes
                |
    (y)---------|------------
    +turret     | -turret
    +vanes      | -vanes

    """
    if(y > 0):
        vane_angle = -vane_angle
    """
    if((y < 0 and x > 0) or (x < 0 and y > 0)):
        turret_angle = -turret_angle
    """

    return [turret_angle, vane_angle]


while x >= -0.6:
    while y <= 0.6:
        print(x, y)
        y += row_increment

        calculated_angles = calculate_angles(x, y, z)
        print("The turret angle is %f degrees" % calculated_angles[0])
        print("The vane angle is %f degrees" % calculated_angles[1])
        position = (-calculated_angles[0]/7.5)*16*18
        #stepper0.setTargetPosition(position)

        #motor starts moving
        #stepper0.setEngaged(True)
        #vanes move to angle
        #go_to_angle(calculated_angles[1])

        #wait a half second for the actuators to get to position
        time.sleep(0.5)
        #blower_on()

        #blow air for increment_pause
        time.sleep(increment_pause)

    x -= colum_increment
    y = 0.6
    if(x <= -0.6):
        break
    print("New Row <--")
    while y >= -0.6:
        print(x, y)
        y -= row_increment

        calculated_angles = calculate_angles(x, y, z)
        print("The turret angle is %f degrees" % calculated_angles[0])
        print("The vane angle is %f degrees" % calculated_angles[1])
        position = (-calculated_angles[0]/7.5)*16*18
        #stepper0.setTargetPosition(position)

        #motor starts moving
        #stepper0.setEngaged(True)
        #vanes move to angle
        #go_to_angle(calculated_angles[1])

        #wait a half second for the actuators to get to position
        time.sleep(0.5)
        #blower_on()

        #blow air for increment_pause
        time.sleep(increment_pause)
    x -= colum_increment
    y = -0.6
    print("New Row -->")

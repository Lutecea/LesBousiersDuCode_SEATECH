"""plateau1_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Motor


class BobRobot: 
    right_wheel = None
    left_wheel = None

# create the Robot instance.
robot = BobRobot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
motor1 = robot.getDevice('left wheel')
motor2 = robot.getDevice('right wheel')

motor1.setPosition(float('inf'))
motor1.setVelocity(0.0)

motor2.setPosition(float('inf'))
motor2.setVelocity(0.0)


#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()
    motor1.setVelocity(10.0)
    # Process sensor data here.
    motor2.setVelocity(-10.0)
    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    pass

# Enter here exit cleanup code.

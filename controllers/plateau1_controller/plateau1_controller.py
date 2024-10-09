"""plateau1_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Motor


class BobRobot(Robot): 
    right_wheel = None
    left_wheel = None

    def __init__(self):
        super().__init__()

        self.left_wheel:Motor = self.getDevice('left wheel')
        self.right_wheel:Motor = self.getDevice('right wheel')

        self.left_wheel:self.setPosition(float('inf'))
        self.right_wheel:self.setPosition(float('inf'))

        self.left_wheel:self.setVelocity(0.0)
        self.right_wheel:self.setVelocity(0.0)
        
    def Beyblade(self) :
        self.right_wheel.setVelocity(10.0)
        self.left_wheel.setVelocity(-10.0)

# create the Robot instance.
robot = BobRobot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:


#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()
    robot.Beyblade()
    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    pass

# Enter here exit cleanup code.

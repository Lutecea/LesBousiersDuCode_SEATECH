"""plateau2_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Motor, DistanceSensor, GPS

#================================================================
#                           Saucisse
#================================================================
class SaucisseRoomba(Robot): 

    def __init__(self):
        super().__init__()
        self.moteur = Moteurs(self)
        self.gps = Galileo(self)
        self.capteurs=Capteurs(self)

    def run(self):
        pos_cotegauche_avant = self.capteurs.get_DistanceDroite()
        pos_cotedroit_avant = self.capteurs.get_DistanceGauche()

        if pos_cotegauche_avant > 800 and pos_cotedroit_avant > 800 :
            self.moteur.avance()
        
        elif pos_cotegauche_avant > 330 and pos_cotegauche_avant > pos_cotedroit_avant: 
            self.moteur.tourne_gauche()

        elif pos_cotedroit_avant > 330 and pos_cotedroit_avant >  pos_cotegauche_avant:
            self.moteur.tourne_droite()

        else :
            self.moteur.avance()



#================================================================
#                           Moteurs
#================================================================
class Moteurs():
    right_wheel = None
    left_wheel = None

    
    def __init__(self,robot:Saucisse):
        super().__init__()

        self.left_wheel:Motor = robot.getDevice('left wheel')
        self.right_wheel:Motor = robot.getDevice('right wheel')

        self.left_wheel.setPosition(float('inf'))
        self.right_wheel.setPosition(float('inf'))

        self.left_wheel.setVelocity(0.0)
        self.right_wheel.setVelocity(0.0)
    #Getters

    #Setters

    #Fonctions
    def Beyblade(self) :
        self.right_wheel.setVelocity(10.0)
        self.left_wheel.setVelocity(-10.0)

    def avance(self):
        print("J'AVANCE LE SANG")
        self.right_wheel.setVelocity(10.0)
        self.left_wheel.setVelocity(10.0)

    def recule(self):
        print("JE RECULE LE SANG")
        self.right_wheel.setVelocity(10.0)
        self.left_wheel.setVelocity(-10.0)

    def tourne_droite(self):
        print("JE TOURNE A DROITE LE SANG")
        self.right_wheel.setVelocity(-10.0)
        self.left_wheel.setVelocity(10.0)

    def tourne_gauche(self):
        print("JE TOURNE A GAUCHE LE SANG")
        self.right_wheel.setVelocity(10.0)
        self.left_wheel.setVelocity(-2.0)

#================================================================
#                           Capteurs
#================================================================
class Capteurs():
    DistanceCaptor = None 

    def __init__(self,robot:SaucisseRoomba):
        super.__init__()
        self.DistanceCaptorDroit:DistanceSensor = robot.getDevice('distance sensor droit')
        self.DistanceCaptorDroit.enable(int(robot.getBasicTimeStep()))

        self.DistanceCaptorGauche:DistanceSensor = robot.getDevice('distance sensor gauche')
        self.DistanceCaptorGauche.enable(int(robot.getBasicTimeStep()))


    def get_DistanceDroite(self): 
        return self.DistanceCaptorDroit.getValue()  
    
    def get_DistanceGauche(self): 
        return self.DistanceCaptorGauche.getValue()  
    
#================================================================
#                           LE GPS
#================================================================
class Galileo():
    GPS = None

    def __init__(self,robot:SaucisseRoomba):
        super.__init__()
        self.gps_roomba:GPS = robot.getDevice('gps')
        self.gps_roomba.enable(int(robot.getBasicTimeStep()))

    def get_posgps(self):
        print(self.gps.getCoordinateSystem())
        return self.gps.getCoordinateSystem()


#================================================================
#                 Le main (la boucle comme tu veux)
#================================================================
# create the Robot instance.
robot = SaucisseRoomba()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getDevice('motorname')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    robot.run()
    pass

# Enter here exit cleanup code.

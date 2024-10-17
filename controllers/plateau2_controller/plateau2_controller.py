"""plateau1_controller controller."""


from controller import Robot, Motor, DistanceSensor, GPS
import time


#================================================================
#                           SolidSnake
#================================================================
class SolidSnake(Robot): 

    def __init__(self):
        super().__init__()
        self.moteur = Moteurs(self)
        #self.gps_solid = Galileo(self)
        self.capteurs=Capteurs(self)

    def run(self):
        pos_cotegauche_avant = self.capteurs.detectgauche_avant()
        pos_cotedroit_avant = self.capteurs.detectdroite_avant()
        pos_avant = self.capteurs.detectavant()

        if pos_avant > 260 : 
            self.moteur.tourne_gauche()

        if pos_cotegauche_avant > 300 and pos_cotedroit_avant > 300 :
            self.moteur.avance()
        
        elif pos_cotegauche_avant > 300 and pos_cotegauche_avant > pos_cotedroit_avant: 
            self.moteur.tourne_gauche()

        elif pos_cotedroit_avant > 300 and pos_cotedroit_avant >  pos_cotegauche_avant:
            self.moteur.tourne_droite()

        else :
            self.moteur.avance()

    
#================================================================
#                           Moteurs
#================================================================
class Moteurs():
    right_wheel = None
    left_wheel = None

    
    def __init__(self,robot:SolidSnake):

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
        #print("J'AVANCE LE SANG")
        self.right_wheel.setVelocity(10.0)
        self.left_wheel.setVelocity(10.0)

    def recule(self):
        #print("JE RECULE LE SANG")
        self.right_wheel.setVelocity(10.0)
        self.left_wheel.setVelocity(-10.0)

    def tourne_droite(self):
        #print("JE TOURNE A DROITE LE SANG")
        self.right_wheel.setVelocity(-10.0)
        self.left_wheel.setVelocity(10.0)

    def tourne_gauche(self):
        #print("JE TOURNE A GAUCHE LE SANG")
        self.right_wheel.setVelocity(10.0)
        self.left_wheel.setVelocity(-2.0)

#================================================================
#                           Capteurs
#================================================================
class Capteurs():
    so0 = None #Côté gauche avant
    so1 = None #Côté gauche avant
    so2 = None #Côté gauche avant
    so3 = None #Avant
    so4 = None #Coté droit avant
    so5 = None #Coté droit avant
    so6 = None #Coté droit avant
    so7 = None #Coté droit 
    so8 = None #Coté gauche 
    so9 = None #Coté gauche arrière
    so10 = None #Coté gauche arrière
    so11 = None #Coté gauche arrière
    so12 = None #Arriere
    so13 = None #Coté droit arrière
    so14 = None #Coté droit arrière
    so15 = None #Coté droit arrière

    
    def __init__(self,robot:SolidSnake):
        #init des capteurs, on les utilise pas tous mais flemme j'ai tout fait je les garde
        self.so0:DistanceSensor = robot.getDevice('so0')
        self.so0.enable(int(robot.getBasicTimeStep()))

        self.so1:DistanceSensor = robot.getDevice('so1')
        self.so1.enable(int(robot.getBasicTimeStep()))

        self.so2:DistanceSensor = robot.getDevice('so2')
        self.so2.enable(int(robot.getBasicTimeStep()))

        self.so3:DistanceSensor = robot.getDevice('so3')
        self.so3.enable(int(robot.getBasicTimeStep()))

        self.so4:DistanceSensor = robot.getDevice('so4')
        self.so4.enable(int(robot.getBasicTimeStep()))

        self.so5:DistanceSensor = robot.getDevice('so5')
        self.so5.enable(int(robot.getBasicTimeStep()))

        self.so6:DistanceSensor = robot.getDevice('so6')
        self.so6.enable(int(robot.getBasicTimeStep()))

        self.so7:DistanceSensor = robot.getDevice('so7')
        self.so7.enable(int(robot.getBasicTimeStep()))

        self.so8:DistanceSensor = robot.getDevice('so8')
        self.so8.enable(int(robot.getBasicTimeStep()))

        self.so9:DistanceSensor = robot.getDevice('so9')
        self.so9.enable(int(robot.getBasicTimeStep()))

        self.so10:DistanceSensor = robot.getDevice('so10')
        self.so10.enable(int(robot.getBasicTimeStep()))

        self.so11:DistanceSensor = robot.getDevice('so11')
        self.so11.enable(int(robot.getBasicTimeStep()))

        self.so12:DistanceSensor = robot.getDevice('so12')
        self.so12.enable(int(robot.getBasicTimeStep()))

        self.so13:DistanceSensor = robot.getDevice('so13')
        self.so13.enable(int(robot.getBasicTimeStep()))

        self.so14:DistanceSensor = robot.getDevice('so14')
        self.so14.enable(int(robot.getBasicTimeStep()))

        self.so15:DistanceSensor = robot.getDevice('so15')
        self.so15.enable(int(robot.getBasicTimeStep()))

        #Getters 
    def get_PositionSensorso0(self): 
        return self.so0.getValue()

    def get_PositionSensorso1(self): 
        return self.so1.getValue()
    
    def get_PositionSensorso2(self): 
        return self.so2.getValue()
    
    def get_PositionSensorso3(self): 
        return self.so3.getValue()
    
    def get_PositionSensorso4(self): 
        return self.so4.getValue()
    
    def get_PositionSensorso5(self): 
        return self.so5.getValue()
    
    def get_PositionSensorso6(self): 
        return self.so6.getValue()
    
    def get_PositionSensorso7(self): 
        return self.so7.getValue()
    
    def get_PositionSensorso8(self): 
        return self.so6.getValue()
    
    def get_PositionSensorso9(self): 
        return self.so9.getValue()
    
    def get_PositionSensorso10(self): 
        return self.so10.getValue()
    
    def get_PositionSensorso11(self): 
        return self.so11.getValue()
    
    def get_PositionSensorso12(self): 
        return self.so12.getValue()
    
    def get_PositionSensorso13(self): 
        return self.so13.getValue()
    
    def get_PositionSensorso14(self): 
        return self.so14.getValue()
    
    def get_PositionSensorso15(self): 
        return self.so15.getValue()
    
    #Fonctions

    def detectavant(self):
        valueavant = self.get_PositionSensorso3() + self.get_PositionSensorso4() / 2
        #print(f"AVANT : {valueavant}" )
        return valueavant
    
    def detectdroite_avant(self):
        val = (self.get_PositionSensorso0() +self.get_PositionSensorso1() + self.get_PositionSensorso2()) /3
        #print(f"DROITE : {val}" )
        return val
    

    def detectgauche_avant(self):
        val = (self.get_PositionSensorso7() +self.get_PositionSensorso6() + self.get_PositionSensorso5() )/3
        #print(f"GAUCHE : {val}" )
        return val

    
#================================================================
#                           LE GPS
#================================================================
class Galileo():
    GPS = None


    #Les coordonnées voulues : -43.7573 , 51.0985, -0.19

    def __init__(self,robot:SolidSnake):
        self.gps_solid:GPS = robot.getDevice('gps')
        self.gps_solid.enable(int(robot.getBasicTimeStep()))

    def get_posgps(self):
        print(self.gps.getCoordinateSystem())
        return self.gps.getCoordinateSystem()


#================================================================
#                 Le main (la boucle comme tu veux)
#================================================================
# create the Robot instance.
robot = SolidSnake()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

#C'est la boucle la vraie
while robot.step(timestep) != -1:
    robot.run()
    pass


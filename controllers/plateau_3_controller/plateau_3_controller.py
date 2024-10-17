

from controller import Robot, Motor, Gyro, GPS


class Robot3(Robot):

    def __init__(self):

        super().__init__()


        # Récupération des dispositifs des rotors

        self.m1_motor: Motor = self.getDevice('m1_motor')
        self.m2_motor: Motor = self.getDevice('m2_motor')
        self.m3_motor: Motor = self.getDevice('m3_motor')
        self.m4_motor: Motor = self.getDevice('m4_motor')


        # Activer les moteurs en position infinie

        self.m1_motor.setPosition(float('inf'))
        self.m2_motor.setPosition(float('inf'))
        self.m3_motor.setPosition(float('inf'))
        self.m4_motor.setPosition(float('inf'))


        # Vitesse de base des rotors
        self.base_speed = 55.5


        # Récupération du gyroscope
        self.gyro: Gyro = self.getDevice('gyro')
        self.gyro.enable(int(self.getBasicTimeStep()))


        # Récupération des coordonnées GPS
        self.gps: GPS = self.getDevice('gps')
        self.gps.enable(int(self.getBasicTimeStep()))

        # Gestion des phases
        self.movement_phase = "x" # Changeant
        self.phase_duration_z = 1000 # En ms
        self.phase_duration_x = 100
        self.phase_duration_y = 100
        self.phase_timer = 0 # Timer de phase en cours

        # Points de passage
        self.waypoints = [

            [-50.0, 60.0, 10.0],
            [-61.0, 72.0, 5.0],
 
        ]

        self.checked_waypoints = []  # Points de passage déjà atteints
        self.current_target = self.waypoints[0]  # Premier point de passage
        self.position_tolerance = 0.2  # Tolérance de position


        # Variables pour l'atterrissage
        self.landing = False


    def get_current_position(self):

        # Récupération de la position GPS actuelle
        current_position = self.gps.getValues()
        #print(f"Position actuelle récupérée: {current_position}")  
        return current_position


    def distance_to_point(self, point):

        # Calcul de la distance entre la position actuelle et un point
        current_position = self.get_current_position()
        distance = ((current_position[0] - point[0]) ** 2 +
                    (current_position[1] - point[1]) ** 2 +
                    (current_position[2] - point[2]) ** 2) ** 0.5
        print(f"Distance calculée entre {current_position} et {point} : {distance}")  
        return distance


    def choose_next_point(self):

        # Choix du prochain point de passage si le point actuel est atteint
        if self.current_target and self.distance_to_point(self.current_target) < self.position_tolerance:

            #print(f"Point de passage atteint: {self.current_target}")  # Debug
            self.checked_waypoints.append(self.current_target)
            remaining_waypoints = [p for p in self.waypoints if p not in self.checked_waypoints]

            if remaining_waypoints:
                self.current_target = remaining_waypoints[0]
                #print(f"Nouveau point de passage sélectionné: {self.current_target}")  # Debug

            else:

                self.current_target = None
                self.landing = True  # Déclencher l'atterrissage

        else:

            #print(f"Le point de passage actuel est {self.current_target}")  # Debug


    def move_to_target(self):
        current_position = self.get_current_position()
        self.phase_timer += int(self.getBasicTimeStep())

        if self.movement_phase == "z":
            # Déplacement en z
            if abs(current_position[2] - self.current_target[2]) > self.position_tolerance:
                
                if current_position[2] < self.current_target[2]:

                    # Déplacement vers le haut
                    #print("Déplacement vers le haut")  # Debug
                    self.m1_motor.setVelocity(-55.99)
                    self.m2_motor.setVelocity(55.99)
                    self.m3_motor.setVelocity(-55.99)
                    self.m4_motor.setVelocity(55.99)

                else:

                    # Déplacement vers le bas
                    #print("Déplacement vers le bas")  # Debug
                    self.m1_motor.setVelocity(-55.0001)
                    self.m2_motor.setVelocity(55.0001)
                    self.m3_motor.setVelocity(-55.0001)
                    self.m4_motor.setVelocity(55.0001)
            
            if self.phase_timer >= self.phase_duration_z:
                self.movement_phase="y" # Passage à la phase y
                self.phase_imer = 0
                #print("Passage à la phase y")

        elif self.movement_phase == "y":
            # Déplacement en y
            if abs(current_position[0] - self.current_target[0]) > self.position_tolerance:

                if current_position[0] < self.current_target[0]:

                    # Déplacement vers la droite
                    #print("Déplacement vers la droite") 
                    self.m4_motor.setVelocity(55.102)
                    self.m2_motor.setVelocity(55.101)
                    self.m3_motor.setVelocity(-55.102)
                    self.m1_motor.setVelocity(-55.101)

                else:
                    #print("Déplacement vers la gauche")
                    self.m4_motor.setVelocity(55.101)
                    self.m2_motor.setVelocity(55.102)
                    self.m3_motor.setVelocity(-55.101)
                    self.m1_motor.setVelocity(-55.102)
            
            if self.phase_timer >= self.phase_duration_x:
                self.movement_phase="x" # Passage à la phase x
                self.phase_timer = 0
                #print("Passage à la phase x")

        elif self.movement_phase == "x":
            # Déplacement en x
            if abs(current_position[1] - self.current_target[1]) > self.position_tolerance:
                if current_position[1] < self.current_target[1]:

                    # Déplacement vers l'avant
                    #print("Déplacement vers l'avant") 
                    self.m2_motor.setVelocity(55.102)
                    self.m4_motor.setVelocity(55.101)
                    self.m1_motor.setVelocity(-55.101)
                    self.m3_motor.setVelocity(-55.102)

                    # Déplacement vers l'arrière
                else: 
                    #print("Déplacent vers l'arrière")
                    self.m2_motor.setVelocity(55.101)
                    self.m4_motor.setVelocity(55.102)
                    self.m1_motor.setVelocity(-55.102)
                    self.m3_motor.setVelocity(-55.101)

            if self.phase_timer >= self.phase_duration_y:
                self.movement_phase="z" # Passage à la phase y
                self.phase_timer = 0
                #print("Passage à la phase z")

        


    def land_drone(self):

        # Atterrissage en douceur
        if self.base_speed > 55.0:
            self.base_speed -= 0.1

        else:

            self.base_speed = 55.0
            #print("Le drone a atterri")
        self.m1_motor.setVelocity(-self.base_speed)
        self.m2_motor.setVelocity(self.base_speed)
        self.m3_motor.setVelocity(-self.base_speed)
        self.m4_motor.setVelocity(self.base_speed)


    def run(self):
        # Exécute le plan de vol tant que le drone n'est pas en train d'atterrir

        if not self.landing:

            #print("Le drone est en vol")  # Debug
            self.choose_next_point()  # Choisir le prochain point si le drone est proche du précédent
            self.move_to_target()  # Se déplacer vers le point choisi

        else:

            #print("Le drone est en train d'atterrir")  # Debug
            self.land_drone()



# Création du robot et du timestep
robot = Robot3()
timestep = int(robot.getBasicTimeStep())


# Boucle principale

while robot.step(timestep) != -1:
    robot.run()

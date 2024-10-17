

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
        self.base_speed = 56.0


        # Récupération du gyroscope
        self.gyro: Gyro = self.getDevice('gyro')
        self.gyro.enable(int(self.getBasicTimeStep()))


        # Récupération des coordonnées GPS
        self.gps: GPS = self.getDevice('gps')
        self.gps.enable(int(self.getBasicTimeStep()))


        # Points de passage
        self.waypoints = [

            [1.0, -5.0, 10.0],
            [1.0, 2.0, 9.0],
            [6.0, 8.0, 4.0],
            [4.0, 3.0, 4.0],
            [5.0, 1.0, 9.0],
            [10.0, 9.0, 2.0]
        ]

        self.checked_waypoints = []  # Points de passage déjà atteints
        self.current_target = self.waypoints[0]  # Premier point de passage
        self.position_tolerance = 0.3  # Tolérance de position


        # Variables pour l'atterrissage
        self.landing = False


    def get_current_position(self):

        # Récupération de la position GPS actuelle
        current_position = self.gps.getValues()
        print(f"Position actuelle récupérée: {current_position}")  
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

            print(f"Point de passage atteint: {self.current_target}")  # Debug
            self.checked_waypoints.append(self.current_target)
            remaining_waypoints = [p for p in self.waypoints if p not in self.checked_waypoints]

            if remaining_waypoints:
                self.current_target = remaining_waypoints[0]
                print(f"Nouveau point de passage sélectionné: {self.current_target}")  # Debug

            else:

                self.current_target = None
                self.landing = True  # Déclencher l'atterrissage

        else:

            print(f"Le point de passage actuel est {self.current_target}")  # Debug


    def move_to_target(self):

        if self.current_target:
            current_position = self.get_current_position()


            # Déplacement en x

            if abs(current_position[0] - self.current_target[0]) > self.position_tolerance:

                if current_position[0] < self.current_target[0]:

                    # Déplacement vers la droite

                    print("Déplacement vers la droite (x)")  # Debug

                    self.m4_motor.setVelocity(55.5)
                    self.m2_motor.setVelocity(55.0)
                    self.m3_motor.setVelocity(-55.0)
                    self.m1_motor.setVelocity(-55.5)

                elif current_position[0] == self.current_target[0]:
                    self.m4_motor.setVelocity(55.5)
                    self.m2_motor.setVelocity(55.0)
                    self.m3_motor.setVelocity(-55.0)
                    self.m1_motor.setVelocity(-55.5)


            # Déplacement en y

            if abs(current_position[1] - self.current_target[1]) > self.position_tolerance:

                if current_position[1] < self.current_target[1]:

                    # Déplacement vers l'avant
                    print("Déplacement vers l'avant (y)") 
                    self.m2_motor.setVelocity(55.5)
                    self.m4_motor.setVelocity(55.0)
                    self.m1_motor.setVelocity(-55.0)
                    self.m3_motor.setVelocity(-55.5)

                    # Déplacement vers l'arrière
                elif current_position[1] == self.current_target[1]:
                    self.m2_motor.setVelocity(55.5)
                    self.m4_motor.setVelocity(55.0)
                    self.m1_motor.setVelocity(-55.0)
                    self.m3_motor.setVelocity(-55.5)


            # Déplacement en z

            if abs(current_position[2] - self.current_target[2]) > self.position_tolerance:

                if current_position[2] < self.current_target[2]:

                    # Déplacement vers le haut
                    print("Déplacement vers le haut (z)")  # Debug
                    self.m1_motor.setVelocity(-55.5)
                    self.m2_motor.setVelocity(55.5)
                    self.m3_motor.setVelocity(-55.5)
                    self.m4_motor.setVelocity(55.5)

                    # Stabilisation à la même altitude
                elif current_position[2] == self.current_target[2]:
                    print("Altitude du waypoint atteinte")
                    self.m1_motor.setVelocity(-55.0)
                    self.m2_motor.setVelocity(55.0)
                    self.m3_motor.setVelocity(-55.0)
                    self.m4_motor.setVelocity(55.0)

                else:

                    # Déplacement vers le bas
                    print("Déplacement vers le bas (z)")  # Debug
                    self.m1_motor.setVelocity(-55.0)
                    self.m2_motor.setVelocity(55.0)
                    self.m3_motor.setVelocity(-55.0)
                    self.m4_motor.setVelocity(55.0)

            else:

                # Arrêt des moteurs en z
                self.m1_motor.setVelocity(-55.0)
                self.m2_motor.setVelocity(55.0)
                self.m3_motor.setVelocity(-55.0)
                self.m4_motor.setVelocity(55.0)


    def land_drone(self):

        # Atterrissage en douceur
        if self.base_speed > 55.0:
            self.base_speed -= 0.1

        else:

            self.base_speed = 55.0
            print("Le drone a atterri")
        self.m1_motor.setVelocity(-self.base_speed)
        self.m2_motor.setVelocity(self.base_speed)
        self.m3_motor.setVelocity(-self.base_speed)
        self.m4_motor.setVelocity(self.base_speed)


    def run(self):
        # Exécute le plan de vol tant que le drone n'est pas en train d'atterrir

        if not self.landing:

            print("Le drone est en vol")  # Debug
            self.choose_next_point()  # Choisir le prochain point si le drone est proche du précédent
            self.move_to_target()  # Se déplacer vers le point choisi

        else:

            print("Le drone est en train d'atterrir")  # Debug
            self.land_drone()



# Création du robot et du timestep
robot = Robot3()
timestep = int(robot.getBasicTimeStep())


# Boucle principale

while robot.step(timestep) != -1:
    robot.run()

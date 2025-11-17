class Map(): # Definierar en klass för labyrinten
    def __init__(self, goal_x, goal_y, traps, treasures):
        self.goal_x = goal_x  # Målets X-koordinat
        self.goal_y = goal_y  # Målets Y-koordinat
        self.traps = traps  # Lista över koordinater för fällor
        self.treasures = treasures  # Lista över koordinater för skatter

class Player():  # Definierar en klass för spelaren
    def __init__(self, name, map_parameter):
        self.name = name  # Spelarens namn
        self.map = map_parameter
        self.x = 0  # Startposition X-koordinat
        self.y = 0  # Startposition Y-koordinat
        self.score = 0  # Startpoäng
        

    def move(self, direction):
        # Flytta spelaren baserat på riktningen
        if direction == "up":
            self.y += 1  # Öka Y-koordinaten för att flytta uppåt
        elif direction == "down":
            self.y -= 1  # Minska Y-koordinaten för att flytta nedåt
        elif direction == "left":
            self.x -= 1  # Minska X-koordinaten för att flytta åt vänster
        elif direction == "right":
            self.x += 1  # Öka X-koordinaten för att flytta åt höger
        self.check_position()  # Kontrollera spelarens nya position

    def check_position(self):
        # Kontrollera om spelaren har träffat en skatt eller fälla
        if (self.x, self.y) in self.map.treasures:
            self.score += 10  # Öka poängen
            self.map.treasures.remove((self.x, self.y))  # Ta bort skatten från listan
            print(f"{self.name} found a treasure! Score: {self.score}")
        elif (self.x, self.y) in self.map.traps:
            self.score -= 5  # Minska poängen för träffad fälla
            print(f"{self.name} hit a trap! Score: {self.score}")

        # Kontrollera om målet är nått
        if (self.x, self.y) == (self.map.goal_x, self.map.goal_y):
            print(f"{self.name} reached the goal! Final Score: {self.score}")


#######################################################
# Skapa en labyrint och en spelare utanför klassdefinitionerna
traps = [(2, 1), (1, 2)]  # Definiera FÄLLORNAS positioner (x,y),tupler 
treasures = [(1, 1), (2, 2)]  # Definiera skatternas positioner
maze_object = Map(3, 3, traps, treasures)  # Skapa en labyrintinstans
player = Player("Pierre", maze_object)  # Skapa en spelarinstans

# Spellogik för att flytta spelaren
player.move("right")  # Spelaren rör sig åt höger
player.move("up")  # Spelaren rör sig uppåt
player.move("right")  # Spelaren rör sig åt höger igen
player.move("right")  # Spelaren rör sig åt höger ännu en gång
player.move("up")  # Spelaren rör sig uppåt
player.move("up")  # Spelaren rör sig uppåt

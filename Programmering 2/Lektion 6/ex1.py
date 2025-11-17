""" Ni ska skapa ett spel där två spelare utforskar en karta för att hitta en gömd skatt. 
Spelarna ska kunna röra sig i olika riktningar på kartan och försöka lokalisera skatten genom sina rörelser. """

class Map():
    def __init__(self, x_max, y_max, treasure_x, treasure_y):
         # attribut = parameter
        self.x_max = x_max  # Maximal x-koordinat på kartan. kartans bredd
        self.y_max = y_max  # Maximal y-koordinat på kartan. kartans höjd
        self.treasure_x = treasure_x  # x-koordinat för skatten
        self.treasure_y = treasure_y  # y-koordinat för skatten

class Player():
    def __init__(self, name, map):
        self.name = name  # Spelarens namn
        self.map = map  # Referens till kartan. 
        self.x = 0  # Spelarens Startposition x
        self.y = 0  # Spelarens Startposition y
        
         
    def move_up(self):
        # Gå upp, om spelaren inte redan är högst upp
        if self.y < self.map.y_max:
            self.y += 1
        
    def move_down(self):
        # Gå ner, om spelaren inte redan är längst ner
        if self.y > 0:
            self.y -= 1
            
    def move_right(self):
        # Gå höger, om spelaren inte redan är längst till höger
        if self.x < self.map.x_max:
            self.x += 1
        
    def move_left(self):
        # Gå vänster, om spelaren inte redan är längst till vänster
        if self.x > 0:
            self.x -= 1
            
    def pick_treasure(self):
        # Kontrollera om spelaren har hittat skatten
        # Om spelarens x-koordinat är samma som skattens x-koordinat, och spelarens y-koordinat är samma som skattens y-koordinat 
        if self.x == self.map.treasure_x and self.y == self.map.treasure_y:
            print(self.name, "hittade skatten!")
        else:
            print(self.name, "kunde inte hitta skatten")
            
####################################################### # Outside Class, utanför klassen
# Skapa en karta och två spelare utanför klassdefinitionerna
map_object = Map(5, 4, 2, 1) # (x_max, y_max, treasure_x, treasure_y)         
player_1 = Player('Isaak', map_object) # Vi har map_object som input till spelaren, så att spelaren vet vilken karta den är på.
player_2 = Player('Maria', map_object)

# Flytta spelarna och skriv ut deras positioner
player_1.move_up()
player_2.move_up()
print(player_1.name, ":", player_1.x, ", ", player_1.y, ", ", player_2.name, ":", player_2.x, ", ",player_2.y)

player_1.pick_treasure()
player_2.pick_treasure()

player_1.move_up()
player_2.move_right()
print(player_1.name, ":", player_1.x, ", ", player_1.y, ", ", player_2.name, ":", player_2.x, ", ",player_2.y)

player_1.pick_treasure()
player_2.pick_treasure()

player_1.move_up()
player_2.move_right()
print(player_1.name, ":", player_1.x, ", ", player_1.y, ", ", player_2.name, ":", player_2.x, ", ",player_2.y)

# Låt spelarna försöka plocka upp skatten
player_1.pick_treasure()
player_2.pick_treasure()



    
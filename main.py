# Datei: main.py

import pygame
import sys

import modul
from tilemap import tilemap

# Pygame initialisieren
pygame.init()

# Bildschirmgröße einstellen
screen = pygame.display.set_mode((600, 660))
pygame.display.set_caption("Pacman")

# Tile-Größe
TILE_SIZE = 20

# Tile-Bilder laden
tiles = {
    0    : pygame.image.load('images/schwarz.jpg'),
    10000: pygame.image.load('images/blau.jpg'),
    10001: pygame.image.load('images/horizontal.jpg'),
    10010: pygame.image.load('images/vertikal.jpg'),
    10011: pygame.image.load('images/vertikal.jpg'),
    10100: pygame.image.load('images/horizontal.jpg'),
    10101: pygame.image.load('images/04.jpg'),
    10110: pygame.image.load('images/03.jpg'),
    10111: pygame.image.load('images/34.jpg'),
    11000: pygame.image.load('images/horizontal.jpg'),
    11001: pygame.image.load('images/01.jpg'),
    11010: pygame.image.load('images/02.jpg'),
    11011: pygame.image.load('images/12.jpg'),
    11100: pygame.image.load('images/horizontal.jpg'),
    11101: pygame.image.load('images/41.jpg'),
    11110: pygame.image.load('images/23.jpg'),
    11111: pygame.image.load('images/kreuz.jpg')
}

# Klasse für bewegliche Objekte anlegen
class bewObj:
    def __init__(self, x, y, spalte, zeile, posX, posY, richtung, richtungswunsch, speed, image, wegpunkteListe, wegpunktNummer):
        self.x = x
        self.y = y
        self.spalte = spalte # die Tiles der Tilema
        self.zeile = zeile
        self.posX = posX
        self.posY = posY
        self.richtung = richtung
        self.richtungswunsch = richtungswunsch
        self.speed = speed
        self.image = image
        self.wegpunkteListe = wegpunkteListe
        self.wegpunktNummer = wegpunktNummer

wegpunkteListe1 = [(330,250), (330,190), (390,190), (390,130), (450,130), (450,50)]
Kreis1 = [(550,50), (550,190), (450,190), (450,50)]

pacman = bewObj(50, 50, 3, 3, 10, 10, "bewegungslos", "nicht definiert", 1, pygame.image.load('images/pac0.jpg'), None, None)
geist1 = bewObj(300, 250, None, None, 10, 10, "bewegungslos", "nicht definiert", 1, pygame.image.load('images/rot1.jpg'), wegpunkteListe1, 0)

bewObjListe = [pacman, geist1]

# Hauptschleife
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Pacman Steuerung durch Pfeiltasten    
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                pacman.richtungswunsch = "rechts"
            elif event.key == pygame.K_LEFT:
                pacman.richtungswunsch = "links"
            elif event.key == pygame.K_DOWN:
                pacman.richtungswunsch = "runter"
            elif event.key == pygame.K_UP:
                pacman.richtungswunsch = "hoch"

    # Steuerung Pacman
    if pacman.richtungswunsch == "rechts":
        if tilemap[pacman.zeile][pacman.spalte+1] == 0:
            if pacman.posY >= 10-pacman.speed and pacman.posY <= 10+pacman.speed:
                pacman.y = pacman.y - pacman.posY + 10
                pacman.richtung = "rechts"
    if pacman.richtungswunsch == "links":
        if tilemap[pacman.zeile][pacman.spalte-1] == 0:
            if pacman.posY >= 10-pacman.speed and pacman.posY <= 10+pacman.speed:
                pacman.y = pacman.y - pacman.posY + 10
                pacman.richtung = "links"
    if pacman.richtungswunsch == "runter":
        if tilemap[pacman.zeile+1][pacman.spalte] == 0:
            if pacman.posX >= 10-pacman.speed and pacman.posX <= 10+pacman.speed:
                pacman.x = pacman.x - pacman.posX + 10
                pacman.richtung = "runter"
    if pacman.richtungswunsch == "hoch":
        if tilemap[pacman.zeile-1][pacman.spalte] == 0:
            if pacman.posX >= 10-pacman.speed and pacman.posX <= 10+pacman.speed:
                pacman.x = pacman.x - pacman.posX + 10
                pacman.richtung = "hoch"

    # Schleife für Objekte der Klasse bewObj
    for objekt in bewObjListe:
        # Werte zur Berechnung der Position eines beweglichen Objekts innerhalb des aktuellen Tiles
        objekt.spalte = objekt.x // 20
        objekt.zeile = objekt.y // 20
        objekt.posX = objekt.x - objekt.spalte*20
        objekt.posY = objekt.y - objekt.zeile*20

        # Bewegungsrichtung (vorerst nur für Pacman)
        if objekt.richtung == "rechts":
            if tilemap[objekt.zeile][objekt.spalte+1] == 0:
                objekt.x += objekt.speed
            elif tilemap[objekt.zeile][objekt.spalte+1] == 1:
                if objekt.posX < 10-objekt.speed:
                    objekt.x += objekt.speed
                elif objekt.posX >= 10-objekt.speed:
                    objekt.x = objekt.x - objekt.posX + 10
                    objekt.richtung = "bewegungslos"
        if objekt.richtung == "links":
            if tilemap[objekt.zeile][objekt.spalte-1] == 0:
                objekt.x -= objekt.speed
            elif tilemap[objekt.zeile][objekt.spalte-1] == 1:
                if objekt.posX > 10+objekt.speed:
                    objekt.x -= objekt.speed
                elif objekt.posX <= 10+objekt.speed:
                    objekt.x = objekt.x - objekt.posX + 10
                    objekt.richtung = "bewegungslos"
        if objekt.richtung == "runter":
            if tilemap[objekt.zeile+1][objekt.spalte] == 0:
                objekt.y += objekt.speed
            elif tilemap[objekt.zeile+1][objekt.spalte] == 1:
                if objekt.posY < 10+objekt.speed:
                    objekt.y += objekt.speed
                elif objekt.posY >= 10+objekt.speed:
                    objekt.y = objekt.y - objekt.posY + 10
                    objekt.richtung = "bewegungslos"
        if objekt.richtung == "hoch":
            if tilemap[objekt.zeile-1][objekt.spalte] == 0:
                objekt.y -= objekt.speed
            elif tilemap[objekt.zeile-1][objekt.spalte] == 1:
                if objekt.posY > 10+objekt.speed:
                    objekt.y -= objekt.speed
                elif objekt.posY <= 10+objekt.speed:
                    objekt.y = objekt.y - objekt.posY + 10
                    objekt.richtung = "bewegungslos"

    # geister bewegen
    for geist in range(1, 2):
        aktuelleNummer = bewObjListe[geist].wegpunktNummer

        # wenn möglich, im Kreis
        if Kreis1[0][1] <= bewObjListe[geist].y < Kreis1[1][1] and bewObjListe[geist].x == Kreis1[0][0]:
            bewObjListe[geist].y += 1
        elif Kreis1[1][0] <= bewObjListe[geist].x < Kreis1[2][0] and bewObjListe[geist].y == Kreis1[1][1]:
            bewObjListe[geist].x += 1
        elif Kreis1[2][1] <= bewObjListe[geist].y < Kreis1[3][1] and bewObjListe[geist].x == Kreis1[2][0]:
            bewObjListe[geist].y += 1
        elif Kreis1[3][0] <= bewObjListe[geist].x < Kreis1[0][0] and bewObjListe[geist].y == Kreis1[3][1]:
            bewObjListe[geist].x += 1        

        # sonst zum Kreis hin
        elif bewObjListe[geist].x != Kreis1[3][0] and bewObjListe[geist].y != Kreis1[3][1] and bewObjListe[geist].x < bewObjListe[geist].wegpunkteListe[aktuelleNummer][0]:
            bewObjListe[geist].x += 1
        elif bewObjListe[geist].x > bewObjListe[geist].wegpunkteListe[aktuelleNummer][0]:
            bewObjListe[geist].x -= 1
        elif bewObjListe[geist].y < bewObjListe[geist].wegpunkteListe[aktuelleNummer][1]:
            bewObjListe[geist].y += 1
        elif bewObjListe[geist].y > bewObjListe[geist].wegpunkteListe[aktuelleNummer][1]:
            bewObjListe [geist].y -= 1

        # wenn wegpunkt erreicht ist, setze nächsten wegpunkt als Ziel
        elif bewObjListe[geist].x == bewObjListe[geist].wegpunkteListe[aktuelleNummer][0] and bewObjListe[geist].y == bewObjListe[geist].wegpunkteListe[aktuelleNummer][1]:
            bewObjListe[geist].wegpunktNummer += 1
    
    # Bildschirm mit schwarzer Farbe füllen
    screen.fill((0, 0, 0))

#   erstelle die Welt im Fenster
    for zeile in range(1, len(tilemap)-1):
        innerzeile = tilemap[zeile]
        for spalte in range(1, len(innerzeile)-1):

            # zur Ermittlung von tile_type muss die Bitmaske erstmal erstellt werden
            tile_type = modul.erstelleBitmaske(tilemap, zeile, spalte)
            screen.blit(tiles[tile_type], (spalte * TILE_SIZE, zeile * TILE_SIZE))    

    # image-figuren zeichnen
    screen.blit(pacman.image, (pacman.x-10, pacman.y-10))
    screen.blit(geist1.image, (geist1.x-10, geist1.y-10))

    # Bildschirm aktualisieren
    pygame.display.flip()

    # Frame-Rate einstellen
    pygame.time.Clock().tick(60)

# Pygame beenden
pygame.quit()

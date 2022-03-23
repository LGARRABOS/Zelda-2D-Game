import pygame
import time
import random as rd


#                  : PROGRAMME VARIABLE / DEFINITION :
#                  : PERSONNAGE :

#Le personnage posséde une image pour chaque action qu'il effectue.

imglinkh = pygame.image.load('linkhaut.png')
imglinkb = pygame.image.load('linkbas.png')
imglinkg = pygame.image.load('linkgauche.png')
imglinkd = pygame.image.load('linkdroite.png')
imglinkhe = pygame.image.load('linkhautepee.png')
imglinkbe = pygame.image.load('linkbasepee.png')
imglinkge = pygame.image.load('linkgaucheepee.png')
imglinkde = pygame.image.load('linkdroiteepee.png')
imglinkad = pygame.image.load('link_arc_droite.png')
imglinkag = pygame.image.load('link_arc_gauche.png')
def perso (x,y,image):
    surface.blit(image, (x,y))

#                  : ENNEMIS :

img_ennemi = pygame.image.load('ennemi1.png')

def ennemi1 (x,y,image):
    surface.blit(image, (x,y))

#                  : OBJET :

#On charge toute les images des "objet" et ont leurs attribut un "x" et un "y"

img_coeur1 = pygame.image.load('spritecoeur1.png')
img_rubis = pygame.image.load('rubis.png')
img_coffre = pygame.image.load('coffre.png')
img_cle = pygame.image.load('cle.png')
img_arc = pygame.image.load('arc.png')
img_arc_inventaire = pygame.image.load('arcinventaire.png')
img_fleched =pygame.image.load('fleche_droite.png')
img_flecheg =pygame.image.load('fleche_gauche.png')
img_flecheb =pygame.image.load('fleche_bas.png')
img_flecheh =pygame.image.load('fleche_haut.png')
def coeur_1 (x,y,image):
    surface.blit(image, (x,y))
def coeur_2 (x,y,image):
    surface.blit(image, (x,y))
def coeur_3(x,y,image):
    surface.blit(image, (x,y))
def rubis (x,y,image):
    surface.blit(image, (x,y))
def coffre (x,y,image):
    surface.blit(image, (x,y))
def cle (x,y,image):
    surface.blit(image, (x,y))
def arc (x,y,image):
    surface.blit(image, (x,y))
def fleche (x,y,image):
    surface.blit(image, (x,y))
def Usine_de_murs(rectangle):
    le_mur = {'rect': rectangle,'vitesse':(0,0)}


#                  : PARTICULE :

img_particule1 = pygame.image.load('particule1.png')
img_particule2 = pygame.image.load('particule2.png')
img_particule3 = pygame.image.load('particule3.png')

#                  : TERRAIN :

#Ajout de toute les map
img_A0 = pygame.image.load('A0.png') ; img_B0 = pygame.image.load('B0.png') ; img_C0 = pygame.image.load('C0.png')
img_A1 = pygame.image.load('A1.png') ; img_B1 = pygame.image.load('B1.png') ; img_C1 = pygame.image.load('C1.png')
img_A2 = pygame.image.load('A2.png') ; img_B2 = pygame.image.load('B2.png') ; img_C2 = pygame.image.load('C2.png')
img_A3 = pygame.image.load('A3.png') ; img_B3 = pygame.image.load('B3.png')
def La_Carte (x,y,image):
    surface.blit(image, (x,y))


"""-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-"""
pygame.init()
"""-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-"""


#                  : INTERFACE :

surface_Largeur = 26*32
surface_Hauteur = 22*32
surface = pygame.display.set_mode((surface_Largeur,surface_Hauteur))
pygame.display.set_caption("Le jeu")

#                  : TEXTE :
couleur_Blanc = (255,255,255)
couleur_Rouge = (255,0,0)
couleur_Gris = (100,100,100)
police_arial = pygame.font.SysFont('arial',30)
police_impact = pygame.font.SysFont('impact',70)

#                   : MUSIQUE PRINCIPAL :

musique = pygame.mixer.Sound("foret.wav")
musique.play()

#                    : MUSIQUE SECONDAIRE :

epee = pygame.mixer.Sound("epee.wav")
monstre = pygame.mixer.Sound("monstre.wav")
monstre.play() #Je lance le son du monstre dés le début car il est spawn au meme endroit que le joueur



#                : LANCEMENT DU PROGRAMME / BOUCLE PRINCIPALE :


    #   VARIABLES :
        # joueur
x_joueur = 18*32
y_joueur = 12*32

        # Map
Carte_x = Carte_y = 0
A0=A2=A3=B0=B1=B2=B3=C0=C1=C2=False
A1 = True
La_Carte(Carte_x,Carte_y,img_A1)
Téléportation = "Possible"

        #Coeur
c1=750 ; c2=700 ; c3=650 ; Coeur=3

x_Ennemi = rd.randint(1,7)*2*32
y_Ennemi = rd.randint(1,5)*2*32

Rubis_Score = 0
x_rubis = 500
y_rubis = 0
x_cle = y_cle = -1000
x_coffre = y_coffre = -1000
random_e = rd.randint(0,100)
x_arc = y_arc = 4444
x_fleche = y_fleche = 4460


game_over = False
gauche = droite = haut = False
bas = True
ennemi_mort = False
cle_ramasser = False
Cle = Coffre = True
arc_ramasser = False
fleche_lancé_vers_droite = False
fleche_lancé_vers_gauche = False
STOP = False

while not game_over :

        # VARIABLES :
    keys = pygame.key.get_pressed()
    mouvement = 16
    if keys[pygame.K_KP1]:
        pygame.time.delay(500)
        print("1")
    if keys[pygame.K_m]:
        print("")

        # VITESSE DU JEU :
    pygame.time.delay(50)

        # CONDITION FERMER LE JEU :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    if keys[pygame.K_ESCAPE]:
        break
        """______"""
    if STOP == False :
            """______"""
            # INTERFACE / TERRAIN :
                # Caractéristique de chauqe carte
            if A0 == True:
                La_Carte(Carte_x,Carte_y,img_A0)
                x_Ennemi = -1000
                y_Ennemi = -1000
            if A1 == True:
                La_Carte(Carte_x,Carte_y,img_A1)
                ennemi_mort = False
                x_coffre = y_coffre = -1000
                if cle_ramasser == False:
                    x_cle = y_cle = -1000
            if A2 == True:
                La_Carte(Carte_x,Carte_y,img_A2)
                if Cle == True:
                    x_cle = y_cle = 192
                x_Ennemi = -1000
                y_Ennemi = -1000
            if A3 == True:
                La_Carte(Carte_x,Carte_y,img_A3)
                if cle_ramasser == False:
                    x_cle = y_cle = -1000
            if B0 == True:
                La_Carte(Carte_x,Carte_y,img_B0)
                x_coffre = y_coffre = -1000
            if B1 == True:
                La_Carte(Carte_x,Carte_y,img_B1)
                if Coffre == True:
                    x_coffre = y_coffre = 352
                x_Ennemi = -1000
                y_Ennemi = -1000
            if B2 == True:
                La_Carte(Carte_x,Carte_y,img_B2)
                x_coffre = y_coffre = -1000
                if cle_ramasser == False:
                    x_cle = y_cle = -1000
            if C1 == True:
                La_Carte(Carte_x,Carte_y,img_C1)
                x_coffre = y_coffre = -1000
            if C2 == True:
                La_Carte(Carte_x,Carte_y,img_C2)


            # _________________________________________________MAP____________________________________________________________
            droite_sortie = x_joueur > surface_Largeur-64
            gauche_sortie = x_joueur < 0
            haut_sortie = y_joueur < 0
            bas_sortie = y_joueur > surface_Hauteur-64
            """---------------------------------------------------FULL BUG------------------------"""
            def All(): #Permets de tous stoper pour facilement changer de carte
                monstre.stop()
                A1=A2=A3=B1=B2=B3=False
                Téléportation = "Impossible"
                x_cle = y_cle = -1000
                x_coffre = y_coffre = -1000
                print("tout a été effacé")
            """---------------------------------------------------FULL BUG------------------------"""

            # on prend l'information que le joueur veut sortir de l'écran
            if Téléportation == "Possible":
                if droite_sortie or gauche_sortie or bas_sortie or haut_sortie:
                    """Pour les A"""
                    if Téléportation == "Possible":
                        if A0 == True :
                            if gauche_sortie :
                                A0=A1=A2=A3=B0=B1=B2=B3=C0=C1=C2=False
                                All() ; A1 = True # On change la carte et ses attributs
                                x_joueur = 16
                                x_Ennemi = rd.randint(1,7)*2*32
                                y_Ennemi = rd.randint(1,5)*2*32
                                monstre.play()
                            Téléportation = "Impossible"
                    if Téléportation == "Possible":
                        if A1 == True : # Si il est dans la case A1
                            if gauche_sortie :
                                A0=A1=A2=A3=B0=B1=B2=B3=C0=C1=C2=False
                                All() ; A0 = True # On change la carte et ses attributs
                                x_joueur = 16
                            if droite_sortie :
                                A0=A1=A2=A3=B0=B1=B2=B3=C0=C1=C2=False
                                All() ; B1 = True # On change la carte et ses attributs
                                x_joueur = 0
                            if bas_sortie :
                                A0=A1=A2=A3=B0=B1=B2=B3=C0=C1=C2=False
                                y_joueur = 0
                                All() ; A2 = True
                            Téléportation = "Impossible"
                    if Téléportation == "Possible":
                        if A2 == True : # Si il est dans la case A2
                            if droite_sortie :
                                A0=A1=A2=A3=B0=B1=B2=B3=C0=C1=C2=False
                                All() ; B2 = True
                                x_joueur = 0
                            if bas_sortie :
                                A0=A1=A2=A3=B0=B1=B2=B3=C0=C1=C2=False
                                All() ; A3 = True
                                y_joueur = 0
                            if haut_sortie :
                                A0=A1=A2=A3=B0=B1=B2=B3=C0=C1=C2=False
                                All() ; A1 = True
                                x_Ennemi = rd.randint(1,7)*2*32
                                y_Ennemi = rd.randint(1,5)*2*32
                                monstre.play()
                                y_joueur = surface_Hauteur-64
                            Téléportation = "Impossible"
                    if Téléportation == "Possible":
                        if A3 == True : # Si il est dans la case A3
                            if droite_sortie :
                                A0=A1=A2=A3=B0=B1=B2=B3=C0=C1=C2=False
                                All() ; B3 = True
                                x_joueur = 0
                            if haut_sortie :
                                A0=A1=A2=A3=B0=B1=B2=B3=C0=C1=C2=False
                                All() ; A2 = True
                                y_joueur = surface_Hauteur-64
                            Téléportation = "Impossible"

                    """Pour les B"""
                    if Téléportation == "Possible":
                        if B0 == True :
                            if bas_sortie :
                                A0=A1=A2=A3=B0=B1=B2=B3=C0=C1=C2=False
                                All() ; B1 = True
                                y_joueur = 0
                            Téléportation = "Impossible"
                    if Téléportation == "Possible":
                        if B1 == True : # Si il est dans la case A1
                            if gauche_sortie :
                                A0=A1=A2=A3=B0=B1=B2=B3=C0=C1=C2=False
                                All() ; A1 = True # On change la carte et ses attributs
                                x_joueur = surface_Largeur-64
                                x_Ennemi = rd.randint(1,7)*2*32
                                y_Ennemi = rd.randint(1,5)*2*32
                                monstre.play()
                            if droite_sortie :
                                A0=A1=A2=A3=B0=B1=B2=B3=C0=C1=C2=False
                                All() ; C1 = True
                                x_joueur = 0
                            if bas_sortie :
                                A0=A1=A2=A3=B0=B1=B2=B3=C0=C1=C2=False
                                All() ; B2 = True
                                y_joueur = 0
                            if haut_sortie :
                                A0=A1=A2=A3=B0=B1=B2=B3=C0=C1=C2=False
                                All() ; B0 = True
                                y_joueur = surface_Hauteur-64
                            Téléportation = "Impossible"
                    if Téléportation == "Possible":
                        if B2 == True : # Si il est dans la case A2
                            if gauche_sortie :
                                A0=A1=A2=A3=B0=B1=B2=B3=C0=C1=C2=False
                                All() ; A2 = True
                                x_joueur = surface_Largeur-64
                            if droite_sortie :
                                A0=A1=A2=A3=B0=B1=B2=B3=C0=C1=C2=False
                                All() ; C2 = True
                                x_joueur = 0
                            if haut_sortie :
                                A0=A1=A2=A3=B1=B2=B3=False
                                All() ; B1 = True
                                y_joueur = surface_Hauteur-64
                            Téléportation = "Impossible"
                    if Téléportation == "Possible":
                        if B3 == True : # Si il est dans la case A3
                            if gauche_sortie :
                                A0=A1=A2=A3=B0=B1=B2=B3=C0=C1=C2=False
                                All() ; A3 = True
                                x_joueur = surface_Largeur-64
                            Téléportation = "Impossible"

                    """Pour les C"""
                    if Téléportation == "Possible":
                        if C1 == True :
                            if gauche_sortie == True :
                                A0=A1=A2=A3=B0=B1=B2=B3=C0=C1=C2=False
                                All() ; B1 = True
                                x_joueur = surface_Largeur-64
                                Téléportation = "Impossible"
                            if bas_sortie == True :
                                A0=A1=A2=A3=B0=B1=B2=B3=C0=C1=C2=False
                                All() ; C2 = True
                                y_joueur = 0
                                Téléportation = "Impossible"
                        if C2 == True :
                            if gauche_sortie == True :
                                A0=A1=A2=A3=B0=B1=B2=B3=C0=C1=C2=False
                                All() ; B2 = True
                                x_joueur = surface_Largeur-64
                                Téléportation = "Impossible"
                            if haut_sortie == True :
                                A0=A1=A2=A3=B0=B1=B2=B3=C0=C1=C2=False
                                All() ; C1 = True
                                y_joueur = surface_Hauteur-64
                                Téléportation = "Impossible"

                    x_fleche = -2000
                    y_fleche = -2000
                Téléportation = "Possible"

            # _________________________________________________MAP____________________________________________________________

            # _________________________________________________JOUEUR__________________________________________________________
            # MOUVEMENT / DIRECTION / COMMANDE DU JOUEUR :

            if keys[pygame.K_LEFT]:
                x_joueur -= mouvement
                gauche = True ; droite = haut = bas = False
            if keys[pygame.K_RIGHT]:
                x_joueur += mouvement
                droite = True ; gauche = haut = bas = False
            if keys[pygame.K_UP]:
                y_joueur -= mouvement
                haut = True ; gauche = droite =  bas = False
            if keys[pygame.K_DOWN]:
                y_joueur += mouvement
                bas = True ; gauche = droite = haut = False

            if gauche == True:
                perso(x_joueur,y_joueur,imglinkg)
            if droite == True:
                perso(x_joueur,y_joueur,imglinkd)
            if haut == True:
                perso(x_joueur,y_joueur,imglinkh)
            if bas == True:
                perso(x_joueur,y_joueur,imglinkb)

            #   COMMANDE / ATTAQUE
            collision_Ennemi = pygame.Rect(x_Ennemi,y_Ennemi,64,64)
            collision_Joueur_Epee_Droite = pygame.Rect(x_joueur,y_joueur+32,128,32)
            collision_Joueur_Epee_Gauche = pygame.Rect(x_joueur-64,y_joueur+32,64,32)
            collision_Joueur_Epee_Haut = pygame.Rect(x_joueur,y_joueur-64,32,16)
            collision_Joueur_Epee_Bas = pygame.Rect(x_joueur+32,y_joueur,32,128)
            def Attaque_Réussie():
                epee.play()
                ennemi1(x_Ennemi,y_Ennemi,img_particule1)
                pygame.time.delay(70)
                ennemi1(x_Ennemi,y_Ennemi,img_particule2)

            if keys[pygame.K_q]:
                pygame.time.delay(70)
                if droite == True:
                    perso(x_joueur,y_joueur,imglinkde)
                    if collision_Joueur_Epee_Droite.colliderect(collision_Ennemi)==1:
                        Attaque_Réussie() ; ennemi_mort = True ; Rubis_Score += 1
                if gauche == True:
                    perso(x_joueur-64,y_joueur,imglinkge)
                    if  collision_Joueur_Epee_Gauche.colliderect(collision_Ennemi)==1:
                        Attaque_Réussie() ; ennemi_mort = True ; Rubis_Score += 1
                if haut == True:
                    perso(x_joueur,y_joueur-64,imglinkhe)
                    if collision_Joueur_Epee_Haut.colliderect(collision_Ennemi)==1:
                        Attaque_Réussie() ; ennemi_mort = True ; Rubis_Score += 1
                if bas == True:
                    perso(x_joueur,y_joueur,imglinkbe)
                    if collision_Joueur_Epee_Bas.colliderect(collision_Ennemi)==1:
                        Attaque_Réussie() ; ennemi_mort = True ; Rubis_Score += 1


            """____________________ Arc / Flèche ____________________"""

            if keys[pygame.K_e] and arc_ramasser == True:
               pygame.time.delay(70)
               fleche_lancé_vers_droite = False
               fleche_lancé_vers_gauche = False
               if droite == True:
                   perso(x_joueur,y_joueur,imglinkad)
                   x_fleche = x_joueur + 30
                   y_fleche = y_joueur + 34
                   fleche_lancé_vers_droite = True
               if gauche == True:
                   perso(x_joueur,y_joueur,imglinkag)
                   x_fleche = x_joueur
                   y_fleche = y_joueur + 34
                   fleche_lancé_vers_gauche = True
               if bas == True:
                   print("arc en bas")
               if haut == True:
                   print("arc en haut")

            vitesse_fleche = 20
            if fleche_lancé_vers_droite == True :
                x_fleche += vitesse_fleche
                fleche(x_fleche,y_fleche,img_fleched)
            if fleche_lancé_vers_gauche == True :
                x_fleche -= vitesse_fleche
                fleche(x_fleche,y_fleche,img_flecheg)

            collision_Fleche = pygame.Rect(x_fleche,y_fleche,32,16)
            if collision_Fleche.colliderect(collision_Ennemi)==1:
                x_fleche = -2000
                y_fleche = -2000
                Attaque_Réussie()
                Rubis_Score += 1
                ennemi_mort = True
            """____________________ Arc / Flèche ____________________"""

            # _________________________________________________JOUEUR__________________________________________________________

            #   CLE
            #Récupération d'un objet

            collision_Joueur = pygame.Rect(x_joueur,y_joueur,64,64)
            collision_Cle = pygame.Rect(x_cle,y_cle,64,64)
            if collision_Cle.colliderect(collision_Joueur)==1:
                print("cle ramasser")
                x_cle = y_cle = 0
                cle_ramasser = True ; Cle = False
            cle(x_cle, y_cle, img_cle)

            #   COFFRE
            #Ouverture d'un coffre

            collision_Coffre = pygame.Rect(x_coffre,y_coffre,64,64)
            if collision_Coffre.colliderect(collision_Joueur)==1 and cle_ramasser==True:
                print("coffre ouvert")
                x_coffre = y_coffre = x_cle = y_cle = -4200
                x_arc = y_arc = 352
                Coffre = False
            coffre(x_coffre, y_coffre, img_coffre)

            #Récupération d'un arc

            collision_Arc = pygame.Rect(x_arc,y_arc,64,64)
            if collision_Arc.colliderect(collision_Joueur)==1:
                print("arc ramasser")
                arc_ramasser = True
                x_arc = 384
                y_arc = 8
            if arc_ramasser == True:
                arc(x_arc,y_arc,img_arc_inventaire)
            if arc_ramasser == False:
                arc(x_arc, y_arc, img_arc)

            # ENNEMI

            if ennemi_mort == True :
                x_Ennemi = y_Ennemi = -1000
                monstre.stop()
            if ennemi_mort == False :
                ennemi1(x_Ennemi,y_Ennemi,img_ennemi)

            # COLLISION / Ennemi attaque

            collision_Joueur = pygame.Rect(x_joueur,y_joueur,64,64)
            if collision_Joueur.colliderect(collision_Ennemi)==1:
                if droite == True :
                    x_joueur -= 48
                if gauche == True :
                    x_joueur += 48
                if bas == True :
                    y_joueur -= 48
                if haut == True :
                    y_joueur += 48
                Coeur -= 1

            # COEUR

            coeur_1(c1, 0, img_coeur1)
            coeur_2(c2, 0, img_coeur1)
            coeur_3(c3, 0, img_coeur1)
            if Coeur == 2:
                c3=-4000
            if Coeur == 1:
                c2=-4000


            #Rubis
            rubis(x_rubis, y_rubis, img_rubis)
            """______Toutes les Hit-box____"""
            # hitbox en A1            x, y,taille x, taille y
            """mur_surf = pygame.Surface((64,64))
            mur_surf.fill(couleur_Rouge)
            mur = Usine_de_murs(pygame.Rect(64*2,64*4,64,64))
            surface.blit(mur_surf, [64*2,64*4])"""

            col_A1_num_1 = pygame.Rect(0,64,64,64)#coin
            col_A1_num_2 = pygame.Rect(64,64,6*64,32)
            col_A1_num_3 = pygame.Rect(7*64,64,64,64)#coin
            col_A1_num_4 = pygame.Rect(0,2*64,64,32)
            col_A1_num_5 = pygame.Rect(7*64,2*64,2*64,32)
            col_A1_num_6 = pygame.Rect(9*64,2*64,64,64)#coin
            col_A1_num_7 = pygame.Rect(4*64,3*64,64,32)
            col_A1_num_8= pygame.Rect(9*64,3*64,2*64,32)
            col_A1_num_9 = pygame.Rect(11*64,3*64,64,64)#coin
            col_A1_num_10 = pygame.Rect(11*64,4*64,2*64,32)
            col_A1_num_11 = pygame.Rect(2*64,5*64,64,2*48)
            col_A1_num_12 = pygame.Rect(6*64,7*64,64,32)
            col_A1_num_13 = pygame.Rect(64,8*64,64,32)
            col_A1_num_14 = pygame.Rect(10*64,9*64,64,32)
            # hitbox en A2
            col_A2_num_1 = pygame.Rect(0,0,64,64)#coin
            col_A2_num_2 = pygame.Rect(64*2,64*4,64,64)
            col_A2_num_3 = pygame.Rect(64*11,64*5,64,64)#coin
            col_A2_num_4 = pygame.Rect(64*12,64*5,64,64)
            col_A2_num_5 = pygame.Rect(64*11,64*6,64,64)
            col_A2_num_6 = pygame.Rect(64*10,64*7,64,64)
            col_A2_num_7 = pygame.Rect(64*11,64*7,64,64)#coin
            col_A2_num_8 = pygame.Rect(64*11,64*5,64*2,64*2)
            """col_A2_num_9 = pygame.Rect(
            col_A2_num_10 = pygame.Rect(
            col_A2_num_11 = pygame.Rect(
            col_A2_num_12 = pygame.Rect(
            col_A2_num_13 = pygame.Rect("""


            # il est conseillé de réduire les "if"
            if A1 == True:
                if gauche == True :
                    if collision_Joueur.colliderect(col_A1_num_4)==1:
                        x_joueur += 16
                    if collision_Joueur.colliderect(col_A1_num_7)==1:
                        x_joueur += 16
                    if collision_Joueur.colliderect(col_A1_num_10)==1:
                        x_joueur += 16
                    if collision_Joueur.colliderect(col_A1_num_11)==1:
                        x_joueur += 16
                    if collision_Joueur.colliderect(col_A1_num_12)==1:
                        x_joueur += 16
                    if collision_Joueur.colliderect(col_A1_num_13)==1:
                        x_joueur += 16
                    if collision_Joueur.colliderect(col_A1_num_14)==1:
                        x_joueur += 16
                if droite == True :
                    if collision_Joueur.colliderect(col_A1_num_5)==1:
                        x_joueur -= 16
                    if collision_Joueur.colliderect(col_A1_num_7)==1:
                        x_joueur -= 16
                    if collision_Joueur.colliderect(col_A1_num_8)==1:
                        x_joueur -= 16
                    if collision_Joueur.colliderect(col_A1_num_10)==1:
                        x_joueur -= 16
                    if collision_Joueur.colliderect(col_A1_num_11)==1:
                        x_joueur -= 16
                    if collision_Joueur.colliderect(col_A1_num_12)==1:
                        x_joueur -= 16
                    if collision_Joueur.colliderect(col_A1_num_13)==1:
                        x_joueur -= 16
                    if collision_Joueur.colliderect(col_A1_num_14)==1:
                        x_joueur -= 16
                if haut == True :
                    if collision_Joueur.colliderect(col_A1_num_2)==1:
                        y_joueur += 16
                    if collision_Joueur.colliderect(col_A1_num_4)==1:
                        y_joueur += 16
                    if collision_Joueur.colliderect(col_A1_num_5)==1:
                        y_joueur += 16
                    if collision_Joueur.colliderect(col_A1_num_7)==1:
                        y_joueur += 16
                    if collision_Joueur.colliderect(col_A1_num_8)==1:
                        y_joueur += 16
                    if collision_Joueur.colliderect(col_A1_num_10)==1:
                        y_joueur += 16
                    if collision_Joueur.colliderect(col_A1_num_11)==1:
                        y_joueur += 16
                    if collision_Joueur.colliderect(col_A1_num_12)==1:
                        y_joueur += 16
                    if collision_Joueur.colliderect(col_A1_num_13)==1:
                        y_joueur += 16
                    if collision_Joueur.colliderect(col_A1_num_14)==1:
                        y_joueur += 16
                if bas == True :
                    if collision_Joueur.colliderect(col_A1_num_7)==1:
                        y_joueur -= 16
                    if collision_Joueur.colliderect(col_A1_num_11)==1:
                        y_joueur -= 16
                    if collision_Joueur.colliderect(col_A1_num_12)==1:
                        y_joueur -= 16
                    if collision_Joueur.colliderect(col_A1_num_13)==1:
                        y_joueur -= 16
                    if collision_Joueur.colliderect(col_A1_num_14)==1:
                        y_joueur -= 16
                # les coins
                if collision_Joueur.colliderect(col_A1_num_1)==1:
                        y_joueur += 16
                        x_joueur += 16
                if collision_Joueur.colliderect(col_A1_num_3)==1:
                        y_joueur += 16
                        x_joueur -= 16
                if collision_Joueur.colliderect(col_A1_num_6)==1:
                        y_joueur += 16
                        x_joueur -= 16
                if collision_Joueur.colliderect(col_A1_num_9)==1:
                        y_joueur += 16
                        x_joueur -= 16
            """if A2 == True:
                if collision_Joueur.colliderect(col_A2_num_2)==1:
                    if gauche == True:
                        x_joueur = 64*3
                    if droite == True:
                        x_joueur = 64*2
                    if haut == True:
                        y_joueur = 64*5
                    if bas == True:
                        y_joueur = 64*4


                if gauche == True:
                    if collision_Joueur.colliderect(col_A2_num_2)==1:
                        x_joueur = 64*3
                if droite == True:
                    if collision_Joueur.colliderect(col_A2_num_2)==1:
                        x_joueur = 64*2
                if haut == True:
                    if collision_Joueur.colliderect(col_A2_num_2)==1:
                        y_joueur = 64*4
                if bas == True:
                    if collision_Joueur.colliderect(col_A2_num_2)==1:
                        y_joueur = 64*5"""








    """______Tous les textes_______"""
    Les_Rubis = police_arial.render(str(Rubis_Score),False,couleur_Blanc)
    surface.blit(Les_Rubis,[532,8])
    if Coeur <= 0:
            surface.fill(couleur_Gris)
            Game_Over = police_impact.render("Game Over",True,couleur_Rouge)
            surface.blit(Game_Over,[270,300])
            musique.stop()
            monstre.stop()
            STOP = True


    """______Tous les textes_______"""

    pygame.display.update()


pygame.quit()
quit()

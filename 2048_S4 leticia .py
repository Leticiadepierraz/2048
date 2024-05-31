"""
Auteur: Leticia Dépierraz
Date: 26.01.2024
Description: reproduction du 2048 de a à z

"""

############
# Import
############

from tkinter import *
import random
import copy
import tkinter.messagebox

############
# Constante
############

score = 0
check_gagner = 0
check_perdu = 0
numbers_move = 0
choice = 0

############
# Fonction
############



def center_window():
    """
    Permets de centrer la fenetre
    :return: la fenetre centré
    """
    # calcul la taille de l'écrant
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    # comande pour centre
    center_x = int(screen_width / 2 - root_width / 2)
    center_y = int(screen_height / 2 - root_height / 2)
    # création de la fenetre
    root.geometry(f"{root_width}x{root_height}+{center_x}+{center_y}")


def quitter():
    """
    :return: quitter le programme
    """
    quit()

def display():
    """
    Insertion des chiffres et de la couleur
    :return: Le tableau remplit de couleur
    """
    global numbers,fg,label_text
    for line in range(len(numbers)):
        for col in range(len(numbers[line])):
            fg = "white"
            if numbers[line][col] <= 32:
                fg = "black"
            # création sans palcement
            # Remplace le texte par '' si la valeur est zéro
            if (numbers[line][col] == 0):
                label_text = ''
            else:
                label_text=numbers[line][col]
            labels[line][col].config(text=label_text, fg=fg, bg=colors[numbers[line][col]])


# Liste permettant de faire apparaitre des 2 ou des 4 dans le jeu.
random_list = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 4]


def spawn_tuile():
    for i in range(1):
        #random.randit sa renvoie un nombre dans la range de 0;3 dans la page séléctionné
        x = random.randint(0, 3)
        y = random.randint(0, 3)
        while numbers[x][y] != 0:
            x = random.randint(0, 3)
            y = random.randint(0, 3)
        #choisi un nombre au hasard dans la liste donné
        numbers[x][y] = random.choice(random_list)

    display()

def tasse_4(a, b, c, d):
    global score, numbers_move
    #supprimer 0 de c
    if c == 0 and d > 0:
        c = d
        d = 0
        numbers_move += 1

    #supprimer le 0 de b
    if b == 0 and c > 0:
        b = c
        c = d
        d = 0
        numbers_move += 1
    #supprimer le 0 de A
    if a == 0 and b > 0:
        a = b
        b = c
        c = d
        d = 0
        numbers_move += 1

    # calcule si les chiffres sont de la meme valeur
    #multiplier a et b
    if a == b:
        a = a * 2
        b = c
        c = d
        d = 0
        score += int(a)
        numbers_move += 1
    #multiplier b et c
    if b == c:
        b = b * 2
        c = d
        d = 0
        score += int(b)
        numbers_move += 1
    #multiplier c et d
    if c == d:
        c = c * 2
        d = 0
        score += int(c)
        numbers_move += 1


    return [a,b,c,d]

def touche_presse(event):
    global score, check_gagner, check_perdu, numbers_move,choice
    touche = event.keysym
    save = copy.deepcopy(numbers)

    #touche pour pack à gauche dans la fenetre
    if touche == ("Left" ) or touche == ("a"):
        for line in range(len(numbers)):
            [numbers[line][0], numbers[line][1], numbers[line][2], numbers[line][3]] = tasse_4(numbers[line][0], numbers[line][1], numbers[line][2], numbers[line][3])

    display()

    #touche pour aller à droite dans la fenetre
    if touche == ("Right") or touche == ("d"):
        for line in range(len(numbers)):
            [numbers[line][3], numbers[line][2], numbers[line][1], numbers[line][0]] = tasse_4(numbers[line][3], numbers[line][2], numbers[line][1], numbers[line][0])

    display()

    # touche pour aller en haut dans la fenetre
    if touche == ("Up") or touche == ("w"):
        for col in range(len(numbers)):
            [numbers[0][col], numbers[1][col], numbers[2][col], numbers[3][col]] = tasse_4(numbers[0][col], numbers[1][col], numbers[2][col], numbers[3][col])

    display()

    # touche pour aller en BAS dans la fenetre
    if touche == ("Down") or touche == ("s"):
        for col in range(len(numbers)):
            [numbers[3][col], numbers[2][col], numbers[1][col], numbers[0][col]] = tasse_4(numbers[3][col], numbers[2][col], numbers[1][col], numbers[0][col])

    display()

    #fonction pour afficher que on a gagner
    if check_gagner == 0 :
        for line in range(len(numbers)):
            for col in range(len(numbers[line])):
                if numbers[line][col] == 2048:
                    tkinter.messagebox.showinfo(title="Victoire", message=f"Vous avez obtenu un 2048 avec un score de {score}")
                    check_gagner = 1
    lbl_score.config(text=f"Score: {score}")
    display()

    #pour sauvgarder le nombre pour savoir si ils doit remettre un nombre ou pas
    if save != numbers:
        spawn_tuile()

    #fonction pour savoir si on a perdu
    if lose(numbers):
        display()
        choice = tkinter.messagebox.askyesnocancel(title="perdu", message="Vous avez perdu, voulez vous recommencer ?" 
                                                                          " Appuiez sur annuler pour quitter le programme.")

        #if choice sert à avoir la fontion pour les 3 boutons
        if choice :
            restart()
        elif choice == None:
            quit()

    return numbers


def restart():
        global numbers, score, lbl_score
        # reset tout à 0 et spawn des tuiles à l'àlatoir à chaque fois que on appuie sur le bouton
        for line in range(len(numbers)):
            for col in range(len(numbers[line])):
                numbers[line][col] = 0

        for i in range(2):
            # random.randit sa renvoie un nombre dasn la range de 0;3 dans la page séléctionné
            x = random.randint(0, 3)
            y = random.randint(0, 3)
            while numbers[x][y] != 0:
                x = random.randint(0, 3)
                y = random.randint(0, 3)
            # choisi un nombre au hasard dans la liste donné
            numbers[x][y] = random.choice(random_list)

        display()
        score = 0
        lbl_score.config(text=f"Score: {score}")

def remplis(numbers):
    """
    :param numbers:
    :return: si le tableau est plein ou pas
    """
    plein = True
    for col in range(4):
        for line in range(4):
            if numbers[col][line] == 0:
                plein = False
    return plein

def lose(numbers):
    """
    Vérifie si le joueur a perdu en ne pouvant pas effectuer de mouvement supplémentaire.

    :param: sert a controler toutes les lignes du jeu
    :return: True si le joueur a perdu, False sinon.
    """

    # Vérifie d'abord si la grille est remplie
    if remplis(numbers):


        # vérifie chaque ligne
        for line in range(len(numbers)):
            if numbers[line][0] == numbers[line][1] or numbers[line][1] == numbers[line][2] or numbers[line][2] == \
            numbers[line][3]:
                return False

        #  vérifie chaque colonnes
        for col in range(len(numbers)):
            if numbers[0][col] == numbers[1][col] or numbers[1][col] == numbers[2][col] or numbers[2][col] == numbers[3][col]:
                return False

        return True

    else:
        # Si la grille n'est pas remplie, le joueur n'a pas encore perdu
        return False


############
# Variable
############

root = Tk()

root_width = 650
root_height = 880

############
# Programe
############

# Changer la couleur de fond de la fenêtre en bleu très clair
root.configure(bg="#D8FFDB")

# centrer la fenetre
center_window()

# donne un nom à la fenetre
root.title("2048")
root.resizable(height=False, width=False)

# ------- Frame ------- #

#frame pour placer l'en tête
frame_top = Frame(root,bg="#D8FFDB")
frame_top.pack()

#frame pour placer au centre
frame_tableau = Frame(root, bg="#C7FFED", padx=20, pady=20, borderwidth=2, relief="solid")
frame_tableau.pack()

#frame pour le bas
frame_bot = Frame(root, bg="#D8FFDB")
frame_bot.pack(fill=X, expand=TRUE)

# ------- Label ------- #

#label pour afficher 2048
lbl_2048 = Label(frame_top, text="2048", font=("comic sans ms", 70), bg="#D8FFDB")
lbl_2048.grid()

#label pour afficher le score
lbl_score = Label(frame_top, text="Score: 0", font=("comic sans ms", 25), bg="#D8FFDB")
lbl_score.grid(row=1, column=0, padx=(10, 0), pady=(0, 10))

# les liste pour afficher les nombres

'''
numbers = [[2, 4, 8, 16],
          [32, 64, 128, 256],
          [512, 1024, 2048, 4096],
          [8192, 4, 8, 0]]
'''

numbers = [[0, 0, 2, 0],
          [0, 0, 0, 0],
          [0, 0, 2, 0],
           [0,0,0,0]]
'''

numbers = [[0, 0, 1024, 0],
          [0, 0, 0, 0],
          [0, 0, 1024, 0],
          [0, 0, 0, 0]]
'''

#bibliothèque de couleur
colors = {0: "#F2E3D5",
        2 : "#D8FFDB",
        4 : "#DAFDBA",
        8 : "#9AEBA3",
        16 : "#93D94E",
        32 : "#60BF81",
        64 : "#3B8C66",
        128 : "#367356",
        256 : "#008F8C",
        512 : "#005C53",
        1024 : "#023535",
        2048 : "#21445B",
        4096 : "#323050",
        8192 : "#38184C"}

# pour crée le tableau
labels = [[None, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]]

#labels creation and position (1. Creation 2. position)
for line in range(len(numbers)):
    for col in range(len(numbers[line])):

        labels[line][col] = Label(frame_tableau, width=6, height=3, borderwidth=2, relief="solid", font=("comic sans ms", 22))
        # label pour positioner le placement
        labels[line][col].grid(row=line+1, column=col, padx=5, pady=5)
display()

# ------- Bouton ------- #

#bouton pour recommancer le 2048
bouton_restart = Button(frame_bot, text="Restart", command=restart, width=7, font=("comic sans ms", 25, "bold"), fg="white", bg="#00747C")
bouton_restart.pack(side=LEFT,padx= 130)

#bouton pour quitter l'application
bouton_recommancer = Button(frame_bot, text= "Quitter",command=quitter,width=7, font=("comic sans ms", 25, "bold"), fg="white", bg="#00747C")
bouton_recommancer.pack(side=LEFT,fill = X)

#pour implementer
root.bind("<Key>", touche_presse)

root.mainloop()

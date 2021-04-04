import webbrowser
from random import randint
from tkinter import Tk, messagebox, BOTTOM, PanedWindow, LEFT, Frame, Label, YES, Button

window = Tk()
window.title("démineur")
window.geometry("575x493")
window.minsize(575, 493)
window.config(background='#FFFFFF')

# fenetre démineur
fenetre = PanedWindow(window)
fenetre.pack(side=LEFT)
fenetre.config(background='#FFFFFF')
window.iconbitmap("démineur.ico")
# score board
score_board = ()

# fenetre score board
left_window = PanedWindow(window, borderwidth=4,relief='groove')
left_window.pack()
left_window.config(background='#FFFFFF',width=20)

# sous fentre 1
def acces_credit():
    def open_github():
        webbrowser.open_new("https://github.com/olivier-be/d-mineurs-python")

    def fermer_fenetre():
        frame.quit()

    fenetre_credit = Tk()
    fenetre_credit.title("démineur")
    window.iconbitmap("démineur.ico")
    fenetre_credit.geometry("1080x720")
    fenetre_credit.minsize(1080, 720)
    fenetre_credit.config(background='#FFFFFF')
    frame = Frame(fenetre_credit, bg='#FFFFFF')
    texted1 = Label(frame, text="bienvenue sur le démineur", font=("Courrier", 40), bg='#FFFFFF')
    texted1.pack(expand=YES)
    texted2 = Label(frame, text="réaliser par Olivier,Yanis et Clément", font=("Courrier", 20), bg='#FFFFFF')
    texted2.pack(expand=YES)
    gt_buttion = Button(frame, text="ouvrir github", font=("Courrier", 20), bg='#FFFFFF', command=open_github)
    gt_buttion.pack(side=BOTTOM, pady=100)
    quit_buttion = Button(frame, text="quitter crédit", font=("Courrier", 20), bg='#FFFFFF', command=fermer_fenetre)
    quit_buttion.pack(side=BOTTOM, pady=50)
    frame.pack()
    fenetre_credit.mainloop()

button_credit = Button(left_window, text="credit", command=acces_credit, width=15).grid(row=12,column=0)
button_menu = Button(left_window, text="menu", width=15).grid(row=17,column=0)

# position mine
tab_mine = [[0, 0]]

for i in range(4):
    tab_mine.append([randint(0, 18), randint(0, 9)])
print(tab_mine)
nb = 1
tab = [Button] * 200
score = 0
scorec = Label(left_window, text= "0", width=15).grid(row=0, column=0)
# score ( case déactiver avant de toucher une mine )
def point():
    global score,scorec
    score = score + 1
    print(str(score))
    scoree=str(score)
    scorec = Label(left_window, text=scoree, width=15).grid(row=0, column=0)
    return score

def minetoucher():
    print("vous avez perdu")
    global score
    messagebox.showerror(title="démineur",message=" tu as perdu \n partie termier !\n ton score est de {}".format(score))
    score = str(score)
    with open("../pythonProject5/score.txt", "a+") as file:
        file.write(score + "\n")
        print(score)
        file.close()

    return 0

tabnb = [[0, 0]] * 191
tabm = [0] * 191
i = 1
z = 1
e = 1

def verification(i, ligne, colonne):
    z = 0
    global tab
    print("start", ligne, colonne)
    for e in range (2):
        u = 0
        v=ligne
        print(e)
        print("start", ligne, colonne)
        p=0

        while (u==0 or u==1 or u==2 or u==3 or u==4):
            for b in range(191):
                if [ligne,colonne]in tabnb:
                    for x in range(-2,1,2):
                        if ligne + x != tab_mine[b][0] and colonne != tab_mine[b][1] and tab[b] != tabl[b].grid_forget:
                            print("a")
                        elif ligne == tab_mine[b][0] and colonne + x == tab_mine[b][1] and tab[b] != tabl[b].grid_forget:
                            tab[e+p].grid_forget()
                            print("e")
                        else:
                            u += 1
            p=p+1
        if u == 3:
            print("vérifier")
            z = 1
            p+=1
        ligne = tabnb[e + i][0]
        colonne = tabnb[e + i][1]

def change_nom_proche(i, ligne, colonne):
    tab[i].grid_forget()
    Label(fenetre, text="1", width=5).grid(row=ligne, column=colonne)
    #verification(i, ligne, colonne)

# creation grille button dans une matrice

def suprimer(i, ligne, colonne):
    tab[i].grid_forget()
    Label(fenetre, text="0", width=5).grid(row=ligne, column=colonne)
    #verification(i, ligne, colonne)
    point()

tabl = tab
test = 0
for ligne in range(19):
    for colonne in range(10):
        if ligne == tab_mine[1][0] and colonne == tab_mine[1][1] or ligne == tab_mine[2][0] and colonne == tab_mine[2][1] or ligne == tab_mine[3][0] and colonne == tab_mine[3][1] or ligne == tab_mine[4][0] and colonne == tab_mine[4][1]:
            tab[i] = Button(fenetre, text="mine0", command=minetoucher).grid(row=ligne, column=colonne)
            tabl[i] = Label(fenetre, text="2", width=5)
            tabnb[i][0] = ligne
            tabnb[i][1] = colonne
            test = 1
            print("a", i)
        if test == 0:
            for t in range(4):
                if ((ligne == tab_mine[t + 1][0] - 1 or ligne == tab_mine[t + 1][0] + 1 or ligne == tab_mine[t + 1][0]) and (colonne == tab_mine[t + 1][1] - 1 or colonne == tab_mine[t + 1][1] + 1)) or ((ligne == tab_mine[t + 1][0] - 1 or ligne == tab_mine[t + 1][0] + 1) and (colonne == tab_mine[t + 1][1] - 1 or colonne == tab_mine[t + 1][1] + 1 or colonne ==
                        tab_mine[t + 1][1])):
                    tab[i] = Button(fenetre, text="mine?", bg='#DC1010', width=5,
                                    command=lambda i=i, ligne=ligne, colonne=colonne: change_nom_proche(i, ligne,colonne) and point()).grid(row=ligne, column=colonne)
                    tabl[i] = Label(fenetre, text="1", width=5)
                    tabnb[i][0] = ligne
                    tabnb[i][1] = colonne
                    test = 1
                    print("2", i)
        if test < 1:
            tab[i] = Button(fenetre, text="mine?", width=5,
                            command=lambda i=i, ligne=ligne, colonne=colonne: suprimer(i, ligne, colonne) and print(i)).grid(row=ligne, column=colonne)
            tabl[i] = Label(fenetre, text="0", width=5)
            tabnb[i][0] = ligne
            tabnb[i][1] = colonne
            print(i)
        i = i + 1
        test = 0

window.mainloop()


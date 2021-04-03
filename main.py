from random import *
from tkinter import *
import webbrowser
from tkinter import messagebox
from score import *
window=Tk()
window.title("démineur")
window.geometry("558x493")
window.minsize(568, 493)
window.iconbitmap("démineur.ico")
window.config(background='#FFFFFF')

# fenetre démineur
fenetre=PanedWindow(window)
fenetre.pack(side=LEFT)
fenetre.config(background='#FFFFFF')

#score board
score_board=()

#fenetre score board
left_window = Frame(window)
left_window.pack(side=BOTTOM)
left_window.config(background='#FFFFFF')

#sous fentre 1
def acces_credit():
    def opencredit():
        fenetre_credit.quit()
        fenetre.mainloop()
    fenetre_credit = Tk()
    def open_github():
        webbrowser.open_new("https://github.com/olivier-be/d-mineurs-python")
    fenetre_credit.title("démineur")
    fenetre_credit.geometry("1080x720")
    fenetre_credit.minsize(1080, 720)
    fenetre_credit.iconbitmap("démineur.ico")
    fenetre_credit.config(background='#FFFFFF')
    fenetre.quit()
    fenetre_credit.mainloop()
    textedebut = Label(fenetre_credit, text="bienvenue sur le démineur", font=("Courrier", 40), bg='#FFFFFF')
    textedebut.pack(expand=YES)
    credit = Label(fenetre_credit, text="réaliser par Olivier,Yanis et Clément", font=("Courrier", 20), bg='#FFFFFF')
    credit.pack(expand=YES)
    gt_buttion = Button(fenetre_credit, text="ouvrir github", font=("Courrier", 20), bg='#FFFFFF', command=open_github)
    gt_buttion.pack(side=BOTTOM, pady=100)
    quit_buttion = Button(fenetre_credit, text="quitter crédit", font=("Courrier", 20), bg='#FFFFFF',command=opencredit())
    quit_buttion.pack(side=BOTTOM, pady=50)
button=Button(left_window,text="credit",command=acces_credit,width=20)
button.pack(side=LEFT)

#position mine
tabmine=[[0,0]]

for i in range (4):
    tabmine.append([randint(0,18),randint(0,9)])
print(tabmine)
nb = 1
tab=[Button]*200
score=0

#score ( case déactiver avant de toucher une mine )
def point():
    global score
    score=score+1
    return score


def minetoucher():
    print("vous avez perdu")
    global score
    messagebox.showerror(title="démineur", message=" tu as perdu \n partie termier !\n ton score est de {}".format(score))
    score=str(score)
    with open("../pythonProject3/score.py", "a+") as file:
        file.write(score)
        print(score)
        file.close()

    return 0

tabnb=[[0,0]]*191
tabm=[0]*191
i=1
z=1
e=1
def verification(i,ligne,colonne):
    e = i
    z = 0
    print("start",ligne,colonne)
    while z == 1:
        ligne = tabl[e][0]
        colonne = tabl[e][1]
        print("start", ligne, colonne)
        if ligne + 1 != tabmine[1][0] and colonne != tabmine[1][1] :
            tab[e].grid_forget()
        elif ligne == tabmine[1][0] and colonne + 1 == tabmine[1][1] and tab[e] != tabl[e].grid_forget:
            tab[e].grid_forget()
        elif ligne == tabmine[1][0] and colonne - 1 == tabmine[1][1] and tab[e] != tabl[e].grid_forget:
            tab[e].grid_forget()
        elif ligne - 1 == tabmine[1][0] and colonne == tabmine[1][1] and tab[e] != tabl[e].grid_forget:
            tab[e].grid_forget()
        elif ligne + 1 != tabmine[2][0] and colonne != tabmine[2][1] and tab[e] != tabl[e].grid_forget:
            tab[e].grid_forget()
        elif ligne == tabmine[2][0] and colonne + 1 == tabmine[2][1] and tab[e] != tabl[e].grid_forget:
            tab[e].grid_forget()
        elif ligne == tabmine[2][0] and colonne - 1 == tabmine[2][1] and tab[e] != tabl[e].grid_forget:
            tab[e].grid_forget()
        elif ligne - 1 == tabmine[2][0] and colonne == tabmine[2][1] and tab[e] != tabl[e].grid_forget:
            tab[e].grid_forget()
        elif ligne + 1 != tabmine[3][0] and colonne != tabmine[3][1] and tab[e] != tabl[e].grid_forget:
            tab[e].grid_forget()
        elif ligne == tabmine[3][0] and colonne + 1 == tabmine[3][1] and tab[e] != tabl[e].grid_forget:
            tab[e].grid_forget()
        elif ligne == tabmine[3][0] and colonne - 1 == tabmine[3][1] and tab[e] != tabl[e].grid_forget:
            tab[e].grid_forget()
        elif ligne - 1 == tabmine[3][0] and colonne == tabmine[3][1] and tab[e] != tabl[e].grid_forget:
            tab[e].grid_forget()
        elif ligne + 1 != tabmine[4][0] and colonne != tabmine[4][1] and tab[e] != tabl[e].grid_forget:
            tab[e].grid_forget()
        elif ligne == tabmine[4][0] and colonne + 1 == tabmine[4][1] and tab[e] != tabl[e].grid_forget:
            tab[e].grid_forget()
        elif ligne == tabmine[4][0] and colonne - 1 == tabmine[4][1] and tab[e] != tabl[e].grid_forget:
            tab[e].grid_forget()
        elif ligne - 1 == tabmine[4][0] and colonne == tabmine[4][1] and tab[e] != tabl[e].grid_forget:
            tab[e].grid_forget()
        else:
            print("vérifier")
            z = 1
        e = e + 1

def change_nom_proche(i,ligne,colonne):
    tab[i].grid_forget()
    Label(fenetre,text="1",width=5).grid(row=ligne,column=colonne)
    verification(i,ligne,colonne)

# creation grille button dans une matrice


def suprimer(i,ligne,colonne):
    globals()
    tab[i].grid_forget()
    Label(fenetre,text="0",width=5).grid(row=ligne, column=colonne)
    verification(i, ligne, colonne)

z=0
tabl=tab
for ligne in range(19):
    for colonne in range(10):
        if ligne == tabmine[1][0] and colonne == tabmine[1][1] or  ligne == tabmine[2][0] and colonne == tabmine[2][1] or ligne == tabmine[3][0] and colonne == tabmine[3][1] or ligne == tabmine[4][0] and colonne == tabmine[4][1] :
            tab[i]=Button(fenetre, text="mine0", command=minetoucher)
            tab[i].grid(row=ligne, column=colonne)
            tabl[i]=Label(fenetre,text="2",width=5)
            tabnb[i][0] = ligne
            tabnb[i][1] = colonne
            print("a", i)
        elif  ((ligne== tabmine[1][0] - 1 or ligne == tabmine[1][0] + 1 or ligne == tabmine[1][0]) and (colonne == tabmine[1][1] - 1 or colonne == tabmine[1][1] + 1 )) or ((ligne== tabmine[1][0] - 1 or ligne == tabmine[1][0] + 1) and (colonne == tabmine[1][1] - 1 or colonne == tabmine[1][1] + 1 or colonne == tabmine[1][1])):
            tab[i]=Button(fenetre, text="mine?",bg='#DC1010',width=5,command=lambda i=i,ligne=ligne,colonne=colonne: change_nom_proche(i,ligne,colonne) and point)
            tab[i].grid(row=ligne, column=colonne)
            tabl[i]=Label(fenetre, text="1", width=5)
            tabnb[i][0] = ligne
            tabnb[i][1] = colonne
            print("2",i)
        elif  ((ligne== tabmine[2][0] - 1 or ligne == tabmine[2][0] + 1 or ligne == tabmine[2][0]) and (colonne == tabmine[2][1] - 1 or colonne == tabmine[2][1] + 1 )) or ((ligne== tabmine[2][0] - 1 or ligne == tabmine[2][0] + 1) and (colonne == tabmine[2][1] - 1 or colonne == tabmine[2][1] + 1 or colonne == tabmine[2][1])):
            tab[i]=Button(fenetre, text="mine?",bg='#DC1010',width=5,command=lambda i=i,ligne=ligne,colonne=colonne: change_nom_proche(i,ligne,colonne) and point)
            tab[i].grid(row=ligne, column=colonne)
            tabl[i]=Label(fenetre, text="1", width=5)
            tabnb[i][0] = ligne
            tabnb[i][1] = colonne
            print("2",i)
        elif  ((ligne== tabmine[3][0] - 1 or ligne == tabmine[3][0] + 1 or ligne == tabmine[3][0]) and (colonne == tabmine[3][1] - 1 or colonne == tabmine[3][1] + 1 )) or( (ligne== tabmine[3][0] - 1 or ligne == tabmine[3][0] + 1 ) and (colonne == tabmine[3][1] - 1 or colonne == tabmine[3][1] + 1 or colonne == tabmine[3][1])):
            tab[i] = Button(fenetre, text="mine?",bg='#DC1010',width=5, command=lambda i=i,ligne=ligne,colonne=colonne: change_nom_proche(i,ligne,colonne) and point)
            tab[i].grid(row=ligne, column=colonne)
            tabl[i]=Label(fenetre, text="1", width=5)
            tabnb[i][0] = ligne
            tabnb[i][1] = colonne
            print("2", i)
        elif  ((ligne== tabmine[4][0] - 1 or ligne == tabmine[4][0] + 1 or ligne == tabmine[4][0]) and (colonne == tabmine[4][1] - 1 or colonne == tabmine[4][1] + 1 )) or ((ligne== tabmine[4][0] - 1 or ligne == tabmine[4][0] + 1 ) and (colonne == tabmine[4][1] - 1 or colonne == tabmine[4][1] + 1 or colonne == tabmine[4][1])) :
            tab[i] = Button(fenetre, text="mine?",bg='#DC1010',width=5, command=lambda i=i,ligne=ligne,colonne=colonne: change_nom_proche(i,ligne,colonne) and point)
            tab[i].grid(row=ligne, column=colonne)
            tabl[i]=Label(fenetre, text="1", width=5)
            tabnb[i][0] = ligne
            tabnb[i][1] = colonne
            print("2", i)
        else:
            tab[i] = Button(fenetre, text="mine?",width=5, command=lambda i=i,ligne=ligne,colonne=colonne: suprimer (i,ligne,colonne) and print(i))
            tab[i].grid(row=ligne,column=colonne)
            tabl[i]=Label(fenetre, text="0", width=5)
            tabnb[i][0] = ligne
            tabnb[i][1] = colonne
            print(i)
        i=i+1

window.mainloop()
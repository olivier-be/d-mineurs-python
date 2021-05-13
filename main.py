import webbrowser
from random import randint
from tkinter import Tk, messagebox, BOTTOM, PanedWindow, LEFT, Frame, Label, YES, Button

#donner le chemin d'accès du ficher du programe sans \main.py et il faut doubler le slash après le disque ex C:\\ et
# il faut verifer qu'il y a \d-mineurs-python-main\d-mineurs-python-main a la fin
accesficher="C:\\Users\olivi\Downloads\d-mineurs-python-main\d-mineurs-python-main"
window = Tk()
window.title("démineur")
window.geometry("575x493")
window.minsize(575, 493)
window.config(background='#FFFFFF')

# fenetre démineur
fenetre = PanedWindow(window)
fenetre.pack(side=LEFT)
fenetre.config(background='#FFFFFF')
window.iconbitmap(accesficher+"\démineur.ico")

# fenetre score board
left_window = PanedWindow(window, borderwidth=4,relief='groove')
left_window.pack()
left_window.config(background='#FFFFFF',width=20)
# score board
score_board =PanedWindow(window, borderwidth=4,relief='groove')
score_board.pack()
score_board.config(background='#FFFFFF',width=20)


# sous fentre 1
def acces_credit():
    def open_github():
        webbrowser.open_new("https://github.com/olivier-be/d-mineurs-python")

    def fermer_fenetre():
        fenetre_credit.quit()

    fenetre_credit = Tk()
    fenetre_credit.title("démineur")
    #window.iconbitmap(accesficher+"\démineur.ico")
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
    #quit_buttion.pack(side=BOTTOM, pady=50)
    frame.pack()
    fenetre_credit.mainloop()
accesficher+="\score.txt"
print(accesficher)
button_credit = Button(left_window, text="credit", command=acces_credit, width=15).grid(row=12,column=0)
button_menu = Button(left_window, text="menu", width=15).grid(row=17,column=0)
with open(accesficher,"r") as file:
    tab_score= file.readlines()
    print(tab_score)
    tab_scorer=["a"]*(len(tab_score))
    n=0
    for t in range(len(tab_scorer),0,-1):
        tab_scorer[t-1]=tab_score[n]
        n+=1
        print(t)
    print(tab_scorer)
    nb_ligne=8
    if len(tab_scorer)<8:
        nb_ligne=len(tab_scorer)
    tab_scorela=[Button]*len(tab_scorer)
    for m in range(nb_ligne):
        print("a")
        print(tab_scorer[m])
        tab_scorela[m]=Label(score_board, text="{} score prec = {}".format(m,tab_scorer[m]), width=15).grid(row=m, column=0)
    file.close()

m=0
nbmine=10
# position mine
tab_mine = [[randint(0, 18), randint(0, 9)]]
for i in range(nbmine):
    tab_mine.append([randint(0, 18), randint(0, 9)])
print(tab_mine)
nb = 1
tab = [Button] * 200
score = 0
scorec = Label(left_window, text= "0", width=15).grid(row=0, column=0)
# score ( case déactiver avant de toucher une mine )
def point():
    global score,scorec,nbmine
    score = score + 1
    print(str(score))
    scoree=str(score)
    scorec = Label(left_window, text=scoree, width=15).grid(row=0, column=0)
    if score>200-nbmine:
        messagebox.showerror(title="démineur",message=" tu as gagner \n partie termier !\n ton score est de {}".format(score))
        with open(accesficher, "a+") as files:
            files.write(str(score) + "\n")
            print(score)
            files.close()
        window.quit()
    return score

def minetoucher():
    print("vous avez perdu")
    global score,fenetre_credit
    messagebox.showerror(title="démineur",message=" tu as perdu \n partie termier !\n ton score est de {}".format(score))
    score = str(score)
    with open(accesficher, "a+") as file:
        file.write(score + "\n")
        print(score)
        file.close()
    window.destroy()
    return 0

tabnb = [[0, 0]] * 191
tabm = [0] * 191
i = 1
z = 1
e = 1
tab_mine_proche=[[0,0]]*(8*nbmine)
def pointmarquer(m, n):
    print(n)
    for e in range(len(m)):
        if m[e]==1 and n[e]=="0":
            point()
            n[e]= "1"
    return n
def verif3(i, ligne, colonne, m, z, t, e, x, n, o, y):
    global tabnb, tab
    print(i, "= i ", x, "= x", m, "= m")
    print(colonne, "colonne", z, "colonne-")
    if [ligne +1, colonne] in tab_mine or [ligne+1, colonne ] in tab_mine_proche and [ligne,colonne] in o:
        i=i
    elif ligne <= 20:
        ligne += 1
        print("verifie colonne", ligne)
        i = i + 1
        print(i)
        tab[i].grid_forget()
        Label(fenetre, text="0", width=5).grid(row=ligne, column=colonne)
        m[i] = 1
        pointmarquer(m, n)
        print(m)
        verif1(i, ligne, colonne, m, z, t, e, x, n, o, y)
        verif2(i, ligne, colonne, m, z, t, e, x, n, o, y)
        verif3(i, ligne, colonne, m, z, t, e, x, n, o, y)

def verif4(i, ligne, colonne, m, z, t, e, x, n, o, y):
    global tabnb, tab
    print(t, "= t ", x, "= x", m, "= m")
    print(colonne, "colonne", z, "colonne-")
    if [ligne -1, colonne] in tab_mine or [ligne-1, colonne ] in tab_mine_proche and ligne>0 and [ligne,colonne] in o:
        t = t
    elif ligne >= 1:
        ligne -= 1
        print("verifie colonne", ligne)
        t = t - 10
        print(t)
        tab[t].grid_forget()
        Label(fenetre, text="0", width=5).grid(row=ligne, column=colonne)
        m[t] = 1
        print(m)
        pointmarquer(m, n)
        verif1(i, ligne, colonne, m, z, t, e, x, n, o, y)
        verif2(i, ligne, colonne, m, z, t, e, x, n, o, y)
        verif4(i, ligne, colonne, m, z, t, e, x, n, o, y)

def verif1(i, ligne, colonne, m, z, t, e, x, n, o, y):
    global tabnb,tab
    print(i,"= i ",x,"= x",m,"= m")
    print(colonne,"colonne",z,"colonne-")
    if [ligne,colonne+1]in tab_mine or[ligne,colonne+1] in tab_mine_proche or colonne<1 and [ligne,colonne] in o:
        i=i
    elif colonne <= 8:
        colonne += 1
        print("verifie colonne",colonne)
        i = i +1
        print(i)
        tab[i].grid_forget()
        Label(fenetre, text="0", width=5).grid(row=ligne, column=colonne)
        o[i] = [ligne, colonne]
        m[i] = 1
        pointmarquer(m, n)
        verif1(i, ligne, colonne, m, z, t, e, x, n, o, y)
def verif2(i, ligne, colonne, m, z, t, e, x, n, o, y):
    global tabnb, tab
    print(i, "= i ", x, "= x", m, "= m")
    print(colonne, "colonne", z, "colonne-")
    if [ligne,z-1]in tab_mine or[ligne,z-1] in tab_mine_proche or z<1 and [ligne,z] in o:
        i=i
    elif z >= 1:
        z -= 1
        print(z,"start")
        print("verifie colonne", z)
        x = x - 1
        print(x)
        tab[x].grid_forget()
        Label(fenetre, text="0", width=5).grid(row=ligne, column=z)
        o[x]=[ligne,z]
        m[x] = 1
        pointmarquer(m, n)
        verif2(i, ligne, colonne, m, z, t, e, x, n, o, y)

def verification(i, ligne, colonne):
    print("start", ligne, colonne)
    print("start verification ligne:", ligne)
    m = [0]*200
    z=colonne
    t=i
    e=i
    x=i
    print(x)
    o=[0,0]*200
    y=0
    n=["0"]*200
    o[i] = [ligne, colonne]
    print(i, " numéro case")
    print(n)
    verif1(i, ligne, colonne,m, z,t,e,x,n,o,y)
    verif2(i, ligne, colonne, m, z, t, e, x,n,o,y)
    verif3(i, ligne, colonne, m, z, t, e, x,n,o,y)
    verif4(i, ligne, colonne, m, z, t, e, x, n, o,y)

def change_nom_proche(i, ligne, colonne):
    tab[i].grid_forget()
    m=0
    for t in range(nbmine):
        if ((ligne == tab_mine[t + 1][0] - 1 or ligne == tab_mine[t + 1][0] + 1 or ligne == tab_mine[t + 1][0])
        and (colonne == tab_mine[t + 1][1] - 1 or colonne == tab_mine[t + 1][1] + 1)) or \
        ((ligne == tab_mine[t + 1][0] - 1 or ligne == tab_mine[t + 1][0] + 1) and (
        colonne == tab_mine[t + 1][1] - 1
        or colonne == tab_mine[t + 1][1] + 1 or colonne == tab_mine[t + 1][1])):
            m+=1

    Label(fenetre, text=str(m), width=5).grid(row=ligne, column=colonne)
    point()


# creation grille button dans une matrice

def suprimer(i, ligne, colonne):
    tab[i].grid_forget()
    Label(fenetre, text="0", width=5).grid(row=ligne, column=colonne)
    print(i)
    verification(i, ligne, colonne)
    point()

tabl = tab
test = 0
b=1
for ligne in range(19):
    for colonne in range(10):
        for y in range (nbmine+1):
            if ligne == tab_mine[y][0] and colonne == tab_mine[y][1] and y!=0:
                tab[i] = Button(fenetre, text="mine0", command=minetoucher).grid(row=ligne, column=colonne)
                tabl[i] = Label(fenetre, text="2", width=5)
                tabnb[i]= [ligne,colonne]
                test = 1
                print("a", i)
        if test == 0:
            for t in range(nbmine):
                if ((ligne == tab_mine[t + 1][0] - 1 or ligne == tab_mine[t + 1][0] + 1 or ligne == tab_mine[t + 1][0])
                and (colonne == tab_mine[t + 1][1] - 1 or colonne == tab_mine[t + 1][1] + 1)) or \
                ((ligne == tab_mine[t + 1][0] - 1 or ligne == tab_mine[t + 1][0] + 1) and (colonne == tab_mine[t + 1][1] - 1
                or colonne == tab_mine[t + 1][1] + 1 or colonne ==tab_mine[t + 1][1])) :
                    tab[i] = Button(fenetre, text="mine?", bg='#DC1010', width=5,
                    command=lambda i=i, ligne=ligne, colonne=colonne: change_nom_proche(i, ligne,colonne)and print(i)).grid(row=ligne, column=colonne)
                    tabl[i] = Label(fenetre, text="1", width=5)
                    tab_mine_proche[b]=[ligne,colonne]
                    tabnb[i] = [ligne, colonne]
                    b+=1
                    test = 1
                    print("2", i)
        if test < 1:
            tab[i] = Button(fenetre, text="mine?", width=5,
            command=lambda i=i, ligne=ligne, colonne=colonne: suprimer(i, ligne, colonne) and print(i)).grid(row=ligne, column=colonne)
            tabl[i] = Label(fenetre, text="0", width=5)
            tabnb[i] = [ligne, colonne]
            print(i)
        i = i + 1
        test = 0
print(tabnb)

window.mainloop()

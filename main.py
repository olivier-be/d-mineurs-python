
def suprimer(i, ligne, colonne):
    tab[i].grid_forget()
    Label(fenetre, text="0", width=5).grid(row=ligne, column=colonne)
    verification(i, ligne, colonne)
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



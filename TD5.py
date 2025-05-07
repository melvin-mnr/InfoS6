from tkinter import Tk, Canvas, Button
import random

root=Tk()
can = Canvas(root, width=1000,height=500,bg='light grey')
can.grid(column=0, row=0, columnspan=1)
couleur=['black','red','blue','green','yellow','orange']
tableau=[1,2,0,0]
n=4

def read_word(canva, mot, h, w,y,col):
    x=0
    for i in mot :
        if i=='H':
            canva.create_line(x,y,x+h,y,fill=col)
            x,y=x+h,y
        if i=='U':
            canva.create_line(x,y,x+w,y-h,fill=col)
            x,y=x+w,y-h
        if i=='D':
            canva.create_line(x,y,x+w,y+h,fill=col)
            x,y=x+w,y+h
    return

def entrelacs_mots(canva,liste,n):
    y=50
    h=50
    for i in range(n):
        #i la position initiale de la ligne, j sa position au fil des entrelacs, k la position de la ligne qui doit croiser avec la k+1 ème
        mot='H'
        j=i
        for k in liste :
            if j==k :
                mot+='D'
                j+=1
            elif j==k+1:
                mot+='U'
                j-=1
            else :
                mot+='H'
            mot+='H'
            read_word(canva,mot,h,h,y+h*i,couleur[i%len(couleur)])
    return


def entrelacs(canva, liste, n):
    h=50
    x,y=0,50
    k=0
    #on allonge la liste de couleurs si il a trop de lignes à créer pour pas modifier les couleurs de plusieurs lignes en même temps sans faire exprès
    while len(couleur)<n:
        couleur.append(couleur[k%6])
        k+=1
    #initialisation avec le début de chaque ligne
    for i in range(n):
        canva.create_line(x,y+i*h,x+h,y+i*h,fill=couleur[i])
    x+=h
    for i in liste:
        #on croise les lignes qu'il faut faire croiser
        canva.create_line(x,y+i*h,x+h,y+(i+1)*h,fill=couleur[i])
        canva.create_line(x,y+(i+1)*h,x+h,y+i*h,fill=couleur[(i+1)])
        #on change l'ordre des couleurs dans la liste pour tenir compte du croisement
        couleur[i],couleur[(i+1)]=couleur[(i+1)],couleur[i]
        for j in range(n):
            if j!=i and j!=i+1 :
                #on allonge les lignes qui n'ont pas croisé
                canva.create_line(x,y+j*h,x+h,y+j*h,fill=couleur[j])
            #puis on allonge toutes les lignes
            canva.create_line(x+h,y+j*h,x+2*h,y+j*h,fill=couleur[j])
        x+=2*h
    return


def permute():
    random.shuffle(couleur)
    can.delete(all)
    entrelacs_mots(can,tableau,n)

but1 = Button(root, text ='Quit', command = root.destroy)
but1.grid(column=0,row=1,ipadx=10,sticky='E')

but2=Button(root, text='Colors', command=permute)
but2.grid(column=1,row=1,padx=10,sticky='W')

entrelacs_mots(can,tableau,n)

root.mainloop()

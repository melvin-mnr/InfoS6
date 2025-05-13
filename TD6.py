from tkinter import Tk, Canvas, Button,Label
import random

class App :
    def __init__(self,data):
        self.root=Tk()
        self.data=data
        self.canva=Canvas(self.root,width=1000 ,height=500 ,bg='whitesmoke')
        self.canva.grid(column=0, row=0, columnspan=2)

    def run_forever(self):
        self.root.mainloop()

    def redraw(self):
        self.canva.delete(all)
        self.root.update()
        #W et H représentent la taille totale de la fenêtre
        #avec le nombre de lignes { self.data.n }
        #et le nombre d'entrelacs { len(self.data.liste_mot()[0]) }
        #on définit les longueurs des saut h et w pour ajuster le dessin à la fenêtre
        H=self.root.winfo_height()
        W=self.root.winfo_width()
        h=H/(self.data.n+1)
        w=W/(2*len(self.data.liste_mot()[0])+1)

        #{ col } est liste initiale de couleurs qu'on agrandit en { couleur } pour correspondre au nombre de lignes qu'on va créer
        #puis on rend l'ordre des couleurs aléatoire pour qu'il change à chaque redraw du canva
        col=['black','red','blue','green','yellow','orange','pink']
        couleur=[col[i%len(col)] for i in range(self.data.n)]
        random.shuffle(couleur)

        j=0
        for mot in self.data.liste_mot() :
            x=0
            y=h*(j+1)
            for i in mot :
                if i=='H':
                    self.canva.create_line(x,y,x+w,y,fill=couleur[j])
                    x,y=x+w,y
                if i=='U':
                    self.canva.create_line(x,y,x+w,y-h,fill=couleur[j])
                    x,y=x+w,y-h
                if i=='D':
                    self.canva.create_line(x,y,x+w,y+h,fill=couleur[j])
                    x,y=x+w,y+h
            j+=1

        #on crée les boutons et textes
        but1 = Button(self.root, text ='Quit', command = self.root.destroy)
        but1.grid(column=0,row=2,padx=10,sticky='E')

        but2=Button(self.root, text='Colors', command=self.redraw)
        but2.grid(column=1,row=2,padx=10,sticky='W')

        mot1= Label(self.root, text='Croisements :')
        mot1.grid(column=0,row=1,padx=10,sticky='E')

        mot2=Label(self.root,text=str(self.data.tableau))
        mot2.grid(column=1,row=1,padx=10,sticky='W')

        return

class Data :
    def __init__(self,tableau,n):
        self.n=n
        self.tableau=tableau

    def liste_mot(self):
        liste=[]
        for i in range(self.n):
        #i la position initiale de la ligne, j sa position au fil des entrelacs, k la position de la ligne qui doit croiser avec la k+1 ème
            mot='H'
            j=i
            for k in self.tableau :
                if j==k :
                    mot+='DH'
                    j+=1
                elif j==k+1:
                    mot+='UH'
                    j-=1
                else :
                    mot+='HH'
            liste.append(mot)
        return(liste)
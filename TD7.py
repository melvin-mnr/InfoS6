from tkinter import Tk, Canvas, Button,Label
import random

class App :
    def __init__(self,data):
        self.root=Tk()
        self.data=data
        self.canva=Canvas(self.root,width=600 ,height=600 ,bg='whitesmoke')
        self.canva.grid(column=0, row=0, columnspan=1)

    def draw(self):
        self.canva.delete('all')
        for i in range(len(self.data.graph)):
            for j in self.data.graph[i]:
                self.canva.create_line(self.data.pos[i][0], self.data.pos[i][1], self.data.pos[j][0], self.data.pos[j][1])
        i=0
        for (x, y) in self.data.pos:
            self.canva.create_oval(x-15,y-15,x+15,y+15,fill="#f3e1d4")
            self.canva.create_text((x,y),text=str(i),fill='black')
            i+=1

        but1 = Button(self.root, text ='Quit', command = self.root.destroy)
        but1.grid(column=0,row=1)

        self.root.bind('<f>',lambda e : self.update())
        return

    def run_forever(self):
        self.root.mainloop()

    def update(self):
        self.data.deplacement()
        self.draw()




class Data :
    def __init__(self,graph):
        self.graph=graph
        self.pos=[(random.uniform(17,583), random.uniform(17,583)) for i in range(len(graph))]
        self.vit=[((random.random()-0.5)*10, (random.random()-0.5)*10) for i in range(len(graph))]


    def deplacement(self):
        #{ T } est un tableau de la même forme que { self.graph } contitué de listes { t } avec les distances et directions entre les sommets reliés
        T=[]
        for i in range(len(self.graph)):
            t=[]
            for j in self.graph[i]:
                distance=( (self.pos[i][0]-self.pos[j][0])**2 + (self.pos[i][1]-self.pos[j][1])**2 )**0.5
                direction=( (self.pos[i][0]-self.pos[j][0])/distance , (self.pos[i][1]-self.pos[j][1])/distance )
                t.append((distance,direction))
            T.append(t)
        #pour chaque sommet on parcours ses voisins et on applique une méthode d'Euler pour connaitre l'accéleration que chaqun lui confère, puis la position résultante
        for i in range(len(self.graph)):
            for j in range(len(self.graph[i])):
                dt=10**(-2)
                dvx = -k*(T[i][j][0]-l)*T[i][j][1][0]*dt/m
                dvy = -k*(T[i][j][0]-l)*T[i][j][1][1]*dt/m
                self.vit[i]=(self.vit[i][0]+dvx,self.vit[i][1]+dvy)
                x = self.pos[i][0] + self.vit[i][0]*dt
                y = self.pos[i][1] + self.vit[i][1]*dt
        #on contraint les sommets à rester dans le canva
                if x <0:
                    x=0
                    self.vit[i]=(-self.vit[i][0]*3/4,self.vit[i][1])
                elif x >600:
                    x=600
                    self.vit[i]=(-self.vit[i][0]*3/4,self.vit[i][1])
                if y <0:
                    y=0
                    self.vit[i]=(self.vit[i][0],-self.vit[i][1]*3/4)
                if y >600:
                    y=600
                    self.vit[i]=(self.vit[i][0],-self.vit[i][1]*3/4)
                self.pos[i]=(x,y)
        return

k=10
l=10
m=1
a=[[2, 7, 3], [3, 4, 9, 10], [5, 8, 0], [10, 1, 4, 6, 0],[3, 1, 6], [2], [3, 10, 4], [0], [2], [10, 1], [3, 1, 6, 9]]
b=Data(a)
c=App(b)
c.draw()
c.run_forever()



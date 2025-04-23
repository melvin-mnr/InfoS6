class Polynomial :
    def __init__(self,ListeCoeff) :
        self.value=ListeCoeff

    def __str__ (self):
        n=len(self.value)
        StringCoeff=''
        if n==1:
            StringCoeff=str(self.value[0])

        if n>1:
            if self.value[0]!=0:
                StringCoeff=str(self.value[0])
                if self.value[0]<0:
                    StringCoeff=' - '+StringCoeff
                elif self.value[0]>0:
                    StringCoeff=' + '+StringCoeff
            if self.value[1]!=0:
                if abs(self.value[1])==1 :
                    StringCoeff='X' + StringCoeff
                else :
                    StringCoeff=str(self.value[1]) + '*X' + StringCoeff
                if self.value[1]<0:
                    StringCoeff=' - '+StringCoeff
                else self.value[1]>0:
                    StringCoeff=' + '+StringCoeff

            for i in range(2,n):

                if self.value[i] !=0:
                        if abs(self.value[i])==1:
                            StringCoeff='X^' + str(i) + ' + ' + StringCoeff
                        if self.value[i]<0:
                            StringCoeff=str(self.value[i]) + '*X^' + str(i) + ' + ' + StringCoeff
                    StringCoeff=str(self.value[i]) + '*X^' + str(i) + ' + ' + StringCoeff

                    if self.value[i]<0:
                        StringCoeff=' - '+StringCoeff
                    elif n>i+1:

        return StringCoeff

    def add(self,p2):
        p3=Polynomial([0])
        n=len(self.value)
        m=len(p.value)
        k=min(n,m)
        i=0
        while i<n or i<m :
            if i>n:
                p3.value


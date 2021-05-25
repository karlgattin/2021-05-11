from Hindeline.Raamat import raamat






class Külastaja:
    def __init__(self, eesNimi, perekonnaNimi):
        self.eesNimi = eesNimi
        self.perekonnaNimi = perekonnaNimi
        self.laenutatudRaamatud = []


    def laenutaRaamat(self, raamat):
        if not raamat.laenutatud:
            raamat.laenutatud = True
            self.laenutatudRaamatud.append(raamat)
        else:
            print("Raamat on juba välja laenutatud!")


    def tagastaRaamat(self, raamat):
        if raamat in self.laenutatudRaamatud:
            raamat.laenutatud = False
            self.laenutatudRaamatud.remove(raamat)
        else:
            print("Raamat pole laenutatud veel!")


    def kuvaLaenutatudRaamatud(self):
        if self.laenutatudRaamatud:
            for raamat in self.laenutatudRaamatud:
                print(raamat.tiitel)
        else:
            print("Sa ei ole lanutanud raamatuid!")




Külastaja1 = Külastaja('Andreas', 'Võsumägi')




Raamat1 = raamat("Harry Potter", "J. K. Rowling", 225)
Raamat2 = raamat("The Maze Runner", "James Dashner", 170)




Külastaja1.laenutaRaamat(Raamat1)
Külastaja1.laenutaRaamat(Raamat2)
Külastaja1.tagastaRaamat(Raamat1)
Külastaja1.laenutaRaamat(Raamat2)
Külastaja1.kuvaLaenutatudRaamatud()
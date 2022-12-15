class pythunder:
    def __init__(self, DATA0, DATA1, DATA2, DATA3, DATA4, DATA5, DATA6, DATA7):
        self.DATA0 = DATA0
        self.DATA1 = DATA1
        self.DATA2 = DATA2
        self.DATA3 = DATA3
        self.DATA4 = DATA4
        self.DATA5 = DATA5
        self.DATA6 = DATA6
        self.DATA7 = DATA7


    def __str__(self):
        result = f'{self.DATA0}{self.DATA1}{self.DATA2}{self.DATA3}{self.DATA4}{self.DATA5}{self.DATA6}{self.DATA7}'
        return result


    def method1(self):
        pass



class Community():
     def __init__(self, community, crime, population):
         self.community = community
         self.crime = crime
         self.population = population

        
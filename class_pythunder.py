class pythunder:
    def __init__(self, sector, community, crimecat, crimecount, residentpop, date, year):
        self.sector = sector
        self.community = community
        self.crimecat = crimecat
        self.crimecount = crimecount
        self.residentpop = residentpop
        self.date = date
        self.year = year



    def __str__(self):
        result = f'{self.sector}{self.community}{self.crimecat}{self.crimecount}{self.residentpop}{self.date}{self.year}'
        return result


    def method1(self):
        pass



class Community():
     def __init__(self, community, crime, population):
         self.community = community
         self.crime = crime
         self.population = population

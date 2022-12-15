
class percent:

    def __init__(self,community,count,population):
        self.community = community
        self.count = count
        self.population = population

    def __str__(self):
        result = f"{self.community}{self.count}{self.population}"
        return result

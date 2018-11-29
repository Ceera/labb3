# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

class OrmObj:

    def __init__(self, id, name, temperament, color, length):
        self.id = id
        self.name = name
        self.temperament = temperament
        self.color = color
        self.length = length
    
    def getSnake(self):
        return(self.id, self.name, self.temperament, self.color, self.length)
    
    def updateSnake(self, id, name, temperament, color, length):
        self.id = id
        self.name = name
        self.temperament = temperament
        self.color = color
        self.length = length
        



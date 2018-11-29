

class OrmCrud:
    from OrmObj import OrmObj
    #Konstruktor
    def __init__(self):
        #instansvariable that is unique  for every instance created through this class
            
            self.snakes = [] 
        
    
    #often soa is the first param to method self. It is a great codeconvention but has no meaning for python
    def add(self, OrmObj):
        self.snakes.append(OrmObj)
        
    def delete(self, id):
        for x in self.snakes:
            if(id == x.id):
                self.snakes.remove(x)
            
    def update(self, id, name , temperament, color, length):
         for x in self.snakes:
            if(id == x.id):
                x.name = name
                x.temeprament = temperament
                x.color = color
                x.length = length
                #OrmObj.updateSnake(id, name, temperament, color, length)
           
    def get_snakes(self):
        return self.snakes
    
    
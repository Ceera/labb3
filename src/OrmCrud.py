

class OrmCrud:
    
    #Konstruktor
        def__init__(self):
        #instansvariable that is unique  for every instance created through this class
    self.name = []#A list with all snakes
    
    #often soa is the first param to method self. It is a great codeconvention but has no meaning for python
    def add(self, name):
        self.names.append(name)
        
    def delete(self,name):
        if(name in self.names):
            self.names.remove(name)
            
    def update(self,old_name,new_name):
        for key, value in enumerate(self.names):
            if(value==old_name):
                self.names[key]=new_name
                break
    
    def get_snakes(self):
        return self.names
    
    
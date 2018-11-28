# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

if __name__ == "__main__":
    print "Hello World"


from OrmCrud import OrmCrud
crud = OrmCrud()
crud.add("Majsorm")
crud.add("Huggorm")
print(crud.get_snakes())

crud.delete("Snok")
crud.update("Mask", "Kobra")
print(crud.get_snakes())
crud.add("bajsorm")
exit()

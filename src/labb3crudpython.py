# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.



from OrmCrud import OrmCrud
from OrmObj import OrmObj
from operator import attrgetter

crud = OrmCrud()
OrmObj1 = OrmObj(1, "Mask", "Nice", "Black", 5)
crud.add(OrmObj1)
OrmObj2 = OrmObj(2, "Hussorm", "Angry", "Black", 25)
crud.add(OrmObj2)
OrmObj3 = OrmObj(3, "Majsorm", "Nice", "Green", 55)
crud.add(OrmObj3)

lista = crud.get_snakes()

for i in lista:
    print(i.getSnake())

crud.delete(1)

print("Deletar nr 1")

listaAfterDelete = crud.get_snakes()

for j in listaAfterDelete:
    print(j.getSnake())
    
print("Nu ska huggorm uppdateras till Huggmask")
    
crud.update(2, "Huggmask", "Hangry", "Red", 2)

listaAfterUpdate = crud.get_snakes()

for k in listaAfterUpdate:
    print(k.getSnake())
    
print("\n")
print("Sorterar listan på längd fallande:")
snakes_sort=crud.get_snakes()
snakes_sort.sort(key=attrgetter('length'),reverse=True)

array = crud.get_snakes()
for i in array:
    print(i.getSnake())
exit()

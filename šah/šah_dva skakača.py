import os
here = os.path.dirname(os.path.abspath(__file__))
filename_u = os.path.join(here,"ulaz1.txt")
filename_i = os.path.join(here,"izlaz1.txt")

lista_next_x = []
lista_next_y = []
lista_next =[]
# ova funkcija nam vraća sve moguće poteze skakača
# ulaz je int
# izlaz je lista
def moves(knight):
    lista_next =[]
    x_next = 0
    y_next = 0
    a = int(knight[0])
    b = int(knight[1])
    x_move = [2, 1, -1, -2, -2, -1, 1, 2]
    y_move = [1, 2, 2, 1, -1, -2, -2, -1]
    for x,y in zip(x_move, y_move):
        x_next = x + a
        y_next = y + b
        if x_next < 0 or y_next < 0 or x_next > 7 or y_next > 7:
          pass
        else:
          lista_next_x.append(x_next)
          lista_next_y.append(y_next)
          lista_next.append(str(x_next) + str(y_next))
    #print(lista_next)
    return (lista_next)
#print(moves([0,7]))
#print(moves([7,0]))

# ova funkcija nam broji poteze dva skakača i dolazak na njegovo ciljano mjesto 
# ulaz je lista
# izlaz 
target = [2,3]  
#def count_moves(target):
knight_white = []
knight_white = moves([2,4])
print (knight_white)
knight_black = []
knight_black = moves([4,2])
print (knight_black)
"""if len(knight_white) == 4 and len(knight_black) == 4:
       if len(knight_white)> len(knight_black):
           return (knight_black)
       elif len(knight_black) > len(knight_white):
           return (knight_white)
       elif len(knight_white)== len(knight_black):
           return ("Nerijeseno")
    else:
        return ()"""
    
    
"""
f_u = open(filename_u,'r')
f_i = open(filename_i,'w')              
for line in f_u:
    line = line.replace("\n","")
    x = line.split(" ")
    f_i.write(str(obradi(x)) + "\n")
f_u.close()
f_i.close()
"""



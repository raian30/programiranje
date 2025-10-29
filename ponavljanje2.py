""""
moja_lista = [10,20,30]

prvi_element=moja_lista[0]

print(prvi_element)

moja_lista.append(40)

dio_lista = moja_lista[1:3]

print(dio_lista)


voce = ["jabuka", "banana", "kruska"]

print(voce[0])

voce.append("naranca")

print(voce)

"""
"""
ormar = [["majica","kapa","sal"],
         ["hlace","carape","remen"],
         ["jakna","cipele","cizme"]]
"""
""""
print(ormar[0][1])
print(ormar[1][1])
print(ormar[2][1])
"""

"""
for odjeca in ormar:
    print(odjeca[1])
"""
"""
for redak in ormar:
    for element in redak:
        print(element)

"""

def pronadji_broj(lista,broj):
    for element in lista:
        if element == broj:
            return print(f"broj {broj} se nalazi u listi")
    print(f"broj {broj} se ne nalazi u listi")

pronadji_broj([10,20,30,40,50], 30)
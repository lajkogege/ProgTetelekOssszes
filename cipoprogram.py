from Cipo import Cipo
import math

peldany1=Cipo("Nike",42)
peldany2=Cipo("Adidas",41)
peldany3=Cipo("Adidas",45)

cipok=[]
cipok.append(peldany1)
cipok.append(peldany2)
cipok.append(peldany3)

for i in range(0,len(cipok),1):
    nev:str=cipok[i].nev
    meret:int=cipok[i].meret
    print(f"{nev} ({meret})")
    
def cipo_atlag():
    osszeg:int=0
    for i in range (0,len(cipok),1):
        osszeg+=cipok[i].meret
    print(round (osszeg/len(cipok),3))
cipo_atlag()

def nagyobb42adidas():
    print("Van.e 42-nél nagyobb Adidas: ", end="")
    van:bool=False
    for i in range(0,len(cipok),1):
        if cipok[i].nev == "Adidas" and cipok[i].meret:
            van=True
    if van== True:
        print("Van ilyen")
    else:
        print("Nincs ilyen")
nagyobb42adidas()
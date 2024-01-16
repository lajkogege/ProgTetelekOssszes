def osszegzes_tetel():
    n:int=int(input("N= "))
    i:int=0
    ossz:int=0
    while not (n<0):
        n: int = int(input("N= "))
        i+=1
    for i in range(0,n+1,1):
        ossz+=i
    print(f" Az első {n} db természetes szám összege:{ossz}")

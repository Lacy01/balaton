import katona_alap
balaton=[]
for _ in range(3):
    telepules=input("Add meg egy település nevét! ")
    fekves=input("Add meg a fekvése (északi vagy déli)! ")
    lakos=input("Add meg a lakosság számát (o/n)! ")
    bala=Balaton(fekves,telepules,lakos,elotag)
    balaton.append(bala)
for balaton in bala:
    print(f'{balaton.település},egy {balaton.elotag} parti {balaton.lakos}')
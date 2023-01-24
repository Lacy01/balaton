def oldal(hazszam):
    if hazszam%2==0:
        return False
    else:
        return True

utca=None
while utca!='':
    utca=input("Add meg az utca nevét!: ")
    hazszam=int(input("Add meg a házszámot!: "))
    if oldal(hazszam)==True:
        print(f'A ház a(z){utca}-ban található a {hazszam} alatt és a bal oldalon található.')
    else:
                print(f'A ház a(z){utca}-ban található a {hazszam} alatt és a jobb oldalon található.')

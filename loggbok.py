loop = True

try:
    f = open("logg.txt", "r")
    f.close()
except:
    f = open("logg.txt", "w")
    f.close()

temp = []

while loop == True:

    print('[1] Visa alla loggar')
    print('[2] Ny logg')
    print('[3] Spara loggar till fil')
    print('[4] Avsluta')
    
    try:
        val = int(input('Val: '))
    except:
        val = 0
    
    if val == 1:

        f = open("logg.txt", "r")
        logg = f.read()
        print(logg)
        f.close()

    elif val == 2:

        nyLogg = input("Skriv loggen här: ")
        temp.append(nyLogg)

    elif val == 3:

        f = open("logg.txt", "a")
        for loggar in temp:
            f.write(loggar + "\n")
        f.close()
        temp = []

    elif val == 4:

        loop = False

    else:

        print("Du måste välja ett av alternativen")

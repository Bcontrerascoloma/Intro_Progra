nota = float(input("Nota? "))
if 1 <=nota <=3.9:
    print("R")
else:
    if 4<= nota <=4.9:
        print("A")
    else:
        if 5<= nota <=5.9:
            print("AD")
        else:
            if 6<= nota <=7:
                print("ADM")
            else:
                if nota < 1 or nota >7:
                    print("Te pillamos")

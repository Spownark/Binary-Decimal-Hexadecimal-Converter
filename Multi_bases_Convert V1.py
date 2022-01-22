#Multi bases converter with interface for user

#module inportation
import math

choise_function=""
while choise_function != "Q" and choise_function != "q" :
    print(" Conversion décimal vers binaire : 1 \n Conversion binaire vers décimal : 2 \n Conversion décimal vers hexadecimal : 3 \n Conversion hexadecimal vers décimal : 4 \n Conversion binaire vers hexadecimal : 5 \n Conversion hexadecimal vers binaire : 6 \n Quitter l'application : Q")
    choise_function = input(" Votre choix : ")

    #Convert a decimal to a binary
    if choise_function == "1":
        nb = int(input(" Entrer un nombre entier: "))
        result = ""
        while nb != 0 :
            r = str(nb % 2)
            result = r + result
            nb = nb // 2
        print(f" Conversion en binaire = {result}\n")

    #Convert a binary to a decimal
    elif choise_function == "2":
        nb = input(" Entrer un nombre binaire = ")
        k = 0
        result = 0
        while len(nb) > 0:
            b = int(nb[len(nb)-1:])
            result += b * math.pow(2, k)
            k += 1
            nb = nb[: len(nb)-1]
        print(f" Conversion en décimal = {result}\n")

    #Convert decimal to hexadecimal
    elif choise_function == "3":
         nb = int(input(" Entrer un nombre entier : "))
         result = ""
         hexa_values = {"0" : "0", "1" : "1", "2" : "2", "3" : "3", "4" : "4", "5" : "5", "6" : "6","7" : "7", "8" : "8", "9" : "9", "10" : "A", "11" : "B", "12" : "C","13" : "D", "14" : "E", "15" : "F"}
         while nb > 0:
             result = hexa_values[str(nb%16)] + result
             nb = nb //16
         print(f" Conversion en hexadecimal = {result}\n")
         

    #Convert hexadecimal to decimal
    elif choise_function == "4":
        hex = input(" Entrer un nombre hexadecimal: ")
        #if the user don't use uppercase character
        hex = hex.upper()
        result=int(hex, 16)
        print(f" Conversion en décimal = {result}\n")

    #Convert binary to hexadecimal
    elif choise_function == "5":
        nb = input(" Entrer un nombre binaire: ")
        decimal=int(nb,2)
        result=hex(decimal)
        #if the user enter a value with 0x
        if "0x" in result:
            result=result.replace("0x","")
        #show the result with uppercase character
        result = result.upper()
        print(f" Conversion en hexadecimal = {result}\n")

    #Convert hexadecimal to binary
    else:
        if choise_function == "6":
            nb = input(" Entrer un nombre hexadecimal: ")
            result=bin(int(nb, 16)).zfill(8)
            #if the user don't use uppercase character
            nb = nb.upper()
            #for don't show the value with 0b
            if "0b" in result:
                result=result.replace("0b","")
            print(f" Conversion en binaire = {result}\n")

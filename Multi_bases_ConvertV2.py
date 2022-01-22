#Multi bases converter with interface for user

#module inportation
import math
from tkinter import *

hexa_values = {"0" : "0", "1" : "1", "2" : "2", "3" : "3", "4" : "4", "5" : "5", "6" : "6","7" : "7", "8" : "8", "9" : "9", "10" : "A", "11" : "B", "12" : "C","13" : "D", "14" : "E", "15" : "F"}

#Convert a decimal to a binary
def decimal_to_binary(string):
    nb = int(string)
    result = ""
    while nb != 0 :
        r = str(nb % 2)
        result = r + result
        nb = nb // 2
    return result

#Convert a binary to a decimal
def binary_to_decimal(string):
    nb = int(string)
    k = 0
    result = 0
    while len(nb) > 0:
        b = int(nb[len(nb)-1:])
        result += b * math.pow(2, k)
        k += 1
        nb = nb[: len(nb)-1]
    return result


#Convert decimal to hexadecimal
def decimal_to_hexadecimal(string):
    nb = int(string)
    result = ""
    while nb > 0:
        result = hexa_values[str(nb%16)] + result
        nb = nb //16
    return result
         

#Convert hexadecimal to decimal
def hexadecimal_to_decimal(string):
    hex = (string)
                                                    #si l'utilisateur n'a pas utilisé de majuscule
    hex = hex.upper()
    result=int(hex, 16)
    return result

#Convert binary to hexadecimal
def binary_to_hexadecimal(string):
    nb = int(string)
    decimal=int(nb,2)
    result=hex(decimal)
                                                #si l'utilisateur à rentré une valeur avec 0x
    if "0x" in result:
        result=result.replace("0x","")
                                                #montrer le résultat avec des lettre majuscule
    result = result.upper()
    return result

#Convert hexadecimal to binary
def hexadecimal_to_binary(string):
    nb = (string)
    result=bin(int(nb, 16)).zfill(8)
                                                #si l'utilisateur n'a pas utilisé de majuscule
    nb = nb.upper()
                                                #pour ne pas montrer le resultat avec 0b au début
    if "0b" in result:
        result=result.replace("0b","")
    return result

#Graphic interface

def convert():
    value=e_value.get()
    x,y=start_base.get(),result_base.get()
    couple=(x,y)
    if couple==(1,2):
        res=decimal_to_binary(value)
    elif couple==(1,3):
        res=decimal_to_hexadecimal(value)
    elif couple==(2,1):
        res=binary_to_decimal(value)
    elif couple==(2,3):
        res=binary_to_hexadecimal(value)
    elif couple==(3,1):
        res=hexadecimal_to_decimal(value)
    elif couple==(3,2):
        res=hexadecimal_to_binary(value)
    else :
        res="Choissisez deux bases différentes !"
    fen2=Toplevel()
    Label(fen2,text="Resultat").pack()
    Label(fen2,text=res).pack()
    fen2.mainloop()

##Il faudrait mettre un message d'erreur si utilisateur utilise des lettre avec comme base de départ décimal et binaire mais je n'ai pas trouvé la solution à part de le péciser dans l'interface graphique

fen=Tk()
fen.title("Convertisseur Multi-Bases")
Label(fen,text="Saisissez la valeur\na convertir").pack(side=TOP)
e_value=Entry(fen)
e_value.pack(side=TOP)

f_left=Frame(fen)
f_left.pack(side=LEFT)
Label(f_left,text="Base de depart").pack()
start_base=IntVar()
Radiobutton(f_left,text="Decimal",variable=start_base,value=1,indicatoron=0,width=15).pack()
Radiobutton(f_left,text="Binaire",variable=start_base,value=2,indicatoron=0,width=15).pack()
Radiobutton(f_left,text="Hexadecimal",variable=start_base,value=3,indicatoron=0,width=15).pack()


f_right=Frame(fen)
f_right.pack(side=RIGHT)
Label(f_right,text="Base d'arrivee").pack()
result_base=IntVar()
Radiobutton(f_right,text="Decimal",variable=result_base,value=1,indicatoron=0,width=15).pack()
Radiobutton(f_right,text="Binaire",variable=result_base,value=2,indicatoron=0,width=15).pack()
Radiobutton(f_right,text="Hexadecimal",variable=result_base,value=3,indicatoron=0,width=15).pack()

b_convert=Button(fen,text="Convertir",command=convert)
b_convert.pack(side=BOTTOM)

fen.mainloop()

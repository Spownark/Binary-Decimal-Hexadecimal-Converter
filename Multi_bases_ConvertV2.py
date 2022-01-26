#Multi bases converter with interface for user
if __name__ == "__main__":
    
    #module importation
    import math
    from tkinter import *

    hexa_values = {"0" : "0", "1" : "1", "2" : "2", "3" : "3", "4" : "4", "5" : "5", "6" : "6","7" : "7", "8" : "8", "9" : "9", "10" : "A", "11" : "B", "12" : "C","13" : "D", "14" : "E", "15" : "F"}
    
    # Function #
    
    #Convert a decimal to a binary
    def decimal_to_binary(string):
        number = int(string)
        result = ""
        while number != 0 :
            remains = str(number % 2)
            result = remains + result
            number = number // 2
        return result

    #Convert a binary to a decimal
    def binary_to_decimal(string):
        number =(string)
        power_increment = 0
        result = 0
        while len(number) > 0:
            last_bit = int(number[len(number)-1:])
            result += last_bit * math.pow(2, power_increment)
            power_increment += 1
            number = number[: len(number)-1]
        return result


    #Convert decimal to hexadecimal
    def decimal_to_hexadecimal(string):
        number = int(string)
        result = ""
        while number > 0:
            result = hexa_values[str(number%16)] + result
            number = number //16
        return result
         

    #Convert hexadecimal to decimal
    def hexadecimal_to_decimal(string):
        hex = (string)
                                                    #if the user don't use uppercase character
        hex = hex.upper()
        result=int(hex, 16)
        return result

    #Convert binary to hexadecimal
    def binary_to_hexadecimal(string):
        number=(string)
        decimal=int(number,2)
        result=hex(decimal)
                                                #if the user enter a value with 0x
        if "0x" in result:
            result=result.replace("0x","")
                                                #show the result with uppercase character
        result = result.upper()
        return result

    #Convert hexadecimal to binary
    def hexadecimal_to_binary(string):
        number = (string)
        result=bin(int(number, 16)).zfill(8)
                                                #if the user don't use uppercase character
        number = number.upper()
                                                #Don't show the result with 0b
        if "0b" in result:
            result=result.replace("0b","")
        return result
    
    # Graphic interface #
    
    #Function for conversion with GUI
    def convert():
        value=entry_value.get()
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
            res="Choose two different types of base!"
        root2=Toplevel()
        Label(root2,text="Result").pack()
        Label(root2,text=res).pack()
        root2.mainloop()

    ##It would be necessary to put an error message if user uses letters with decimal and binary as starting base but I did not find the solution except to specify it in the graphic interface

    root=Tk()
    root.title("Multi bases converter")
    Label(root,text="Choose a value\nto convert").pack(side=TOP)
    entry_value=Entry(root)
    entry_value.pack(side=TOP)

    frame_left=Frame(root)
    frame_left.pack(side=LEFT)
    Label(frame_left,text="Start base").pack()
    start_base=IntVar()
    Radiobutton(frame_left,text="Decimal",variable=start_base,value=1,indicatoron=0,width=15).pack()
    Radiobutton(frame_left,text="Binary",variable=start_base,value=2,indicatoron=0,width=15).pack()
    Radiobutton(frame_left,text="Hexadecimal",variable=start_base,value=3,indicatoron=0,width=15).pack()


    frame_right=Frame(root)
    frame_right.pack(side=RIGHT)
    Label(frame_right,text="Result base").pack()
    result_base=IntVar()
    Radiobutton(frame_right,text="Decimal",variable=result_base,value=1,indicatoron=0,width=15).pack()
    Radiobutton(frame_right,text="Binary",variable=result_base,value=2,indicatoron=0,width=15).pack()
    Radiobutton(frame_right,text="Hexadecimal",variable=result_base,value=3,indicatoron=0,width=15).pack()

    button_convert=Button(root,text="Convert",command=convert)
    button_convert.pack(side=BOTTOM)

    root.mainloop()

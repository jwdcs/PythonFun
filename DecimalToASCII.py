# Python3 program designed to convert decimal values to ASCII format string
# Originally created in order to complete picoCTF challenge "Nice netcat..."
asci = ""
for i in range(int(input("Enter how many decimal values do you want to convert to ASCII: "))): 
    deci = int(input("Input the decimal to be converted: "))
    try:
        asci += chr(deci)
    except Exception as e:
        print("The previous value was not converted to ASCII")
        print("This is because the following exception has occurred:", e)
        
print("The conversion yields: ")
print(asci)

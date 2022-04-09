# Python3 program designed to convert hexadecimal string to ASCII format string
# Designed to explain and 
print("Note: remove the '0x' in the beginning, it is just a prefix to designate it is a hexadecimal value")
print("Further note: for best results, do not separate hexadecimal values with a space")
hexx = input("Enter the hexidecimal value to be converted to ASCII: ")
 
# initialize the ASCII code string as empty.
asci = ""
for i in range(0, len(hexx), 2):
    asci += chr(int(hexx[i : i + 2], 16))

print(asci)


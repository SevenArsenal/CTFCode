#Encryption or Discryption

ENC = "Guvf vf n irel fvzcyr Ebgngvba13 rapelcgvba. \n SYNT{EbgngvbaGuvegrra}"

#Shift position
Pos = -13

#Output
Discryption = ""

for char in list(ENC):

    ascii = ord(char)
    if ascii >=65 and ascii <=90:
        #do
        num = ascii -65
        shift_num = (num + Pos)%26
        discp_ascii = shift_num +65
        Discryption += chr(discp_ascii)                
    elif ascii >=97 and ascii <=122 :
        num = ascii -97
        shift_num = (num + Pos)%26
        discp_ascii = shift_num +97
        Discryption += chr(discp_ascii)              
    else:
        Discryption += char 
        
print("Discryption res = ")
print(Discryption)

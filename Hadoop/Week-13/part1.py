fileread=open("1985.txt","r")
filewrite=open("outputbyshivank.txt","w")
print("Extracting the values")
for line in fileread:
   longitude=line[34:41]
   qualitycode=line[63]
   temperature=line[87:92]
   if(temperature!='+9999'):
        filewrite.write(longitude+"\t"+temperature+"\t"+qualitycode+"\n")

print("Field Extraction completed and output file made")                                                                                                                                                                                                               ~                                                                                                                                                                                                                  ~                                                                 

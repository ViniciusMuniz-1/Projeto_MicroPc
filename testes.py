bin = "0011/0000/1000/0000/0000/0000/0000/0011"
bin = bin.split("/")
cont = 0
numhex = []
for num in bin:
    if(num == "0000"):
        numhex.append(num)

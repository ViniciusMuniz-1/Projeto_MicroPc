#Farei aqui um programa que rode em uma sequência de instruções na minha ULA. Essas sequências possuem
#um código cada uma, logo faz-se necessário declarar cada uma dessas intruções.


#Função que possui a função de transformar um número em binário para hexadecimal. 
                 #Entrada: lista em bin com os números separados em 4 casas cada um; 
                 #Saída: lista em hex
def bintohex(l): 
    for num in bin:
        if(num == "0000"):
            num = "0"
            numhex.append(num)
        elif(num == "0001"):
            num = "1"
            numhex.append(num)
        elif(num == "0010"):
            num = "2"
            numhex.append(num)
        elif(num == "0011"):
            num = "3"
            numhex.append(num)
        elif(num == "0100"):
            num = "4"
            numhex.append(num)
        elif(num == "0101"):
            num = "5"
            numhex.append(num)
        elif(num == "0110"):
            num = "6"
            numhex.append(num)
        elif(num == "0111"):
            num = "7"
            numhex.append(num)
        elif(num == "1000"):
            num = "8"
            numhex.append(num)
        elif(num == "1001"):
            num = "9"
            numhex.append(num)
        elif(num == "1010"):
            num = "a"
            numhex.append(num)
        elif(num == "1011"):
            num = "b"
            numhex.append(num)
        elif(num == "1100"):
            num = "c"
            numhex.append(num)
        elif(num == "1101"):
            num = "d"
            numhex.append(num)
        elif(num == "1110"):
            num = "e"
            numhex.append(num)
        elif(num == "1111"):
            num = "f"
            numhex.append(num)
    return numhex


#Bloco de código que abre o arquivo e coloca as instruções em uma variável
arqinstructions = open("intrucoes.txt")
instruction1 = arqinstructions.readlines()
instruction = arqinstructions.readlines()


#Linha de código que transforma em string e retira os colchetes e aspas, já que se tratava de uma lista antes
instruction = str(instruction).strip('[]').strip("''")


#Bloco de código que transforma a instrução em binário
bin = ""
for inst in instruction1:
    if(inst == "addi $8 $0 3"):
        bin = "0011/0000/1000/0000/0000/0000/0000/0011"
bin = bin.split("/")


#Abre o arquivo para transcrever as operações em hexadecimal, em seguida escreve o 
#número em hexadecimal em outro arquivo
arqhex = open("intructionshex.txt", "w+")
numhex = []
bintohex(numhex)
cont = 0
for num in bin:
    arqhex.write(numhex[cont])
    cont+=1
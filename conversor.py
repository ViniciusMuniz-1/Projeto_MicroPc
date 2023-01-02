#Farei aqui um programa que rode em uma sequência de instruções na minha ULA. Essas sequências possuem
#um código cada uma, logo faz-se necessário declarar cada uma dessas intruções.

arq = open("Projeto_MicroPc\intrucoes.txt")
instruction = arq.readlines()
string = str(instruction).strip('[]').strip("''")
string = string.split(" ")
for instructions in instruction:
    if(instructions == "addi $8 $0 3"):
        bin = "00110000100000000000000000000011"
    
ar2 = open("Projeto_MicroPc\intructionshex.txt", "w+")
for inst in instruction:
    ar2.write(hex)


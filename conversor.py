#Farei aqui um programa que rode em uma sequência de instruções na minha ULA. Essas sequências possuem
#um código cada uma, logo faz-se necessário declarar cada uma dessas intruções.

arq = open("Projeto_MicroPc\intrucoes.txt")
instruction = arq.readlines()
string = str(instruction).strip('[]')
string = string.split(" ")
for instructions in instruction:
    if(instructions == "addi"):
        hex = "001100"
    
ar2 = open("Projeto_MicroPc\intructionshex.txt", "w+")

for inst in instruction:
    ar2.write(inst)


#Farei aqui um programa que rode em uma sequência de instruções na minha ULA. Essas sequências possuem
#um código cada uma, logo faz-se necessário declarar cada uma dessas intruções.


#Função que possui a função de transformar um número em binário para hexadecimal. 
                 #Entrada: lista em bin com os números separados em 4 casas cada um; 
                 #Saída: lista em hex
# def bintohex(l): 
#     for num in bin:
#         if(num == "0000"):
#             num = "0"
#             numhex.append(num)
#         elif(num == "0001"):
#             num = "1"
#             numhex.append(num)
#         elif(num == "0010"):
#             num = "2"
#             numhex.append(num)
#         elif(num == "0011"):
#             num = "3"
#             numhex.append(num)
#         elif(num == "0100"):
#             num = "4"
#             numhex.append(num)
#         elif(num == "0101"):
#             num = "5"
#             numhex.append(num)
#         elif(num == "0110"):
#             num = "6"
#             numhex.append(num)
#         elif(num == "0111"):
#             num = "7"
#             numhex.append(num)
#         elif(num == "1000"):
#             num = "8"
#             numhex.append(num)
#         elif(num == "1001"):
#             num = "9"
#             numhex.append(num)
#         elif(num == "1010"):
#             num = "a"
#             numhex.append(num)
#         elif(num == "1011"):
#             num = "b"
#             numhex.append(num)
#         elif(num == "1100"):
#             num = "c"
#             numhex.append(num)
#         elif(num == "1101"):
#             num = "d"
#             numhex.append(num)
#         elif(num == "1110"):
#             num = "e"
#             numhex.append(num)
#         elif(num == "1111"):
#             num = "f"
#             numhex.append(num)
#     return numhex


#Bloco de código que transforma a instrução em binário
def insttobin(instruction):
    for inst in instruction:
        if inst == "addi":
            instbin.append("001000")
        elif inst == "ori":
            instbin.append("001101")
        elif inst == "xori":
            instbin.append("001110")
        elif inst=="andi":
            instbin.append("001100")
        elif inst=="addiu":
            instbin.append("001001")
        elif inst=="and":
            instbin.append("100100")
        elif inst=="or":
            instbin.append("100101")
        elif inst=="xor":
            instbin.append("100110")
        elif inst=="nor":
            instbin.append("100111")
        elif inst=="add":
            instbin.append("100000")
        elif inst=="sub":
            instbin.append("100010")
        elif inst=="shl":
            instbin.append("000000")
        elif inst=="shr":
            instbin.append("000001")
        elif inst=="sar":
            instbin.append("000011")
        elif inst=="slt":
            instbin.append("101010")
        elif inst=="beq":
            instbin.append("000100")
        elif inst=="bne":
            instbin.append("000101")

def verificareg(instruction):
    for inst in instruction:
        match inst:
            case "$0":
                instbin.append("00000")
            case "$1":
                instbin.append("00001")
            case "$2":
                instbin.append("00010")
            case "$3":
                instbin.append("00011")
            case "$4":
                instbin.append("00100")
            case "$5":
                instbin.append("00101")
            case "$6":
                instbin.append("00110")
            case "$7":
                instbin.append("00111")
            case "$8":
                instbin.append("01000")
            case "$9":
                instbin.append("01001")
            case "$10":
                instbin.append("01010")
            case "$11":
                instbin.append("01011")
            case "$12":
                instbin.append("01100")
            case "$13":
                instbin.append("01101")
            case "$14":
                instbin.append("01110")
            case "$15":
                instbin.append("01111")
            case "$16":
                instbin.append("10000")
            case "$17":
                instbin.append("10001")
            case "$18":
                instbin.append("10010")
            case "$19":
                instbin.append("10011")
            case "$20":
                instbin.append("10100")
            case "$21":
                instbin.append("10101")
            case "$22":
                instbin.append("10110")
            case "$23":
                instbin.append("10111")
            case "$24":
                instbin.append("11000")
            case "$25":
                instbin.append("11001")
            case "$26":
                instbin.append("11010")
            case "$27":
                instbin.append("11011")
            case "$28":
                instbin.append("11100")
            case "$29":
                instbin.append("11101")
            case "$30":
                instbin.append("11110")
            case "$31":
                instbin.append("11111")

instbin=[]

#Bloco de código que abre o arquivo e coloca as instruções em uma variável
arqinstructions = open("intrucoes.txt")
instruction = arqinstructions.readlines()


#Linha de código que transforma em string e retira os colchetes e aspas, já que se tratava de uma lista antes
instruction = str(instruction).strip('[]').strip("''")

#Abre o arquivo para transcrever as operações em hexadecimal, em seguida escreve o 
#número em hexadecimal em outro arquivo
arqhex = open("intructionshex.txt", "w+")
numhex = []
cont = 0
for num in bin:
    arqhex.write(numhex[cont])
    cont+=1
 
hex(numhex)
#Farei aqui um programa que rode em uma sequência de instruções na minha ULA. Essas sequências possuem
#um código cada uma, logo faz-se necessário declarar cada uma dessas intruções.


#Função que possui a função de transformar um número em binário para hexadecimal. 
                 #Entrada: lista em bin com os números separados em 4 casas cada um; 
                 #Saída: lista em hex

#Bloco de código que transforma a instrução em binário
def insttobin(instruction):
    for inst in instruction:
        match inst:
            case "addi":
                instbin.append("001000")
                break
            case "ori":
                instbin.append("001101") 
                break
            case "xori":
                instbin.append("001110")
                break
            case "andi":
                instbin.append("001100")
                break
            case "addiu":
                instbin.append("001001")
                break
            case "and":
                instbin.append("100100")
                break
            case "or":
                instbin.append("100101")
                break
            case "xor":
                instbin.append("100110")
                break
            case "nor":
                instbin.append("100111")
                break
            case "add":
                instbin.append("100000")
                break
            case "sub":
                instbin.append("100010")
                break
            case "shl":
                instbin.append("000000")
                break
            case "shr":
                instbin.append("000001")
                break
            case "sar":
                instbin.append("000011")
                break
            case "slt":
                instbin.append("101010")
                break
            case "beq":
                instbin.append("000100")
                break
            case "bne":
                instbin.append("000101")
                break

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


#Bloco de código que abre o arquivo e coloca as instruções em uma variável

arquivo = open("Projeto_MicroPc/intrucoes.txt")
instruction = arquivo.readlines()
string = str(instruction).strip('[]').strip("''")
string = string.split(" ")
instbin=[]
insttobin(string)
verificareg(string)
numbin = "{:016d}".format(int(bin(int(string[3])).strip("0b")))
instbin.append(numbin)
instbin.insert(0, "0b")
separator = ''
result = [separator.join(instbin)]
result = str(result).strip('[]').strip("''")
bin = int(result,2)


#Abre o arquivo para transcrever as operações em hexadecimal, em seguida escreve o 
#número em hexadecimal em outro arquivo
arqhex = open("intructionshex.txt", "w+")
print(hex(bin))
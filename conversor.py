#https://docs.google.com/document/d/1R7723_xGjHCnNPqFmIiZDQS5AbxTrvVQ7oMJaBG_S5o/edit - Guia para entender o sistema

#Farei aqui um programa que rode em uma sequência de instruções na minha ULA. Essas sequências possuem
#um código cada uma, logo faz-se necessário declarar cada uma dessas intruções.


#Função que possui a função de transformar um número em binário para hexadecimal. 
                 #Entrada: lista em bin com os números separados em 4 casas cada um; 
                 #Saída: lista em hex

#Bloco de código que transforma a instrução em binário
def verificaop(instruction):
        match instruction:
            case "addi":
                instbin.append("001000")
            case "ori":
                instbin.append("001101") 
            case "xori":
                instbin.append("001110")
            case "andi":
                instbin.append("001100")
            case "addiu":
                instbin.append("001001")
            case "and":
                instbin.append("100100")
            case "or":
                instbin.append("100101")
            case "xor":
                instbin.append("100110")
            case "nor":
                instbin.append("100111")
            case "add":
                instbin.append("100000")
            case "sub":
                instbin.append("100010")
            case "shl":
                instbin.append("000000")
            case "shr":
                instbin.append("000001")
            case "sar":
                instbin.append("000011")
            case "slt":
                instbin.append("101010")
            case "beq":
                instbin.append("000100")
            case "bne":
                instbin.append("000101")

def verificareg(instruction):
    match instruction:
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

def casoopcode(instruction):
     #op rega regb value
        verificaop(instruction[0]) #verifica a operação
        verificareg(instruction[1]) #verifica primeiro registrador
        verificareg(instruction[2]) #verifica segundo registrador
        if "-" in instruction[3]:
            b = "1"
            instruction[3] = instruction[3].replace("-","")
            numbin = bin(~int(instruction[3]))
            numbin = numbin.replace("-", "")
            sub = bin(int(numbin,2) - int(b, 2))
            imm = sub.replace("0b","")
            imm = imm.rjust(16, "1")
            imm = imm.replace("-", "")
        else:
            imm = "{:016d}".format(int(bin(int(instruction[3])).replace("0b","")))
        instbin.append(imm)

def casofunction(instruction):
    #rega #regb #regc #op
    if instruction[0] == "shl" or instruction[0] == "shr" or instruction[0] == "sar":
        instbin.append("000000") #adiciona valor 0 ao opcode
        verificareg(instruction[1]) #verifica reg 1
        verificareg(instruction[1]) #verifica reg 2
        verificareg(instruction[2]) #verifica reg 3
        sa = "{:05d}".format(int(bin(int(instruction[3])).replace("0b","")))
        instbin.append(sa)
        verificaop(instruction[0]) #add instrução
    else:
        instbin.append("000000") #adiciona valor 0 ao opcode
        verificareg(instruction[1]) #verifica reg 1
        verificareg(instruction[2]) #verifica reg 2
        verificareg(instruction[3]) #verifica reg 3
        instbin.append("00000") #verifica sa
        verificaop(instruction[0]) #add instrução


#Bloco de código utilizado para abrir a seleção de arquivos
import sys
import PySimpleGUI as sg
from tkinter import Button, Tk
from tkinter.filedialog import askopenfilename

janela_padrao = Tk().withdraw()

#Criação do layout interface
sg.theme('Dark Grey 13')
layout = [  [sg.Image("unnamed.png"), sg.Text('Converta Assembly para Hexadecimal aqui:')],
            [sg.Button('Converter trivialmente',size=(10,5),font = ("Comic Sans", 10)),  sg.Button('Não converter :(',size=(10,5),font = ("Comic Sans", 10))]],

# Cria a janela
window = sg.Window('Conversor', layout,size=(300, 200))
# Loop de eventos
while True:
    event, values = window()
    if event == sg.WIN_CLOSED or event == 'Não converter :(': # if user closes window or clicks cancel
        sys.exit()
    caminho_do_arquivo = askopenfilename(filetypes = (("Arquivos de texto", "*.txt"), ("Arquivos csv", "*.csv")))
    nome = sg.popup_get_text("Digite o nome do arquivo")
    break
window.close()


valuedec=[]
instruction=[]
separator = ''
cont = 0

#Bloco de código que abre o arquivo e coloca as instruções em uma variável
with open(caminho_do_arquivo, encoding='latin_1') as arquivo:
    for line in arquivo:
        cont+=1
        instbin=[]
        line = line.replace("\n", "")
        instruction.append(line)
        instruction = ' '.join(map(str, instruction)).split(" ")

        if ("i" in instruction[0]) or (instruction[0]=="beq") or (instruction[0]=="bne"): #CASO DO OPCODE COMO OPERADOR
           casoopcode(instruction)
        else: #CASO DO FUNCTION COMO OPERADOR
            casofunction(instruction)
        instbin.insert(0, "0b")

        #Transformando para decimal
        instbin = [separator.join(instbin)]
        instbin = str(instbin).strip('[]').strip("''")
        valuedec.append(int(instbin,2))

        #limpa a 1º linha de instrução para fazer a próxima
        instruction.clear()


valuehex=[]
for i in range(0,cont):
    valuehex.append(hex(valuedec[i]).replace("0x", "") + "\n")

nome = nome+".txt"
arqhex = open(nome, 'w')
arqhex.write("v2.0 raw\n")
arqhex.writelines(valuehex)
arqhex.close()
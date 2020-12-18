from tkinter import *
import threading
import time
import socket

def tremCinza(janela, canvas):
    global L1
    global L2
    global L3
    global L4

    trem = canvas.create_rectangle(5,5, 35, 35, fill="gray")

    while 1:
        if L2 < 9:
            canvas.move(trem,20,0)
            L2 = L2 + 1
        else:
            if L3 < 9:
                if L3 == 0:
                    print("Bloqueia L3")
                    mL3L8.acquire()
                canvas.move(trem,0,20)
                L3 = L3 + 1    
            else:
                if L3 == 9:
                    print("Libera L3")
                    mL3L8.release()
                    L3 = 100
                if L4 < 9:
                    if L4 == 0:
                        print("Bloqueia L4")
                        mL4L16.acquire()
                    canvas.move(trem, -20, 0)
                    L4 = L4 + 1
                else:
                    if L4 == 9:
                        print("Libera L4")
                        mL4L16.release()
                        L4 = 100
                    if L1 < 9:
                        canvas.move(trem, 0, -20)
                        L1 = L1 + 1
                    else:
                        L1, L2, L3, L4 = 0, 0, 0, 0
        
        time.sleep(n1)

def tremVermelho(janela, canvas):
    global L5
    global L6
    global L7
    global L8

    trem = canvas.create_rectangle(215,5, 245, 35, fill="red")
    while 1:
        if L7 < 9:
            canvas.move(trem,20,0)
            L7 = L7 + 1
        else:
            if L5 < 9:
                if L5 == 0:
                    print("Bloqueia L5")
                    mL5L12.acquire()
                canvas.move(trem,0,20)
                L5 = L5 + 1
            else:
                if L5 == 9:
                    print("Libera L5")
                    mL5L12.release()
                    L5 = 100                
                if L6 < 9:
                    if L6 == 0:
                        print("Bloqueia L6")
                        mL6L17.acquire()
                    canvas.move(trem,-20,0)
                    L6 = L6 + 1
                else:
                    if L6 == 9:
                        print("Libera L6")
                        mL6L17.release()
                        L6 = 100
                    if L8 < 9:
                        if L8 == 0:
                            print("Bloqueia L8")
                            mL3L8.acquire()
                        canvas.move(trem,0,-20)
                        L8 = L8 + 1
                    else:
                        if L8 == 9:
                            print("Libera L8")
                            mL3L8.release()
                            L8 = 100
                        L5, L6, L7, L8 = 0, 0, 0, 0
        time.sleep(n2)

def tremVerde(janela, canvas):
    global L9
    global L10
    global L11
    global L12

    trem = canvas.create_rectangle(425,5, 455, 35, fill="green")
    while 1:
        if L9 < 9:
            canvas.move(trem,20,0)
            L9 = L9 + 1
        else:
            if L10 < 9:
                canvas.move(trem,0,20)
                L10 = L10 + 1
            else:
                if L11 < 9:
                    if L11 == 0:
                        print("Bloqueia L11")
                        mL11L18.acquire()
                    canvas.move(trem,-20,0)
                    L11 = L11 + 1
                else:
                    if L11 ==9:
                        print("Libera L11")
                        mL11L18.release()
                        L11 = 100
                    if L12 < 9:
                        if L12 == 0:
                            print("Bloqueia L12")
                            mL5L12.acquire()
                        canvas.move(trem,0,-20)
                        L12 = L12 + 1
                    else:
                        if L12 == 9:
                            print("Libera L12")
                            mL5L12.release()
                            L12 = 100
                        L9, L10, L11, L12 = 0, 0, 0, 0
        time.sleep(n3)

def tremAzul(janela, canvas):
    global L13
    global L14
    global L15
    global L16
    global L17
    global L18

    trem = canvas.create_rectangle(5,215, 35, 245, fill="blue")
    while 1:
        if L16 < 9:
            if L16 == 0:
                print("Bloqueia L16")
                mL4L16.acquire()
            canvas.move(trem,20,0)
            L16 = L16 + 1
        else:
            if L16 == 9:
                print("Libera L16")
                mL4L16.release()
                L16 = 100
            if L17 < 10:
                if L17 == 0:
                    print("Bloqueia L17")
                    mL6L17.acquire()
                canvas.move(trem,20,0)
                L17 = L17 + 1
            else:
                if L17 == 10:
                    print("Libera L17")
                    mL6L17.release()
                    L17 = 100
                if L18 < 11:
                    if L18 == 0:
                        print("Bloqueia L18")
                        mL11L18.acquire()
                    canvas.move(trem,20,0)
                    L18 = L18 + 1
                else:
                    if L18 == 11:
                        print("Libera L18")
                        mL11L18.release()
                        L18 = 100
                    if L13 <9:
                        canvas.move(trem,0,20)
                        L13 = L13 + 1
                    else:
                        if L14 < 30:
                            canvas.move(trem,-20,0)
                            L14 = L14 + 1
                        else:
                            if L15 < 9:
                                canvas.move(trem,0,-20)
                                L15 = L15 + 1
                            else:
                                L13, L14, L15, L16, L17, L18 = 0, 0, 0, 0, 0, 0
                        
        time.sleep(n4)    

def velocidades_cliente(janela, canvas):
    global n1
    global n2
    global n3
    global n4
    
    print('Na thread')
    while True:
        # Quantidadde de dados que o server espera receber
        data, adress = server.recvfrom(1024)
        print(data)
        n1 = float(data.split()[0])
        n2 = float(data.split()[1])
        n3 = float(data.split()[2])
        n4 = float(data.split()[3])
    
# Nome da máquina que está executando o arquivo
HOST = 'localhost'
# Porta 
PORT = 5000

#Objeto socket, AF_INIET (família do endereço)
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Vincula o socket ao port number
server.bind((HOST, PORT))
print('Server Started')

janela = Tk()
janela.title('Dinâmica dos Trêns (Server)')
janela.geometry('1200x1200')

widget = Canvas(janela, width=1000, height=1000)
widget.pack()

e1 = Entry(janela)
e1.pack()

n1 = 1
n2 = 1
n3 = 1
n4 = 1
L1, L2, L3, L4 = 0, 0, 0, 0
L5, L6, L7, L8 = 0, 0, 0, 0
L9, L10, L11, L12 = 0, 0, 0, 0
L13, L14, L15, L16, L17, L18 = 0, 0, 0, 0, 0, 0

trilhoCina = widget.create_rectangle(10, 10, 210, 210, outline="gray", width="5")
trilhoVermelho = widget.create_rectangle(220, 10, 420, 210, outline="red", width="5")
trilhoVerde = widget.create_rectangle(430, 10, 630, 210, outline="green", width="5")
trilhoAzul = widget.create_rectangle(10, 220, 630, 420, outline="blue", width="5")


mL3L8 = threading.Lock()
mL5L12 = threading.Lock()
mL4L16 = threading.Lock()
mL6L17 = threading.Lock()
mL11L18 = threading.Lock()

t1 = threading.Thread(target=tremCinza, args=[janela, widget])
t2 = threading.Thread(target=tremVermelho, args=[janela, widget])
t3 = threading.Thread(target=tremVerde, args=[janela, widget])
t4 = threading.Thread(target=tremAzul, args=[janela, widget])
t5 = threading.Thread(target=velocidades_cliente, args=[janela, widget])

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
    #data, endereco = server.recvfrom(1024)
    #print(data)

janela.mainloop()

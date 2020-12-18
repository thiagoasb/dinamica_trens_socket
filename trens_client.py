from tkinter import *
import threading
import time
import socket


HOST = 'localhost' #127.0.0.1
PORT = 5000

server = (HOST, PORT)

conexao = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def controleVelocidade():
    global n1
    global n2
    global n3
    global n4
    n1 = e1.get()
    n2 = e2.get()
    n3 = e3.get()
    n4 = e4.get()

    message = n1 + ' ' + n2 + ' ' + n3 + ' ' + n4
    print(message)
    conexao.sendto(message.encode('utf-8'), (HOST, PORT))
    
janela = Tk()
janela.title('Dinâmica dos Trêns (Client)')
janela.geometry('1200x400')

widget = Canvas(janela, width=1000, height=1000)
widget.pack()

e1 = Entry(janela)
e1.pack()

e1 = Entry()
e1.insert(0, 'Trem Cinza')
e2 = Entry()
e2.insert(0, 'Trem Vermelho')
e3 = Entry()
e3.insert(0, 'Trem Verde')
e4 = Entry()
e4.insert(0, 'Trem Azul')

b = Button(0, text="submit", command=controleVelocidade)

widget.create_window(20, 60, window=e1)
widget.create_window(20, 100, window=e2)
widget.create_window(20, 140, window=e3)
widget.create_window(20, 180, window=e4)
widget.create_window(20, 220, window=b)

#t5 = threading.Thread(target=controleVelocidade, args=[janela, widget])
#t5.start()

janela.mainloop()

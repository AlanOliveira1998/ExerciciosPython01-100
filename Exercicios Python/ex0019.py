#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seu seno, cosse e tangente
import math
import PySimpleGUI as sg
class codigo:
    n = int(input('Digite o valor do seu angulo:'))
    se = math.sin(math.radians(n))
    co = math.cos(math.radians(n))
    ta = math.tan(math.radians(n))
    print('O valo do seno corresponde a {:.2f},\n do coseno {:.2f} \n e da tangente {:.2f}'.format(se, co, ta))

class Telapython:
    def __init__(self):
        #layout
        layout = [ 
            sg.Text('Digite o valor do seu angulo')
        ]
        #janela
        janela = [
            sg.Window('Conversosr trigonométrico').layout(layout)
        ]
        #Extração de dados 
            self.values = janela.Read()
    def iniciar(self):
        print(self.values)
    tela = Telapython
    tela.iniciar()
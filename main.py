from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

Window.size = (600, 600)
Window.clearcolor = '#216770'

class MyGcdAndLcm(App):
    def add_data(self, instance): #считает и добавляет данные в поля
        b = []
        a = list(map(int, (self.gl0.text).split()))
        c = set()
        d = 1
        for i in range(len(a)):  # считывает все делетели каждого числа
            for j in range(1, max(a)):
                if a[i] % j == 0:
                    b.append(j)
        for i in range(len(b)):  # считает количество повторений каждого делителя
            if b.count(b[i]) == len(a):
                c.add(b[i])
        for i in range(len(a)):  # считает НОК
            d *= a[i]

        self.gl1.text = str(c) #выводит общие делители
        self.gl2.text = str(max(c))    #выводит НОД
        self.gl3.text = str(d // max(c))  #выводит НОК


    def build(self): #создает интерфейс
        gl = GridLayout(cols=2, rows=4)

        self.gl0 = TextInput(text = '', multiline=False, background_color='#5A7D82', background_normal = '', foreground_color=(1, 1, 1, 1))
        gl.add_widget(self.gl0)
        gl.add_widget(Button(text='Подсчитать', background_color='#07575B', background_normal = '', on_press=self.add_data))
        gl.add_widget(Label(text='Общие делители:'))
        self.gl1 = Label(text='')
        gl.add_widget(self.gl1)
        gl.add_widget(Label(text='НОД:'))
        self.gl2 = Label(text='')
        gl.add_widget(self.gl2)
        gl.add_widget(Label(text='НОК:'))
        self.gl3 = Label(text='')
        gl.add_widget(self.gl3)

        return gl


if __name__ == '__main__':
    MyGcdAndLcm().run()








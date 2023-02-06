import kivy
from kivy.app import App
from kivy.uix.label import Label

from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        layout = GridLayout(cols=2)
    
        btn1 = Button(text='Hello 1')
        btn2 = Button(text='Hello 2')
        btn3 = Button(text='Hello 3')
        btn4 = Button(text='Hello 4')

        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4)

        return layout
        
if __name__ == '__main__':
    MyApp().run()

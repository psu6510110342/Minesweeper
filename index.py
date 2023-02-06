import kivy
from kivy.app import App
from kivy.uix.label import Label

from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        layout = GridLayout(cols=8)

        for i in range(1,65):
            layout.add_widget(Button(text='test'))

        return layout
        
if __name__ == '__main__':
    MyApp().run()

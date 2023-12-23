from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
# from kivy.core import text
# from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout

Window.clearcolor = (0,0,0,0)   

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation = "vertical")
        label = Label(text="Hello fareed", font_size ="120sp", bold =True, color = (1,0,0,1))
        btn = Button(text = "click me ")
        img = Image(source = 'ks.jpg')
        layout.add_widget(label)
        layout.add_widget(img)
        layout.add_widget(btn)
        return layout
    
MyApp().run()
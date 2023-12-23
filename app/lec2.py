from kivy.uix.textinput import TextInput
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class tut2(App):
    def build(self):
        layout = BoxLayout(orientation="vertical",padding = 200, spacing =20)
        self.lay1 = TextInput(text= "enter your email")
        self.lay2 = TextInput(text = "enter your password")
        self.submit = Button(text = "login", on_press = self.submitbtn)
        layout.add_widget(self.lay1)
        layout.add_widget(self.lay2)
        layout.add_widget(self.submit)
        return layout
    def submitbtn(self,obj):
        print(f"your email is {self.lay1.text}")
        print (f"your password is {self.lay2.text}")
tut2().run()
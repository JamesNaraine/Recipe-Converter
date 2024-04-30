import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.lang import Builder

class Window1(Screen):
    def button_pressed(self, button_number):
        print(f"Button {button_number} pressed")

class Window2(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("ButtonPresser.kv")


class ButtonPresser(App):
    def build(self):
        return kv
    

if __name__ == "__main__":
    ButtonPresser().run()




import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix. floatlayout import FloatLayout
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.graphics import Line
from kivy.app import App 
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


class MainWindow(Screen):
    pass

class SecondWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass



kv = Builder.load_file("KivyTouch.kv")

import sys
from pathlib import Path

parent_dir = str(Path(__file__).resolve().parent.parent)
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

from conversion import main_loop


class Touch(Widget):

    def __init__(self, **kwargs):
        super(Touch,self).__init__(**kwargs)

        with self.canvas:
            Line(points = (20,30,400,500,600,69))
            Color(1,0,0,.5, mode = "rgba")
            self.rect = Rectangle(pos=(0,0), size =(50,50))
            Color(1,1,0,.5, mode = "rgba")
            self.rect = Rectangle(pos=(200,300), size =(500,300))

        btn = ObjectProperty(None)


        super().__init__(**kwargs)
        # self.btn.background_normal = ''  # Use background_color instead of an image
        # self.btn.background_color = (0, 0, 1, 0.6)  # Grey color in RGBA

    def on_touch_down(self, touch):
        # if self.btn and self.collide_point(*touch.pos):
        #     self.btn.opacity = 0.5
        self.rect.pos = touch.pos
        print("Mouse Down", touch)
        return super().on_touch_down(touch)
    
    def on_touch_up(self, touch):
        # if self.btn and self.collide_point(*touch.pos):
        #     self.btn.opacity = 1

        print("Mouse Up", touch)
        return super().on_touch_up(touch)

    def on_touch_move(self, touch):
        self.rect.pos = touch.pos
        print("mouse move", touch)

class KivyTouch(App):
    def build(self):
#         ##return Label(text="IM RICH", font_size=300, color="brown")
        # return Touch()
        return kv
    

if __name__ == "__main__":
    KivyTouch().run()




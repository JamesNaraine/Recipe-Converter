import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix. floatlayout import FloatLayout

import sys
from pathlib import Path

parent_dir = str(Path(__file__).resolve().parent.parent)
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

from conversion import main_loop


class Touch(Widget):
    btn = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.btn.background_normal = ''  # Use background_color instead of an image
        self.btn.background_color = (0, 0, 1, 0.6)  # Grey color in RGBA

    def on_touch_down(self, touch):
        if self.btn and self.collide_point(*touch.pos):
            self.btn.opacity = 0.5
            print("Mouse Down", touch)
        return super().on_touch_down(touch)
    
    def on_touch_up(self, touch):
        if self.btn and self.collide_point(*touch.pos):
            self.btn.opacity = 1

            print("Mouse Up", touch)
        return super().on_touch_up(touch)

    def on_touch_move(self, touch):
        print("mouse move", touch)

class KivyTouch(App):
    def build(self):
#         ##return Label(text="IM RICH", font_size=300, color="brown")
        return Touch()
    

if __name__ == "__main__":
    KivyTouch().run()




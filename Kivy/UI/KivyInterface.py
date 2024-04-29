import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix. floatlayout import FloatLayout


from kivy.uix.screenmanager import ScreenManager, Screen
import sys
from pathlib import Path

parent_dir = str(Path(__file__).resolve().parent.parent.parent)
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

from conversion import main_loop

class MyGrid(Widget):
    input = ObjectProperty(None)
    output = ObjectProperty(None)

    def btn(self):
        inputtext = str(self.input.text)
        preTranslatedOutput = main_loop(True,inputtext)
        # self.output.text = preTranslatedOutput
        print(preTranslatedOutput)
        self.input.text = ""


class MainWindow(Screen):
    pass

class LoadingWindow(Screen):
    pass

class OutputWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass


from kivy.lang import Builder

kv = Builder.load_file("my.kv")

import sys
from pathlib import Path

parent_dir = str(Path(__file__).resolve().parent.parent.parent)
if parent_dir not in sys.path:
    sys.path.append(parent_dir)


from conversion import main_loop


inputtext = "lukethisdoesn'twork"
output = ""


    



class MyApp(App):
    def build(self):
        return kv
    

if __name__ == "__main__":
    MyApp().run()




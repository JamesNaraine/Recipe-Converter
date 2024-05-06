import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty


from kivy.uix.screenmanager import ScreenManager, Screen
import sys
from pathlib import Path

parent_dir = str(Path(__file__).resolve().parent.parent.parent)
if parent_dir not in sys.path:
    sys.path.append(parent_dir)


output_text = ""

from conversion import main_loop

class MainWindow(Screen):
    input_text = ObjectProperty(None)
    

    def btn(self):
        input_text = str(self.input_text.text)
        preTranslatedOutput = main_loop(True,input_text)
        print(preTranslatedOutput)
        self.manager.get_screen("output").output_text = preTranslatedOutput
        self.manager.current = "output"
        self.input_text.text = ""

class LoadingWindow(Screen):
    pass

class OutputWindow(Screen):
    output_text = StringProperty("")

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



output = ""


    



class MyApp(App):
    def build(self):
        return kv
    

if __name__ == "__main__":
    MyApp().run()




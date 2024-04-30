import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix. floatlayout import FloatLayout
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
    input = ObjectProperty(None)
    output = StringProperty('') 

    def btn(self):
        inputtext = str(self.input.text)
        preTranslatedOutput = main_loop(True,inputtext)
        # self.output.text = preTranslatedOutput
        print(preTranslatedOutput)
        output_text = preTranslatedOutput
        self.output = preTranslatedOutput
        self.input.text = ""

class LoadingWindow(Screen):
    pass

class OutputWindow(Screen):
    output = ObjectProperty(None)
    def output_text_display(self):
        print(self.manager.get_screen('main').output)
        return 

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




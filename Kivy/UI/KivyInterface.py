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

import threading
from kivy.core.clipboard import Clipboard
from kivy.uix.screenmanager import ScreenManager, Screen
import sys
from pathlib import Path
from kivy.uix.dropdown import DropDown


parent_dir = str(Path(__file__).resolve().parent.parent.parent)
if parent_dir not in sys.path:
    sys.path.append(parent_dir)


output_text = ""

from conversion import main_loop

class MainWindow(Screen):
    input_text = ObjectProperty(None)
    measurement_type = True
    measurement_button_text = StringProperty("Measurement \n Imperial to Metric")
    
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        self.measurement_dropdown = DropDown()

        imperial_btn = Button(text="Imperial to Metric", size_hint_y = None)
        metric_btn = Button(text="Metric to Imperial", size_hint_y = None)

        imperial_btn.bind(on_release= lambda btn: self.select_measurement("Imperial"))
        metric_btn.bind(on_release= lambda btn: self.select_measurement("Metric"))

        self.measurement_dropdown.add_widget(imperial_btn)
        self.measurement_dropdown.add_widget(metric_btn)

    def open_measurement_dropdown(self):
        self.measurement_dropdown.open(self.ids.measurement_button)

    def select_measurement(self, text):
        if text == "Imperial":
            self.measurement_type = True
            self.measurement_button_text = "Measurement \n Imperial to Metric"
            print("Imperial to Metric")
        elif text == "Metric":
            self.measurement_type = False
            self.measurement_button_text = "Measurement \n Metric to Imperial"
            print("Metric to Imperial")
        else:
            print("possible error: selct measurement neither imperial or metric")





    

    def btn(self):
        input_text = str(self.input_text.text)
        print(f"imperial {self.measurement_type}, input text = {input_text}")
        preTranslatedOutput = main_loop(self.measurement_type,input_text)
        print(preTranslatedOutput)
        self.manager.get_screen("output").output_text = preTranslatedOutput
        self.manager.current = "output"
        self.input_text.text = ""
        

class LoadingWindow(Screen):
    pass

class OutputWindow(Screen):
    output_text = StringProperty("")

    def copy(self):
        Clipboard.copy(self.output_text)
    
    
        


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




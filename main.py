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

from plyer import camera
from kivy.core.clipboard import Clipboard
from kivy.uix.screenmanager import ScreenManager, Screen
import sys
from pathlib import Path
from kivy.uix.dropdown import DropDown
from kivy.uix.image import Image


parent_dir = str(Path(__file__).resolve().parent.parent.parent)
if parent_dir not in sys.path:
    sys.path.append(parent_dir)


output_text = ""

from conversion import main_loop
from Translator import Translating

class MainWindow(Screen):
    input_text = ObjectProperty(None)
    measurement_type = True
    measurement_button_text = StringProperty("Measurement \nImperial to Metric")
    target_language = StringProperty("en")
    language_button_text = StringProperty("Target Language \nEnglish")
    source_language_target = StringProperty("en")
    source_language_button_text = StringProperty("Source Language \nEnglish")
    
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        self.measurement_dropdown = DropDown()

        imperial_btn = Button(text="Imperial to Metric", size_hint_y = None)
        metric_btn = Button(text="Metric to Imperial", size_hint_y = None)

        imperial_btn.bind(on_release= lambda btn: self.select_measurement("Imperial"))
        metric_btn.bind(on_release= lambda btn: self.select_measurement("Metric"))

        self.measurement_dropdown.add_widget(imperial_btn)
        self.measurement_dropdown.add_widget(metric_btn)

        self.language_dropdown = DropDown()

        English_button = Button(text= "English", size_hint_y= None)
        French_button = Button(text= "French", size_hint_y= None)
        German_button = Button(text= "German", size_hint_y= None)
        Spanish_button = Button(text= "Spanish", size_hint_y = None)

        English_button.bind(on_release = lambda btn: self.select_language("English"))
        French_button.bind(on_release = lambda btn: self.select_language("French"))
        German_button.bind(on_release = lambda btn: self.select_language("German"))
        Spanish_button.bind(on_release = lambda btn: self.select_language("Spanish"))

        self.language_dropdown.add_widget(English_button)
        self.language_dropdown.add_widget(French_button)
        self.language_dropdown.add_widget(German_button)
        self.language_dropdown.add_widget(Spanish_button)

        self.source_language_dropdown = DropDown()

        English_button_source = Button(text= "English", size_hint_y= None)
        French_button_source = Button(text= "French", size_hint_y= None)
        German_button_source = Button(text= "German", size_hint_y= None)
        Spanish_button_source = Button(text= "Spanish", size_hint_y = None)

        English_button_source.bind(on_release = lambda btn: self.select_language_source("English"))
        French_button_source.bind(on_release = lambda btn: self.select_language_source("French"))
        German_button_source.bind(on_release = lambda btn: self.select_language_source("German"))
        Spanish_button_source.bind(on_release = lambda btn: self.select_language_source("Spanish"))

        self.source_language_dropdown.add_widget(English_button_source)
        self.source_language_dropdown.add_widget(French_button_source)
        self.source_language_dropdown.add_widget(German_button_source)
        self.source_language_dropdown.add_widget(Spanish_button_source)


        self.img = Image()
        

    def open_measurement_dropdown(self):
        self.measurement_dropdown.open(self.ids.measurement_button)

    def open_language_dropdown(self):
        self.language_dropdown.open(self.ids.language_button)
    
    def open_source_language(self):
        self.source_language_dropdown.open(self.ids.source_language)

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

    def select_language(self, text):
        if text == "English":
            self.target_language = "en"
            self.language_button_text = "Target Language \nEnglish"
        elif text == "French":
            self.target_language = "fr"
            self.language_button_text = "Target Language \nFrench"
        elif text == "German":
            self.target_language = "de"
            self.language_button_text = "Target Language \nGerman"
        elif text == "Spanish":
            self.target_language = "es"
            self.language_button_text = "Target Language \nSpanish"
        else:
            pass
        
    




    def select_language_source(self, text):
        if text == "English":
            self.source_language_target = "en"
            self.source_language_button_text = "Source Language \nEnglish"
        elif text == "French":
            self.source_language_target = "fr"
            self.source_language_button_text = "Source Language \nFrench"
        elif text == "German":
            self.source_language_target = "de"
            self.source_language_button_text = "Source Language \nGerman"
        elif text == "Spanish":
            self.source_language_target = "es"
            self.source_language_button_text = "Source Language \nSpanish"
        else:
            pass
    

    def btn(self):
        input_text = str(self.input_text.text)
        print(f"imperial {self.measurement_type}, input text = {input_text}")
        preTranslatedOutput = main_loop(self.measurement_type,input_text)
        print(preTranslatedOutput)
        print(f"translating into {self.target_language} : {preTranslatedOutput}")
        TranslatedOutput = Translating(preTranslatedOutput, self.source_language_target,self.target_language)
        self.manager.get_screen("output").output_text = TranslatedOutput
        self.manager.current = "output"
        self.input_text.text = ""

    def take_picture(self, *args):
        print("trying to take a picture")
        try:
            camera.take_picture(filename="picture.jpg", on_complete = self.on_picture_taken)
        except NotImplementedError:
            print("Camera feature is not implemented on this platform.")

    def on_picture_taken(self, filepath):
        if filepath:
            self.img.source = filepath
            self.img.reload()
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




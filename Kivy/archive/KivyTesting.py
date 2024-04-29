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


# class MyGrid(GridLayout):
#     def __init__(self, **kwargs):
#         super(MyGrid, self).__init__(**kwargs)
#         self.cols = 1

#         self.inside = GridLayout()
#         self.inside.cols = 2

        
#         self.inside.add_widget(Label(text="First Name: "))
#         self.name = TextInput(multiline=False)
#         self.inside.add_widget(self.name)

#         self.inside.add_widget(Label(text=" Last Name: "))
#         self.lastName = TextInput(multiline=False)
#         self.inside.add_widget(self.lastName)

#         self.inside.add_widget(Label(text="Email: "))
#         self.email = TextInput(multiline=False)
#         self.inside.add_widget(self.email)

#         self.add_widget(self.inside)

#         self.submit = Button(text="Submit", font_size=40)
#         self.submit.bind(on_press=self.pressed)
#         self.add_widget(self.submit)

#     def pressed(self, instance):
#         name = self.name.text
#         last= self.lastName.text
#         email = self.email.text
#         print("Name: ", name, "Last Name: ", last, "Email: ", email)
#         self.name.text = ""
#         self.lastName.text = ""
#         self.email.text = ""


inputtext = "lukethisdoesn'twork"
output = ""

class MyGrid(Widget):
    input = ObjectProperty(None)
    output = ObjectProperty("")

    def btn(self):
        inputtext = str(self.input.text)
        preTranslatedOutput = main_loop(True,inputtext)
        self.output.text = preTranslatedOutput
        print(preTranslatedOutput)
        self.input.text = ""



class MyApp(App):
    def build(self):
#         ##return Label(text="IM RICH", font_size=300, color="brown")
        return MyGrid()
    

if __name__ == "__main__":
    MyApp().run()




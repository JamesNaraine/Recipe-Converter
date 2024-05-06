import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, StringProperty
from kivy.lang import Builder
import sys
from pathlib import Path

# Ensure the parent directory is in sys.path
parent_dir = str(Path(__file__).resolve().parent.parent.parent)
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

from conversion import main_loop  # Assuming main_loop function exists

class MainWindow(Screen):
    input_text = ObjectProperty(None)

    def btn(self):
        input_text = str(self.input_text.text)
        translated_output = main_loop(True, input_text)
        self.manager.get_screen('output').output_text = translated_output
        self.manager.current = 'output'
        self.input_text.text = ""

class OutputWindow(Screen):
    output_text = StringProperty('')

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("OnePage.kv")

class MyApp(App):
    def build(self):
        return kv

if __name__ == "__main__":
    MyApp().run()

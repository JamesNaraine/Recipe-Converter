from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from plyer import camera
from kivy.core.window import Window

class CameraApp(App):
    def build(self):
        self.img = Image()
        layout = BoxLayout(orientation='vertical')
        self.btn = Button(text='Take Picture', size_hint=(1, 0.2))
        self.btn.bind(on_press=self.take_picture)
        layout.add_widget(self.btn)
        layout.add_widget(self.img)
        return layout

    def take_picture(self, *args):
        # Use plyer to take a picture and save it to a file
        try:
            camera.take_picture(filename='picture.jpg', on_complete=self.on_picture_taken)
        except NotImplementedError:
            print("Camera feature is not implemented on this platform.")

    def on_picture_taken(self, filepath):
        # Update the Image widget to display the picture
        if filepath:
            self.img.source = filepath
            self.img.reload()

if __name__ == '__main__':
    CameraApp().run()

from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.image import AsyncImage

class MyImage(AsyncImage):
    pass

class MyKivy3App(App):
    def build(self):
        return MyImage()

if __name__ == '__main__':
    MyKivy3App().run()
from kivy.app import App
from kivy.graphics import Rectangle
from kivy.uix.widget import Widget

class MyWidget(Widget):
    def on_touch_down(self, touch):
        # canvas is a root class object containing a set of drawing instructions
        # add is a Canvas method that lets us append a graphical drawing instruction to the canvas
        self.canvas.add(Rectangle(pos=(touch.x, touch.y), size=(50,50)))

class MyKivyApp(App):
    def build(self):
        return MyWidget

if __name__=='__main__':
    MyKivyApp().run()
from kivy.app import App
from kivy.graphics import Rectangle, Line
from kivy.uix.widget import Widget

class MyWidget(Widget):
    # touch.ud['line'] (touch dictionary) is an array that stores the history of points that make up our line object
    # the touch dictionary (Line object) is initiated with the first coordinate point when we touch down, then we add 
    # the Line object to the canvas 
    def on_touch_down(self, touch):
        touch.ud['line'] = Line(points=(touch.x, touch.y))
        self.canvas.add(touch.ud['line'])

    # we append the touch dictionary with our move points and add them to the canvas
    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y] 



class MyKivyApp(App):
    def build(self):
        return MyWidget()

if __name__=='__main__':
    MyKivyApp().run()
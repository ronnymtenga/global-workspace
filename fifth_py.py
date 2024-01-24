from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class MyLabel(Label):
    def __init__(self, text):
        super().__init__()
        self.text = text # just a string variable for the current instance

    # touch is a variable for the position of the touch on the GUI
    # here we simulate (by mouse click) a touch and return the action and the position of the action
    def on_touch_down(self, touch):
        print('DOWN', touch) #print has been overloaded probs
    def on_touch_up(self, touch):
        print('UP', touch)
    def on_touch_move(self, touch):
        print('MOVE', touch)

class MyKivyApp(App):
    def build(self):
        self.currentLabel = MyLabel('hi')
        return self.currentLabel
    
if __name__ == '__main__':
    MyKivyApp().run()
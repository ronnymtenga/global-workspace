from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

# recycle view explanations here: https://chat.openai.com/share/5f786f50-4292-4d5d-973f-b98c86101fea
from kivy.uix.recycleview import RecycleView

class RV(RecycleView):
    def __init__(self):
        super().__init__()
        # data is a list of dictionaries where each dictionary contains 
        # key-value pairs which correspond to the data of the viewclass 
        # to be displayed in the Recycle View, eg 'text' : string
        self.data = [{'text':str(i)} for i in range(20)]

class MyKivy5App(App):
    def build(self):
        return RV()
    
if __name__ == '__main__':
    MyKivy5App().run()
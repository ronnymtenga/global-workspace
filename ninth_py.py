from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty 

class MyBox(Widget):
    # ObjectProperty class links the main .py o the .kv file
    # Here myInput is an ObjectProperty object which allows us 
    # to link the id variable in the TextInput widget back to
    # our MyBox class so we can access the text input from 
    # TextInput in the printOut method. (the key is the myInput: inputID 
    # which links any variable in our kv file that is set to var: inputID, 
    # to myInput which is then linked back to here)

    # In reality the ObjectProperty class is used to create a property (myInput) 
    # which stores an instance of another widget (TextInput)... 
    myInput = ObjectProperty(None)
    def printOut(self):
    # ...allowing us to access the properties of that widget; here we access the text 
    # property of the TextInput widget 
        print(self.myInput.text)
    

class MyKivy2App(App):
    def build(self):
        return MyBox()

if __name__ == '__main__':
    MyKivy2App().run()
from kivy.app import App 
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

# create our own widget class that inherits from BoxLayout
class MyLayout(BoxLayout):
    # a method that initializes a layout widget object that is made from MyLayout class
    # self is a reference to the current layout widget object(instance)
    def __init__(self):
        # super() returns a temporary instance of the parent class of our subclass allowing 
        # us to inherit methods and instance variables defined in the parent class from the subclass eg. the __init__() constructor method
        super().__init__()
        # here we create an instance variable called button then instantiate and assign a new Button widget object to it
        self.button = Button(text='Click here')
        # here we bind an event that is triggered by the button which in our case is a function that will run
        self.button.bind(on_press = self.new_label)# not self.new_label() so it doesnt run right away
        # adding the button widget to the current layout widget object
        self.add_widget(self.button)#add_button was already inherited from a higher class (probaby from kivy to boxlayout to MyLayout)

    def new_label(self, button):
        self.label = Label(text='Hello, Kivy!')
        self.add_widget(self.label)
        self.remove_widget(button) #we dont have to use self.button since the instance variable was already passed into the method as a parameter

# create our App class
class MyKivyApp(App):
    def build(self):
        return MyLayout() #root widget is an object from our MyLayout class
    
if __name__ == '__main__':
    MyKivyApp().run()
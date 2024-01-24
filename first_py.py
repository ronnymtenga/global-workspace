from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

class SimpleKivyApp(App):
    # buid method defined in App class called when the app is started and for creates the root widget of the app
    def build(self):
        # Create a BoxLayout class object (widget)
        layout = BoxLayout(orientation='vertical')
        # Create a Label and Button class objects (widget) with text
        # A widget is the basic buiding block of GUI interfaces
        # Widgets in kivy are organized in trees 
        label1 = Label(text='Label 1')
        label2 = Label(text='Label 2')
        button = Button(text='Press Me')
        # Adding the label widgets to the layout widget; add_widget is a method in the BoxLayout class
        # add_widget is one of several methods that can manipulate the widget tree in a kivy app
        layout.add_widget(label1)
        layout.add_widget(label2) 
        layout.add_widget(button)
        # Return the layout as the root widget of the application
        # The root widget of a kivy app manages the layout of all other widgets
        # The root widget at the top of the widget tree
        return layout

# Run the application
if __name__ == '__main__':
    SimpleKivyApp().run()

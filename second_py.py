from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class SimpleKivyApp(App):
    def build(self):

        layout = FloatLayout()
        # size_hint={width, height} (dimentions)
        # pos_hint={x_center,y_center} (x,y position)
        # width and height are % values of the dimentions of the root widget (same as pos_hint)
        # here the root widget is a FloatLayout which takes up the whole window
        label1 = Label(text='Label 1', size_hint={0.3, 0.2}, pos_hint={'center_x':0.2, 'center_y':0.5})
        label2 = Label(text='Label 2', size_hint={0.5, 0.7}, pos_hint={'center_x':0.5, 'center_y':0.2})

        layout.add_widget(label1)
        layout.add_widget(label2)

        return layout

# Run the application
if __name__ == '__main__':
    SimpleKivyApp().run()

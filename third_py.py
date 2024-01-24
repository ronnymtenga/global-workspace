from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class SimpleKivyApp(App):
    def build(self):
        layout = FloatLayout()
        button = Button(text='Click here', size_hint={0.9, 0.15}, pos_hint={'center_x':0.5, 'center_y':0.2})

        layout.add_widget(button)

        return layout

# Run the application
if __name__ == '__main__':
    SimpleKivyApp().run()

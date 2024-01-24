from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition

class FirstPage(Button):
    def __init__(self):
        super().__init__()
        self.text = 'Hello'
        self.bind(on_press=self.switch)

    def switch(self, item):
        mykivy.screen_manager.transition = SlideTransition(direction='down')
        mykivy.screen_manager.current = 'second'

class SecondPage(Button):
    def __init__(self):
        super().__init__()
        self.text = 'World'
        self.bind(on_press=self.switch)

    def switch(self, item):
        mykivy.screen_manager.transition = SlideTransition(direction='up')
        mykivy.screen_manager.current = 'first'

class MyKivyApp(App):
    def build(self):
        # instantiate ScreenManager class
        self.screen_manager = ScreenManager()

        self.firstpage = FirstPage()# is 1st button
        screen = Screen(name='first')# create 1st screen object
        screen.add_widget(self.firstpage)#add 1st button to 1st screen
        self.screen_manager.add_widget(screen)#add 1st screen to screen manager

        self.secondpage = SecondPage()# is 2nd button
        screen = Screen(name='second')# create 2nd screen object
        screen.add_widget(self.secondpage)#add 2nd button to 2nd screen
        self.screen_manager.add_widget(screen)#add 2nd screen to screen manager

        return self.screen_manager # is our root widget


mykivy = MyKivyApp()
mykivy.run() 
from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.uix.boxlayout import BoxLayout

class SoundPlayer(BoxLayout):
    

    def play_sound(self):
        sound = SoundLoader.load('lelly.mp3')
        if sound:
            sound.volume = 0.5
            sound.play()

class MyKivy4App(App):
    def build(self):
        return SoundPlayer()
    
if __name__ == '__main__':
    MyKivy4App().run()
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.recycleview import RecycleView

# every ivariable that is in the form of "self.variable" is an instance 
# variable and is only created and owned by the current instantiated object 
# so every instance of the class will have its own value for self.variable
class ListViewer(RecycleView): 

	# this creates the data dictionary which is updated through the item list
	def update(self):
		self.data = [{'text':str(item)} for item in self.items]

	# this initiated a recycleview widget and its item list (initially with no items inside) 
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.items = []


class MainWidget(BoxLayout):
	inputcontent = ObjectProperty(None)
	outputcontent = ObjectProperty(None)

	def add_item(self):
		if self.inputcontent.text != '':
			# access TextInput class with inputcontent Object Property to format the inputted string
			formatted = f'\n •{self.inputcontent.text}'
			# access the ListViewer class with outputcontent Object Property to add the formatted 
			# string to items and then run the update method (items and update() are ListViewer properties)
			self.outputcontent.items.append(formatted)
			self.outputcontent.update()
			# empty the TextInput widget
			self.inputcontent.text = ''

class mainApp(App):
	def build(self):
		return MainWidget()


if __name__ == '__main__':
	mainApp().run()
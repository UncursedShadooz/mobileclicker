import kivy
# kivy.require('2.3.1') # adjust the minimum required Kivy version as needed

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.lang import Builder

# Define the screens in Kv language for cleaner structure
Builder.load_string("""
<MenuScreen>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Welcome to the Calculator'
        BoxLayout:
            orientation: 'horizontal'
            Button:
                text: '1'
            Button:
                text: '2'
            Button:
                text: '3'
        BoxLayout:
            orientation: 'horizontal'
            Button:
                text: '4'
            Button:
                text: '5'
            Button:
                text: '6'
        BoxLayout:
            orientation: 'horizontal'
            Button:
                text: '7'
            Button:
                text: '8'
            Button:
                text: '9'
""")

# 1. Subclass the Screen class for each screen you need
class MenuScreen(Screen):
    pass

# 2. Create the main application class
class ScreenApp(App):
    def build(self):
        # 3. Create the ScreenManager instance
        sm = ScreenManager()
        
        # 4. Add your custom screens to the manager
        sm.add_widget(MenuScreen(name='menu'))
        
        return sm

if __name__ == '__main__':
    ScreenApp().run()

# from kivy.uix.popup import Popup
# from kivy.uix.label import Label
# from kivy.uix.button import Button
# from kivy.uix.boxlayout import BoxLayout
# from kivy.app import App
# from kivy.core.window import Window

# class TestApp(App):
#     def build(self):
#         # Create the content for the popup
#         content = BoxLayout(orientation='vertical')
#         content.add_widget(Label(text='Hello world'))
#         close_button = Button(text='Close', size_hint_y=None, height=40)
#         content.add_widget(close_button)

#         # Create the Popup widget
#         self.popup = Popup(title='Test popup',
#                            content=content,
#                            size_hint=(None, None), size=(400, 400),
#                            auto_dismiss=False)

#         # Bind the close button press to the popup's dismiss method
#         close_button.bind(on_release=self.popup.dismiss)

#         # Main window content button to open the popup
#         open_button = Button(text='Open Popup')
#         open_button.bind(on_release=self.popup.open)
#         return open_button

# if __name__ == '__main__':
#     TestApp().run()

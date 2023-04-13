from funkcija import download_song
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import webbrowser
from kivy.properties import StringProperty


class MainInterface(BoxLayout):
    connection_message=StringProperty('')
    try:
        def __init__(self, **kwargs):
            super().__init__(**kwargs)


        def submit_link(self, link):
            download_song(link)


        def open_github(self):
            webbrowser.open("https://github.com/EyeAmHari")
       
    except ConnectionError:
        connection_message=StringProperty('Please connect to the internet and try again.')
    except ValueError:
        connection_message=StringProperty('Please input the correct.')

class AplikacijaApp(App):
    pass


#pokrecemo kopmletan program
AplikacijaApp().run()

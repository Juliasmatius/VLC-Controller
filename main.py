import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

class VLCHttpControl:
    def __init__(self, base_url, username, password):
        self.base_url = base_url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
        }
        self.playing = False
        self.username = ""
        self.password = password
    def changeurlorpass(self, base_url, password):
        self.base_url = base_url
        self.password = password
    def toggle_play_pause(self):
        command = 'pl_pause'
        response = self.send_command(command)
        self.playing = not self.playing
        return response

    def send_command(self, command):
        url = f"{self.base_url}/requests/status.xml?command={command}"
        print(self.password)
        response = requests.get(url, auth=("", self.password), headers=self.headers)
        return response

    def skip_forward(self):
        response = self.send_command('pl_next')
        return response

    def skip_backward(self):
        response = self.send_command('pl_previous')
        return response
    def set_volume(self, volume):
        volume_command = f'volume&val={int(volume)}'
        response = self.send_command(volume_command)
        return response

class VLCControlApp(App):
    def build(self):
        self.title = 'VLC Controller'
        def on_base_url_text_change(instance, value):
            vlc_http_control.changeurlorpass(value, password_input.text)

        def on_password_text_change(instance, value):
            vlc_http_control.changeurlorpass(base_url_input.text, value)
        base_url = "http://localhost:8080"  # Default VLC HTTP interface URL
        username = ""
        password = ""
        vlc_http_control = VLCHttpControl(base_url, username, password)

        layout = BoxLayout(orientation='vertical')

        base_url_input = TextInput(hint_text='Enter base URL(with http://)')
        password_input = TextInput(hint_text='Enter password')
        
        base_url_input.bind(text=on_base_url_text_change)
        password_input.bind(text=on_password_text_change)
        play_pause_button = Button(text='Play/Pause')
        play_pause_button.bind(on_press=lambda instance: vlc_http_control.toggle_play_pause())

        stop_button = Button(text='Stop')
        stop_button.bind(on_press=lambda instance: vlc_http_control.send_command('pl_stop'))

        skip_forward_button = Button(text='Forward')
        skip_forward_button.bind(on_press=lambda instance: vlc_http_control.skip_forward())

        skip_backward_button = Button(text='Backward')
        skip_backward_button.bind(on_press=lambda instance: vlc_http_control.skip_backward())

        fullscreen_button = Button(text='Fullscreen')
        fullscreen_button.bind(on_press=lambda 
            instance: vlc_http_control.send_command('fullscreen'))
        volume_label = Label(text='Volume: 100%')
        volume_slider = Slider(min=0, max=320, value=255)
        volume_slider.bind(value=lambda instance, value: self.update_volume_label(volume_label, value))
        volume_slider.bind(value=lambda instance, value: self.update_volume(vlc_http_control, value))

        layout.add_widget(base_url_input)
        layout.add_widget(password_input)
        layout.add_widget(play_pause_button)
        layout.add_widget(stop_button)
        layout.add_widget(skip_forward_button)
        layout.add_widget(skip_backward_button)
        layout.add_widget(fullscreen_button)
        layout.add_widget(volume_label)
        layout.add_widget(volume_slider)

        self.vlc_http_control = vlc_http_control  # Store it as an attribute for volume control


        return layout

    
    def update_volume_label(self, label, value):
        if value==0:
            label.text = f'Volume: 0%'
        else:
            label.text = f'Volume: {int(value/255*100)}%'
    def update_volume(self, vlc_http_control, value):
        vlc_http_control.set_volume(value)
    def on_base_url_text_change(self, vlc_http_control, new_base_url):
        print("Base URL changed:", new_base_url)
        vlc_http_control.changeurlorpass(new_base_url, vlc_http_control.password)

    def on_password_text_change(self, vlc_http_control, new_password):
        print("Password changed:", new_password)
        vlc_http_control.changeurlorpass(vlc_http_control.base_url, new_password)

if __name__ == '__main__':
    VLCControlApp().run()

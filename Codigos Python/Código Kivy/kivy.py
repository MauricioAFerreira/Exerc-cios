from kivy.app import App
from kivy.uix.button import Button

class MainApp(App):
    def build(self):
        button = Button(
            text='Olá, LinkedIn!',
            size_hint=(.5, .5),
            pos_hint={'center_x': .5, 'center_y': .5}
        )
        button.bind(on_press=self.on_press)
        return button

    def on_press(self, instance):
        print('O botão foi pressionado!')

MainApp().run()

from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton

class DemoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Teal'
        self.theme_cls.primary_hue = '500'
        self.theme_cls.theme_style = 'Dark'

        screen = Screen()
        
        btn_flat = MDRectangleFlatButton(
            text="Hello World",
            pos_hint={'center_x':.5, 'center_y':.5}
        )

        screen.add_widget(btn_flat)

        return screen


DemoApp().run()

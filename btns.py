from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton, MDFloatingActionButton


class DemoApp(MDApp):
    def build(self):
        screen = Screen()

        btn_flat = MDFlatButton(
            text='Hello World',
            pos_hint={'center_x':.5, 'center_y':.9}    
        )

        btn_rectangle_flat = MDRectangleFlatButton(
            text='Hello World',
            pos_hint={'center_x':.5, 'center_y':.8} 
        )

        icon_btn = MDIconButton(
            icon='android',
            pos_hint={'center_x':.5, 'center_y':.7} 
        )
        
        icon_floating_btn = MDFloatingActionButton(
            icon='language-python',
            pos_hint={'center_x':.5, 'center_y':.6} 
        )

        screen.add_widget(btn_flat)
        screen.add_widget(btn_rectangle_flat)
        screen.add_widget(icon_btn)
        screen.add_widget(icon_floating_btn)

        return screen


DemoApp().run()
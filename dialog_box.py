from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.dialog import MDDialog

from kivy.lang import Builder

from helpers import username_helper



class DemoApp(MDApp):
    def build(self):
        screen = Screen()
        self.theme_cls.primary_palette= "Green"

        button = MDRectangleFlatButton(
            text="Show",
            pos_hint={'center_x':.5, 'center_y':.4},
            on_release=self.show_data
        )

        self.username= Builder.load_string(username_helper)
        
        screen.add_widget(self.username)
        screen.add_widget(button)

        return screen

    def show_data(self, obj):
        if self.username.text == '':
            check_string = 'Please enter a username'
        else:
            check_string = f'{self.username.text} does not exist'

        close_button = MDFlatButton(
            text='Close',
            on_release=self.close_dialog
        )

        other_button = MDFlatButton(
            text='Other'
        )
        
        self.dialog = MDDialog(
            title='Username Check',
            text=check_string,
            size_hint=(.7, 1),
            buttons=[close_button, other_button]
        )

        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()


DemoApp().run()
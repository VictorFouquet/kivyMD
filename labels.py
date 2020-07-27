from kivymd.app import MDApp
from kivymd.uix.label import MDLabel,MDIcon

class DemoApp(MDApp):
    def build(self):
        label = MDLabel(
            text="Demo App",
            halign="center",
            theme_text_color='Custom', 
            text_color=(0,0.6,1,1),
            font_style='H1'
        )

        icon_label = MDIcon(
            icon='language-python',
            halign='center'
        )
        
        #return label
        return icon_label

DemoApp().run()
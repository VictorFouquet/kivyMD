from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.list import MDList, ThreeLineListItem, ThreeLineIconListItem, ThreeLineAvatarListItem
from kivymd.uix.list import IconLeftWidget, ImageLeftWidget



list_helper = '''
Screen:
    ScrollView:
        MDList:
            id: container

'''

class DemoApp(MDApp):
    def build(self):
        screen = Builder.load_string(list_helper)
        return screen

    def on_start(self):
        for i in range(1,21):
            if i % 2 == 0:
                icon = IconLeftWidget(
                    icon="android"
                )

                item =  ThreeLineIconListItem(
                    text=f"Item {i}",
                    secondary_text="Three lines version",
                    tertiary_text="Third line"
                )
                item.add_widget(icon)

            else:
                image = ImageLeftWidget(
                    source="logoC.png"
                )

                item =  ThreeLineAvatarListItem(
                    text=f"Item {i}",
                    secondary_text="Three lines version",
                    tertiary_text="Third line"
                )
                item.add_widget(image)


            self.root.ids.container.add_widget(item)

DemoApp().run()
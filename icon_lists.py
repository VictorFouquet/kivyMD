from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import MDList, ThreeLineListItem, ThreeLineIconListItem, ThreeLineAvatarListItem
from kivymd.uix.list import IconLeftWidget, ImageLeftWidget
from kivy.uix.scrollview import ScrollView



class DemoApp(MDApp):
    def build(self):
        screen = Screen()
        self.theme_cls.primary_palette= "Green"
        
        list_view = MDList()
        
        scroll = ScrollView()
        scroll.add_widget(list_view)

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

            list_view.add_widget(item)


        screen.add_widget(scroll)
        
        return screen



DemoApp().run()
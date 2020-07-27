from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import MDList, OneLineListItem, TwoLineListItem, ThreeLineListItem
from kivy.uix.scrollview import ScrollView



class DemoApp(MDApp):
    def build(self):
        screen = Screen()
        self.theme_cls.primary_palette= "Green"
        
        list_view = MDList()
        
        scroll = ScrollView()
        scroll.add_widget(list_view)

        for i in range(1,21):
            item = OneLineListItem(
                text=f"Item {i}"
            )
            item2 = TwoLineListItem(
                text=f"Item {i}",
                secondary_text=f"Two lines version"
            )
            item3 = ThreeLineListItem(
                text=f"Item {i}",
                secondary_text="Three lines version",
                tertiary_text="Third line"
            )

            list_view.add_widget(item)
            list_view.add_widget(item2)
            list_view.add_widget(item3)

        screen.add_widget(scroll)
        
        return screen



DemoApp().run()
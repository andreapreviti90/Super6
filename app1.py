from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.image import Image
from kivymd.uix.label import MDLabel
from random import sample



KV = """
BoxLayout:
    orientation: 'vertical'
    Screen:
        MDRectangleFlatButton:
            id: generate_button
            text: "GENERA NUMERI"
            pos_hint: {"center_x": 0.5, "center_y": 0.5} 
            bold: True
            md_bg_color: 1, 0.92, 0.23, 1  # Giallo
            on_release: app.generate_numbers()

        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: self.minimum_height  
            pos_hint: {"center_x": 0.5, "center_y": 0.3}  
            MDLabel:
                id: numbers_label
                text: ""
                theme_text_color: "Secondary"
                halign: 'center'
                font_style: 'H6'  

        FitImage:
            source: "lotteria.jpg"
            size_hint_y: .35
            pos_hint: {"top": 1}
            radius: "36dp", "36dp", 0, 0
"""

class MainApp(MDApp):
    def build(self):
        self.title = "Super6"
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_string(KV)
    
    def generate_numbers(self):
        numbers = sample(range(1, 91), 6)
        numbers_str = "  |  ".join(map(str, numbers)) 
        self.root.ids.numbers_label.text = numbers_str

if __name__ == "__main__":
    MainApp().run()
        
    

MainApp().run()
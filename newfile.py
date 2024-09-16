from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        # Membuat layout vertikal
        layout = BoxLayout(orientation='vertical')
        
        # Membuat label dan tombol
        self.label = Label(text="Hello, Kivy!")
        btn = Button(text="Click Me")
        
        # Menambahkan fungsi saat tombol ditekan
        btn.bind(on_press=self.change_text)
        
        # Menambahkan label dan tombol ke layout
        layout.add_widget(self.label)
        layout.add_widget(btn)
        
        return layout

    def change_text(self, instance):
        self.label.text = "Button Pressed!"

# Menjalankan aplikasi
if __name__ == '__main__':
    MyApp().run()
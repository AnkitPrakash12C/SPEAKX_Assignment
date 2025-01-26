from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MainApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        self.name_input = TextInput(hint_text='Enter your name')
        self.age_input = TextInput(hint_text='Enter your age', input_filter='int')

        submit_button = Button(text='Submit')
        submit_button.bind(on_press=self.on_submit)

        self.result_label = Label(text='')

        layout.add_widget(self.name_input)
        layout.add_widget(self.age_input)
        layout.add_widget(submit_button)
        layout.add_widget(self.result_label)

        return layout

    def on_submit(self, instance):
        name = self.name_input.text
        age = int(self.age_input.text) if self.age_input.text.isdigit() else 0

        if 10 < age < 18:
            self.result_label.text = f'Hello {name}, you are eligible!'
        else:
            self.result_label.text = 'You are not eligible.'

if __name__ == '__main__':
    MainApp().run()

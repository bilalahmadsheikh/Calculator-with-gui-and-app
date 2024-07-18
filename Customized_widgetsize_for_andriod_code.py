from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

class CalculatorApp(App):
    def build(self):
        self.operators = ["+", "-", "*", "/"]
        self.last_was_operator = None
        self.last_button = None

        # Get window size
        window_width, window_height = Window.size

        # Set sizes dynamically
        font_size = window_width * 0.08  # Increased font size for display
        button_font_size = window_width * 0.08
        button_height = window_height * 0.12
        display_height = window_height * 0.2  # Increased height for display

        self.solution = TextInput(font_size=font_size, readonly=True, halign="right", multiline=False, size_hint_y=None, height=display_height)
        main_layout = BoxLayout(orientation="vertical")
        main_layout.add_widget(self.solution)
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"],
            ["="]
        ]
        for row in buttons:
            h_layout = BoxLayout(size_hint_y=None, height=button_height)
            for label in row:
                button = Button(
                    text=label, font_size=button_font_size, size_hint_y=None, height=button_height, pos_hint={"center_x": 0.5, "center_y": 0.5}
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)
        return main_layout

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == "C":
            self.solution.text = ""
        elif button_text == "=":
            try:
                self.solution.text = str(eval(self.solution.text))
            except Exception:
                self.solution.text = "Error"
        else:
            if current and (
                self.last_was_operator and button_text in self.operators):
                return
            elif current == "" and button_text in self.operators:
                return
            else:
                new_text = current + button_text
                self.solution.text = new_text
        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators

if __name__ == "__main__":
    app = CalculatorApp()
    app.run()

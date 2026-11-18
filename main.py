from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class HostelCalculator(App):

    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=12
        )

        layout.add_widget(Label(
            text="HOSTEL EXPENSE CALCULATOR",
            font_size=23,
            bold=True,
            size_hint_y=None,
            height=60
        ))

        self.rent = self.add_field(layout, "Hostel Rent")
        self.food = self.add_field(layout, "Food Expense")
        self.electricity = self.add_field(layout, "Electricity Units")
        self.rate = self.add_field(layout, "Charge per Unit")
        self.persons = self.add_field(layout, "Number of Persons")

        button = Button(
            text="CALCULATE",
            size_hint_y=None,
            height=55
        )
        button.bind(on_press=self.calculate)
        layout.add_widget(button)

        self.result = Label(
            text="Each person will pay: Rs. 0",
            font_size=20
        )
        layout.add_widget(self.result)

        return layout

    def add_field(self, layout, hint):
        field = TextInput(
            hint_text=hint,
            multiline=False,
            input_filter="int",
            size_hint_y=None,
            height=48
        )
        layout.add_widget(field)
        return field

    def calculate(self, instance):
        try:
            rent = int(self.rent.text)
            food = int(self.food.text)
            electricity_spend = int(self.electricity.text)
            charge_per_unit = int(self.rate.text)
            persons = int(self.persons.text)

            if persons <= 0:
                self.result.text = "Enter valid persons!"
                return

            total_bill = electricity_spend * charge_per_unit

            output = (food + rent + total_bill) / persons

            self.result.text = (
                f"Each person will pay: Rs. {output:.2f}"
            )

        except ValueError:
            self.result.text = "Please fill all fields!"


if __name__ == "__main__":
    HostelCalculator().run()

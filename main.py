from weather_finder import get_data
import customtkinter as ctk
from datetime import datetime


class WeatherApp(ctk.CTk):
    def convert_temperature(self, choice):
        try:
            temperature = self.temperature
            if choice != 'fahrenheit':
                self.temperature_label.configure(text=f"{temperature} °C")
            else:
                temperature = int(temperature * (9 / 5) + 32)
                self.temperature_label.configure(text=f"{temperature} °F")
                print(temperature)
        except:
            self.entry_town.configure(placeholder_text=f"Insert a town first")

    def get_data_list(self, event):
        self.data_weather_list: list = get_data(self.entry_town.get())
        self.temperature = self.data_weather_list[0]
        self.emoji_label.configure(text=f"     {self.data_weather_list[1].emoji}")

        self.temperature_label.configure(text=f"{self.temperature} °C")

        self.data_weather_list.pop()
        self.data_weather_list.pop()

    def __init__(self):
        super().__init__()
        self.temperature = None
        self.data_weather_list = None
        self.title("Weather app")
        self.geometry(f"{720}x{520}")

        self.columnconfigure((0, 1, 2), weight=4, uniform='a')
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1, uniform='a')

        self.left_side = ctk.CTkFrame(self)
        self.left_side.grid(row=0, column=0, sticky="nsew")
        self.left_side.columnconfigure((0, 1, 2), weight=1, uniform='a')
        self.left_side.columnconfigure(0, weight=2, uniform='a')
        self.left_side.columnconfigure(1, weight=5, uniform='a')

        self.left_side.rowconfigure((0, 1, 2, 3, 4, 5), weight=2, uniform='a')
        self.left_side.grid_rowconfigure(3, weight=1)

        self.entry_town = ctk.CTkEntry(self.left_side, placeholder_text="Enter a town",
                                       corner_radius=10,
                                       fg_color=r"#525894",
                                       border_width=2
                                       )
        self.entry_town.grid(row=4, column=1, sticky="nsew", pady=(30, 10))
        self.entry_town.bind("<Return>", self.get_data_list)

        self.emoji_label = ctk.CTkLabel(self.left_side,
                                        corner_radius=10,
                                        fg_color="gray",
                                        text="",
                                        font=("roboto", 50)
                                        )
        self.emoji_label.grid(row=1, column=1, rowspan=2, sticky='nsew', padx=(5, 5))

        self.temperature_label = ctk.CTkLabel(self.left_side,
                                              corner_radius=10,
                                              text="",
                                              font=("roboto", 20)
                                              )
        self.temperature_label.grid(row=3, column=1, sticky='nsew', padx=(30, 50))

        # right side

        self.right_side = ctk.CTkFrame(self)
        self.right_side.grid(row=0, column=2, sticky='nsew')

        self.right_side.columnconfigure((0, 1, 2, 3), weight=3, uniform='a')
        self.right_side.columnconfigure(1, weight=1, uniform='a')

        self.right_side.rowconfigure((0, 1, 2, 3, 4, 5), weight=2, uniform='a')
        self.right_side.rowconfigure(3, weight=1, uniform='a')

        self.date_frame = ctk.CTkFrame(self.right_side,
                                       corner_radius=15,
                                       fg_color='gray',
                                       )
        self.date_frame.grid(row=1, column=0, columnspan=2, rowspan=2, sticky='nsew', padx=(0, 100))
        self.date_frame.rowconfigure((0, 1), weight=1, uniform='a')

        self.time_label = ctk.CTkLabel(self.date_frame,
                                       corner_radius=10,
                                       fg_color='gray',
                                       text=f"{datetime.now():%H:%M}",
                                       font=("roboto", 20)
                                       )

        self.time_label.grid(row=0, sticky='nsew', pady=(15, 10))
        self.date_label = ctk.CTkLabel(self.date_frame,
                                       corner_radius=10,
                                       fg_color='gray',
                                       font=('roboto', 15),
                                       text=f"{datetime.now():%A, %d %B %Y}"
                                       )
        self.date_label.grid(row=1, sticky='nsew', padx=(0, 0))

        self.scaling_option = ctk.CTkOptionMenu(self.right_side,
                                                corner_radius=10,
                                                values=['celcius', 'fahrenheit'],
                                                command=self.convert_temperature
                                                )
        self.scaling_option.grid(row=4, column=0, columnspan=2, sticky='nsew', pady=(30, 25), padx=(0, 120))

        # middle side (for the color)
        self.middle_side = ctk.CTkFrame(self)
        self.middle_side.grid(row=0, column=1, rowspan=2, sticky='nsew')


if __name__ == "__main__":
    app = WeatherApp()
    app.mainloop()

from weather_finder import get_weather_forecast
import customtkinter as ctk
import datetime

class Weather_app(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.weather_info = None
        self.title("Weather app")
        self.geometry(f"{1080}x{720}")
        self.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), weight=1, uniform='a')
        self.columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), weight=1, uniform='a')

        # Create widgets
        self.label_city = ctk.CTkLabel(self, text="Enter City:")
        self.entry_city = ctk.CTkEntry(self)
        self.button_get_weather = ctk.CTkButton(self, text="Get Weather", command=self.display_weather)
        self.label_weather_info = ctk.CTkLabel(self, text="Weather Information")

        # Grid layout
        self.label_city.grid(row=0, column=0, padx=10)
        self.entry_city.grid(row=0, column=1, columnspan=2, padx=10)
        self.button_get_weather.grid(row=1, column=0, columnspan=3)
        self.label_weather_info.grid(row=2, column=0, columnspan=2)


    def display_weather(self):
        city = self.entry_city.get()
        if city:
            self.weather_info = get_weather_forecast(city)
            self.frame_label_info1 = ctk.CTkLabel(self, fg_color='gray', corner_radius=20)
            self.frame_label_info1.grid(
                row=3,rowspan=4, column=1, columnspan=3, padx=10, sticky='nsew'
            )
            self.date_info1 = ctk.CTkLabel(self, text=f"{self.weather_info[0].date :%d.%m.%y}", font=('roboto', 20))
            self.date_info1.grid(row=7, column=2, sticky='nsew')

            self.frame_label_info2 = ctk.CTkLabel(self, fg_color='gray', corner_radius=20).grid(
                row=3,rowspan=4, column=4,columnspan=3, padx=10, sticky='nsew'
            )
            self.date_info2 = ctk.CTkLabel(self, text=f"{self.weather_info[1].date :%d.%m.%y}", font=("roboto", 20))
            self.date_info2.grid(row=7, column=5, sticky='nsew')

            self.frame_label_info3 = ctk.CTkLabel(self, fg_color='gray', corner_radius=20).grid(
                row=3,rowspan=4, column=7, columnspan=3, padx=10,sticky='nsew'
            )
            self.date_info3 = ctk.CTkLabel(self, text=f"{self.weather_info[2].date :%d.%m.%y}", font=("roboto", 20))
            self.date_info3.grid(row=7, column=8, sticky='nsew')
            print(self.weather_info[2].date)

            self.frame_label_info1.configure(text="")
            print(self.weather_info[0].temperature)

            
            
        else:
            self.label_weather_info.configure(text="Please enter a city.")

        
        
if __name__ == "__main__":
    app = Weather_app()
    app.mainloop()

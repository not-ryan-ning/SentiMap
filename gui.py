#gui
import tkinter
import webbrowser

import customtkinter
from sentiment_map import *
from carbon_map import *

def generate():
    country = country_entry.get()
    selection = selection_var.get()

    if selection == "Option 1":
        make_sentiment_map(country)
        if country.lower() == 'canada':
            webbrowser.open('http://localhost:63342/SentiMap/canada_sentiment_map.html?_ijt=v2pube0k6vttu1fkut251i5f41&_ij_reload=RELOAD_ON_SAVE')
        else:
            webbrowser.open(
                'http://localhost:63342/SentiMap/usa_sentiment_map.html?_ijt=8elrlj11akpsi3q9ut2pnhsaob&_ij_reload=RELOAD_ON_SAVE')
    else:
        make_carbon_map(country)
        if country.lower() == 'canada':
            webbrowser.open(
                'http://localhost:63342/SentiMap/canada_carbon_map.html?_ijt=v2pube0k6vttu1fkut251i5f41&_ij_reload=RELOAD_ON_SAVE')
        else:
            webbrowser.open('http://localhost:63342/SentiMap/usa_carbon_map.html?_ijt=v2pube0k6vttu1fkut251i5f41&_ij_reload=RELOAD_ON_SAVE')


# system settings
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

# frame initialization
app = customtkinter.CTk()

screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

window_width = 500
window_height = 540
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
app.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))

app.title("SentiMap")

# UI elements
title = customtkinter.CTkLabel(app, text="Please input a country:")
title.pack(padx=10, pady=10)

user_country = tkinter.StringVar()
country_entry = customtkinter.CTkEntry(app, width=350, height=10,
                                       textvariable=user_country)
country_entry.pack()

selection_var = tkinter.StringVar()
selection_var.set("Option 1")

option_title = customtkinter.CTkLabel(app,
                                      text="Select an option for map:")
option_title.pack(padx=20, pady=10)

radiobutton1 = customtkinter.CTkRadioButton(app, text='Sentiment Analysis',
                                            variable=selection_var,
                                            value="Option 1"). \
    pack(anchor=tkinter.W, padx=125,
         pady=5)
radiobutton2 = customtkinter.CTkRadioButton(app,
                                            text='Carbon Emission Analysis',
                                            variable=selection_var,
                                            value="Option 2"). \
    pack(anchor=tkinter.W, padx=125,
         pady=5)

generate_button = customtkinter.CTkButton(app, text="Generate",
                                          command=generate)
generate_button.pack(padx=10, pady=10)

information = "Input a country name and select an option to generate " \
              "a heatmap! \n Here are what the following options generate:" \
              "\n \n Sentiment Analysis creates a heatmap of a country using " \
              "sentiment analysis of tweets with the topic climate change " \
              "which were sent from that location. Red indicates that people " \
              "living in that area are more negative to the concept of " \
              "climate change, and green indicates that they are more " \
              "receptive. This can help policymakers create targeted climate" \
              "change campaigns for areas where people are less receptive. " \
              "\n Carbon Emission Analysis creates a heatmap of a country " \
              "using its carbon emission by region, and suggests building " \
              "renewable energy generation sources based on wind, solar and " \
              "location data. This can help policymakers quickly decide the " \
              "best course of action to combat climate change." \

information_label = customtkinter.CTkLabel(app, text=information,
                                           wraplength=400, justify="center",
                                           anchor=customtkinter.W)
information_label.pack(padx=10, pady=10)

# run app
app.mainloop()

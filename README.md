# SentiMap
**Climate change is an urgent and critical global issue that threatens our planet and its inhabitants.**

SentiMap is a data visualization software that allows users to gain crucial insights into public sentiments surrounding climate change. 

It has two functionalities: **display sentiment analysis** and **display carbon emissions analysis**. 
- **Display sentiment analysis** is accomplished by **scraping** Twitter tweets based on country inputted, using **sentiment analysis** to assign a sentiment (from very positive to very negative) to each tweet, and displaying it in a **heatmap**. 
- **Display carbon emissions analysis** is accomplished by **analysing** a country's carbons emissions and displaying it in a **heatmap**. 

### Running the Program 
Download the files and run the **`gui.py`** file.

### Technical Documentation
The **front-end** is constructed with Python's **`TKinter`** module.
- **`gui.py`** contains the main window GUI.

The **back-end** is constructed using **`Folium`** and **`TextBlob`**.
- **`Carbon_map.py`** creates a carbon heatmap using `Folium` by reading a `.csv` file of the country entered.
- **`Sentiment_map.py`** creates a sentiment heatmap using `Folium` by scraping Twitter tweets based on the country entered and assigning sentiments to each tweet using `TextBlob`'s natural language processing capabilities.

## Note:
Sample carbon emissions and sentiment `.csv` files for USA and Canada are provided as testers since we did not have a Twitter API key to access tweets. 

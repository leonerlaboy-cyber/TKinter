from tkinter import *
import requests
import json

def zipLookup():
    # zip.get()
    # zip_label = Label(root, text=zip.get())
    # zip_label.grid(row=1, column=0, columnspan=2)

    try:
        api_request = requests.get('https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=' + zip.get() + '&distance=25&API_KEY=B4EDB910-0C36-4537-88AE-220A6030DDC5')
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']

        if category == 'Good':
            weather_color = 'light green'
        elif category == 'Moderate':
            weather_color = '#FFFF00'
        elif category == 'Unhealthy for Sensitive Groups':
            weather_color = '#ff9900'
        elif category == 'Unhealthy':
            weather_color = '#FF0000'
        elif category == 'Very Unhealthy':
            weather_color = '#990066'
        elif category == 'Hazardous':
            weather_color = '#660000'
        else:
            weather_color = 'white'

        root.configure(background=weather_color)
        my_label.config(text=f'Area: {city}, Air Quality: {quality}, {category}', background=weather_color)

    except Exception as e:
        print(f"API error: {e}")


root = Tk()
root.geometry('600x150')

#https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=07801&distance=25&API_KEY=B4EDB910-0C36-4537-88AE-220A6030DDC5

city = quality = category = 'N/A'
weather_color = ''

# try:
#     api_request = requests.get('https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=07801&distance=25&API_KEY=B4EDB910-0C36-4537-88AE-220A6030DDC5')
#     api = json.loads(api_request.content)
#     city = api[0]['ReportingArea']
#     quality = api[0]['AQI']
#     category = api[0]['Category']['Name']

#     if category == 'Good':
#         weather_color = 'light green'
#     elif category == 'Moderate':
#         weather_color = '#FFFF00'
#     elif category == 'Unhealthy for Sensitive Groups':
#         weather_color = '#ff9900'
#     elif category == 'Unhealthy':
#         weather_color = '#FF0000'
#     elif category == 'Very Unhealthy':
#         weather_color = '#990066'
#     elif category == 'Hazardous':
#         weather_color = '#660000'

#     root.configure(background=weather_color)

#     my_label = Label(root, text=f'Area: {city}, Air Quality: {quality}, {category}', font='Helvetica, 20', background=weather_color)
#     my_label.grid(row=1, column=0, columnspan=2)
# except Exception as e:
    # api = 'Error...'
    # print(f"API error: {e}") 

zip = Entry(root)
zip.grid(row=0, column=0, pady=10, sticky='WENS')

zip_button = Button(root, text='Lookup Zipcode', command=zipLookup)
zip_button.grid(row=0, column=1, sticky='WENS')

my_label = Label(root, font='Helvetica, 20')
my_label.grid(row=1, column=0, columnspan=2)

root.mainloop()
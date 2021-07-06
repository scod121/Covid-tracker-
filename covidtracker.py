# importing libraries

import requests
import bs4
import tkinter as tk

# Request Function # Collecting Data from Web

def get_html_data(url):
    data = requests.get(url)
    return data

# Extracting data from webpage

def get_covid_data():
    url = "https://www.worldometers.info/coronavirus/"
    html_data = get_html_data(url)
    bs = bs4.BeautifulSoup(html_data.text, 'html.parser')
    info_div = bs.find("div", class_="content-inner").findAll("div", id="maincounter-wrap")
    all_data=""

    for block in info_div:
       text = block.find("h1", class_=None).get_text()

       count = block.find("span", class_=None).get_text()

       all_data = all_data + text + "" + count + "\n"

    return all_data

# Extracting country data from webpage # Adding Functionality to GUI

def get_country_data():
    name = textfield.get()
    url = "https://www.worldometers.info/coronavirus/country/"+name;
    html_data = get_html_data(url)
    bs = bs4.BeautifulSoup(html_data.text, 'html.parser')
    info_div = bs.find("div", class_="content-inner").findAll("div", id="maincounter-wrap")
    all_data=""

    for block in info_div:
        try:
            text = block.find("h1", class_=None).get_text()
            count = block.find("span", class_=None).get_text()
            all_data = all_data + text + "" + count + "\n"
        except:
            print("This block does not required")
    mainlabel['text']=all_data

# Reload Function # Adding Functionality to GUI

def reload():
    new_data = get_covid_data()
    mainlabel['text']=new_data

get_covid_data()

# GUI #Creating GUI

root = tk.Tk()
root.geometry("900x700")
root.title("Covid Tracker")
f = ("poppins",25,"bold")

# Covid Logo # Creating GUI

banner = tk.PhotoImage(file="download.png")
bannerlabel = tk.Label(root, image=banner)
bannerlabel.pack()

# Taking country name input # Adding Functionality to GUI

textfield = tk.Entry(root, width = 50)
textfield.pack()

# Display data on GUI # Adding Functionality to GUI

mainlabel = tk.Label(root, text=get_covid_data(), font=f)
mainlabel.pack()

# Get Data button # Adding Functionality to GUI

gbtn = tk.Button(root, text="Get Data", font=f, relief='solid', command=get_country_data)
gbtn.pack()

# Reload button # Adding functionality to GUI
rbtn = tk.Button(root, text="Reload", font=f, relief='solid', command=reload)
rbtn.pack()

root.mainloop()


from flask import Flask
import requests, datetime, csv

app = Flask(__name__)

#receive json response from url
def url_to_json(url):
    try:
        res = requests.get(url)
        return res.json()
    except:
        return "Connection error"

#added helper functions for the rules

#order king alphabatically (by name)
def order_alpha(data):
    return sorted(data,key=lambda x : x['nm'])

#reverse first name
def reverse(name):
    word_list = name.split(' ')
    word_list[0] = word_list[0][::-1] #reverses word as step = -1
    new_name = ' '.join(word_list)
    return new_name

#acronym country names (take only the first letter of each word)
def shorten_country(str):
    word_list = str.split(' ')
    new_str = ''.join([word[0] for word in word_list]) #get first char in every words
    return new_str

#only include starting year they were coronated in
def coronated_year(years):
    year_list = years.split('-')
    return year_list[0]

#Main app
@app.route('/')
def read_url():
    #retreive json
    url = "http://mysafeinfo.com/api/data?list=englishmonarchs&format=json"
    json_list = url_to_json(url)
    json_list = order_alpha(json_list) #order list alphabetically

    #create file for writing
    filename = "king_data.csv"
    csv_file = open(filename, 'w')
    csv_writer = csv.writer(csv_file)
    
    #header of the csv
    header = ["Name","Country", "House", "Year of birth","Ingestion Time"]
    csv_writer.writerow(header)

    for king in json_list:
        #ignore if it is House of Wessex
        if king['hse'] != "House of Wessex":
            row = [reverse(king['nm']), shorten_country(king['cty']),coronated_year(king['yrs']), datetime.datetime.utcnow()]
            csv_writer.writerow(row)

    #close writer
    csv_file.close
    return "Hi! I have made the csv file that you wanted. filename is called: "+filename+".\n"
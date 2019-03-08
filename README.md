# Coding Challenge README
> Name: Gabriel Lee

***

This is the code used with Python and Flask.

### Instructions:
* Clone the project
* Install requirements:
    > pip install -r requirements.txt
* To run the code:
    > FLASK_APP=parseData.py flask run
* Ping the server to get the csv file:
    > curl http://127.0.0.1:5000/

### Notes:
* parseData.js has all the required code needed to tackle this problem.
* A csv file is created once you ping the server (as instructed above)

### Methods Used:
* uses 'requests' to get json response from the url
* After getting the json data, I made adjustments to it based on the rules I was given
    * the data is first sorted based on the first name
    * In the loop where we go through every king, we ignore any king with "House of Wessex"
        * we have helper function to handle all the other rules (reversing first name, acronyms, coronated year)

### Improvements to make:
* Ability to customize (like adding additional restraints) by using Post Requests (retreive data from user)
    * Following the idea above, we could save any changes the user made so that the next time they run the tool, it remembers.
* Store the json data from URL in case the site is down. That way, if the tool recognizes that the site can't be loaded, it'll use the stored data instead.
* Possibly have passwords or an authentication key to use the api (so that the public can't access it)
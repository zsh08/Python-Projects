import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "zahra.shadmani@outlook.com" # my email address to send recieve notifications
MY_PASSWORD = "qy123" #password (not the real one)
MY_LAT = 51.507351 # My latitude in London
MY_LONG = -0.127758 # My longitude in London

# Function to check if the ISS is overhead.
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status() # Raise an exception if there is an error with the request.
    data = response.json() 

     # Extract the current ISS latitude and longitude from the data.
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #position is within +5 or -5 degrees of the iss position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True # if iss is overhead then return true

# Function to check if it is currently nighttime at my location.
def is_night():
    # Define parameters for the sunrise-sunset API using my latitude and longitude
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0, # Set 'formatted' to 0 for time in 24-hour format.
    }
    # Make a GET request to the sunrise-sunset API with the parameters.
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status() # Raise an exception if there is an error with the request.
    data = response.json()

    # Extract sunrise and sunset times, isolating the hour from the time string
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    # Get the current hour of the day.
    time_now = datetime.now().hour

    # Return True if it is night (after sunset or before sunrise).
    if time_now >= sunset or time_now <= sunrise: 
        return True


while True:
    time.sleep(60)  #Wait for 60 seconds before running the loop again.

    if is_iss_overhead() and is_night():  # Check if the ISS is overhead and it is nighttime.
        connection = smtplib.SMTP("smtp.outlook.com")  # Establish a secure connection to the email server.
        connection.starttls() # Start TLS encryption for the email connection.
        connection.login(MY_EMAIL, MY_PASSWORD)  # Login to my email account.
        connection.sendmail(   # Send an email notification to myself that the ISS is overhead.
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up👆\n\nThe ISS is above you in the sky."
        )



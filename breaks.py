# Open the browser
import webbrowser
webbrowser.open('http://google.co.kr', new=2)

# Make the program wait for a certain period of time
import time

time.sleep(10)
webbrowser.open('https://www.youtube.com/watch?v=IQexGzI_paE', new = 2)

# A loop to make the user take a break after every 20mins

breaks = 3

for i in range(breaks):
    time.sleep(20*60)
    webbrowser.open('http://google.co.kr', new=2)
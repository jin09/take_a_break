import webbrowser
import time

print("This program started on "+time.ctime())  #
i=0
while(i<3):
    time.sleep(2) #10 seconds
    webbrowser.open("https://www.youtube.com/watch?v=BgyqAD5Z6_A")
    i=i+1

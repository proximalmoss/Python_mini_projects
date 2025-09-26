from datetime import datetime
import pygame
import time
pygame.mixer.init()
alarm_time=input("Enter the time of alarm to be set:HH:MM:SS\n")
alarm_hour=alarm_time[0:2]
alarm_minute=alarm_time[3:5]
alarm_second=alarm_time[6:8]
alarm_period=alarm_time[9:11].upper()

print("Setting up alarm..")
while True:
    now=datetime.now()
    current_hour=now.strftime("%I") #current hour (12-hr format)
    current_minute=now.strftime("%M") #current minute
    current_seconds=now.strftime("%S") #current second
    current_period=now.strftime("%p") #gives AM/PM
    if (alarm_period==current_period):
        if (alarm_hour==current_hour):
            if (alarm_minute==current_minute):
                if (alarm_second==current_seconds):
                    print("WAKE UP!!")
                    pygame.mixer.music.load('audio.mp3')
                    pygame.mixer.music.play()
                    break
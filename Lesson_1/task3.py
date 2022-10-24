try:
    value = int(input("Enter value(seconds): "))
    if value < 0: quit()
    days = value // 86400
    hours = value // 3600 % 24
    minutes = value // 60 % 60
    seconds = value % 60
    print ("Days: " + str(days) + "| Hours: " + str(hours) + "| Minutes: " + str(minutes) + "| Seconds: " + str(seconds))
except:
    print ("Invalid value")
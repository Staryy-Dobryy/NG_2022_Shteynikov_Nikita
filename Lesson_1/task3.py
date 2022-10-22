try:
    value = int(input("Enter value(seconds): "))
    if value < 0: quit()
    print ("Days: " + str(value // 86400) + "| Hours: " + str(value // 3600 % 24) + "| Minutes: " + str(value // 60 % 60) + "| Seconds: " + str(value % 60))
except:
    print ("Invalid value")
try:
    a = int(input("Enter first coefficient: "))
    b = int(input("Enter second coefficient: "))
    c = int(input("Enter third coefficient: "))
    if a < 0: quit();
    print ("Result: " , end="")
    if a != 0 and b != 0 and c != 0:
        d = b ** 2 - 4 * a * c
        if d < 0: quit()
        if d > 0:
            x1 = (-b+d**(1/2))/(2*a)
            x2 = (-b-d**(1/2))/(2*a)
            print ("x1=" + str(x1) + " |x2=" + str(x2))
        elif d == 0: 
            x = -b/(2*a)
            print ("x=" + str(x))
    elif a != 0 and b != 0:
        x1 = 0
        x2 = -b/a
        print ("x1=" + str(x1) + " |x2=" + str(x2))
    elif a != 0 and c != 0:
        if c > 0: quit()
        x1 = (-c/a)**(1/2)
        x2 = -((-c/a)**(1/2))
        print ("x1=" + str(x1) + " |x2=" + str(x2))
except:
    print ("Invalid value")
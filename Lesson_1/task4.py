try:
    coefficientA = int(input("Enter first coefficient: "))
    coefficientB = int(input("Enter second coefficient: "))
    coefficientC = int(input("Enter third coefficient: "))
    if coefficientA < 0: quit();
    print ("Result: " , end="")
    d = coefficientB ** 2 - 4 * coefficientA * coefficientC
    if d < 0: quit()
    if d > 0:
        x1 = (-coefficientB+d**(1/2))/(2*coefficientA)
        x2 = (-coefficientB-d**(1/2))/(2*coefficientA)
        print ("x1=" + str(x1) + " |x2=" + str(x2))
    elif d == 0: 
        x = -coefficientB/(2*coefficientA)
        print ("x=" + str(x))
except:
    print ("Invalid value")
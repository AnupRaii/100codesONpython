
x, y = map(int, list(input("Insert the value for variable X and Y : ").split(" ")))

if x > 0 and y > 0:
    print("point (", x, ",", y, ") lies in the First quadrant")

elif x < 0 and y > 0:
    print("point (", x, ",", y, ") lies in the Second quadrant")


elif x < 0 and y < 0: 
    print("point (", x, ",", y, ") lies in the Third quadrant")

elif x > 0 and y < 0:
    print("point (", x, ",", y, ") lies in the Fourth quadrant
elif x == 0 and y == 0:
    print("point (", x, ",", y, ") lies at the origin")


elif y == 0 and x != 0:
    print("point (", x, ",", y, ") on x-axis")

elif x == 0 and y != 0:
    print("point (", x, ",", y, ") on at y-axis")

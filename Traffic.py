

# Traffic
import time

directions = ["NORTH", "SOUTH", "EAST", "WEST"]
signal = ["RED", "ORANGE", "GREEN", "FREE LEFT", "RIGHT"]

def timer(t):
    for i in range(t, 0, -1):
        print("Time:", i)
        time.sleep(1)

while True:

    # MODE INPUT
    while True:
        mode = input("Do you want manual or automatic mode:\n'M' for manual / 'A' for automatic: ").upper()

        if mode in ["M", "A"]:
            break
        else:
            print("Please enter a valid option")

    # MANUAL MODE
    if mode == "M":

        # DIRECTION INPUT
        while True:
            direction = input("Enter the Direction (North/South/East/West): ").upper()
            if direction in directions:
                break
            else:
                print("Please enter a valid direction")

        # SIGNAL INPUT
        while True:
            signals = input("Enter the signal (Red/Orange/Green/Free left/Right): ").upper()
            if signals in signal:
                break
            else:
                print("Please enter a valid signal")

        print("\nTraffic Signal Status\n")

        # RIGHT
        if signals == "RIGHT":
            print(direction, ": TURN RIGHT GREEN, FREE LEFT")

            for d in directions:
                if d != direction:
                    print(d, ": RED, FREE LEFT")

            timer(10)

        # RED
        elif signals == "RED":

            if direction in ["NORTH", "SOUTH"]:
                for d in ["NORTH", "SOUTH"]:
                    print(d, ": RED, FREE LEFT")

                for d in ["EAST", "WEST"]:
                    print(d, ": GREEN, FREE LEFT")

            else:
                for d in ["EAST", "WEST"]:
                    print(d, ": RED, FREE LEFT")

                for d in ["NORTH", "SOUTH"]:
                    print(d, ": GREEN, FREE LEFT")

            timer(10)

        # ORANGE
        elif signals == "ORANGE":

            if direction in ["NORTH", "SOUTH"]:
                for d in ["NORTH", "SOUTH"]:
                    print(d, ": ORANGE, FREE LEFT")

                for d in ["EAST", "WEST"]:
                    print(d, ": RED, FREE LEFT")

            else:
                for d in ["EAST", "WEST"]:
                    print(d, ": ORANGE, FREE LEFT")

                for d in ["NORTH", "SOUTH"]:
                    print(d, ": RED, FREE LEFT")

            timer(5)

        # GREEN
        elif signals == "GREEN":

            if direction in ["NORTH", "SOUTH"]:
                for d in ["NORTH", "SOUTH"]:
                    print(d, ": GREEN, FREE LEFT")

                for d in ["EAST", "WEST"]:
                    print(d, ": RED, FREE LEFT")

            else:
                for d in ["EAST", "WEST"]:
                    print(d, ": GREEN, FREE LEFT")

                for d in ["NORTH", "SOUTH"]:
                    print(d, ": RED, FREE LEFT")

            timer(10)

    # AUTOMATIC MODE
    elif mode == "A":

        while True:
            print("\nTraffic Signal Status\n")

# North Right 
            print("NORTH : TURN RIGHT GREEN, FREE LEFT")
            print("SOUTH : RED, FREE LEFT")
            print("EAST : RED, FREE LEFT")
            print("WEST : RED, FREE LEFT")
            timer(5)
        
# North South Green
            print("NORTH : GREEN, FREE LEFT")
            print("SOUTH : GREEN, FREE LEFT")
            print("EAST : RED, FREE LEFT")
            print("WEST : RED, FREE LEFT")
            timer(5)

# South Right         
            print("NORTH : RED, FREE LEFT")
            print("SOUTH : TURN RIGHT GREEN, FREE LEFT")
            print("EAST : RED, FREE LEFT")
            print("WEST : RED, FREE LEFT")
            timer(5)
                 

# North South Orange
            print("NORTH : ORANGE, FREE LEFT")
            print("SOUTH : ORANGE, FREE LEFT")
            print("EAST : RED, FREE LEFT")
            print("WEST : RED, FREE LEFT")
            timer(5)

# East Right
            print("NORTH : RED, FREE LEFT")
            print("SOUTH : RED, FREE LEFT")
            print("EAST : TURN RIGHT GREEN, FREE LEFT")
            print("WEST : RED, FREE LEFT")
            timer(5)         

# East West Green
            print("NORTH : RED, FREE LEFT")
            print("SOUTH : RED, FREE LEFT")
            print("EAST : GREEN, FREE LEFT")
            print("WEST : GREEN, FREE LEFT")
            timer(5)

# West Right
            print("NORTH : RED, FREE LEFT")
            print("SOUTH : RED, FREE LEFT")
            print("EAST : RED, FREE LEFT")
            print("WEST : TURN RIGHT GREEN, FREE LEFT")
            timer(5)         

#East West Orange

            print("NORTH : RED, FREE LEFT")
            print("SOUTH : RED, FREE LEFT")
            print("EAST : ORANGE, FREE LEFT")
            print("WEST : ORANGE, FREE LEFT")
            timer(5)

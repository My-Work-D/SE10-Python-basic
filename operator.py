class Operator:
    def check_wheel_count(self):
        count = int(input("Input the wheel count: "))  # Get user input and convert to integer

        if count == 1:
            print("Wheel Barrow")
        elif count == 2:
            print("Bicycle")
        elif count == 3:
            print("Three Wheel")
        elif count == 4:
            print("Car")
        else:
            print("Not recognized as a Vehicle")


# Create an instance of the Operator class and call the method
operator = Operator()
operator.check_wheel_count()

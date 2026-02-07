import time

#Just print out thre dots with a delay for a cool show
def ThreeDots():
    three_dots = "..."
    for char in three_dots:
        print(char,end="",flush=True)
        time.sleep(0.3)
    print("\n")

##################################################################################################################################
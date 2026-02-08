import time

#Just print out thre dots with a delay for a cool show
def threedots():
    three_dots = "..."
    for char in three_dots:
        print(char,end="",flush=True)
        time.sleep(0.3)
    print("\n")

##################################################################################################################################


#print out names slowly for fancyness
def coolPrint(text, sleep = 0.1):
    for char in text:
        print(char, end ="",flush = True)
        time.sleep(sleep)


##################################################################################################################################
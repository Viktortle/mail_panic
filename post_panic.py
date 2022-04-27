from random import randint, choice
from time import sleep

class Client:
    def __init__(self, name : str, errands : int):
        self.name = name
        self.errands = errands
    
    def get_name(self):
        return self.name

    def get_errands(self):
        return self.errands

def random_errands():
    # Randomizes number of errands a client has
    number_of_errands = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4]
    return choice(number_of_errands)

def time_passage(hour, closing_hour):
    # Defining the variables for the loop
    queue = []
    total_errands = 0
    total_clients = []
    serving = 0
    minutes = 0

    # Main loop of the program which will 
    while hour < closing_hour or len(queue) > 0 or serving > 0:
        #sleep(0.14)
        print(f'\n{hour}:{minutes}:')
        # Checks if there is a client entering this minute or not as well as putting them in the queue
        if randint(1,5) == 1:
            queue.append(Client(f"Client {len(total_clients) + 1}", random_errands()))
            total_clients.append(queue[-1])
            total_errands += total_clients[-1].get_errands()

            if len(queue) == 1:
                print(f"{queue[0].get_name()} was the only one in the queue, they come to the front desk right away.")
                serving = queue.pop(0).get_errands() * 2
            elif serving > 0:
                print(f"{queue[-1].get_name()} joins the queue as number {len(queue)}.")

        # Cashier works on the active errand
        serving -= 1

        # Counts minutes and hours
        minutes += 1
        if minutes == 60:
            minutes = 0
            hour += 1
        if hour == 24:
            hour = 0

    # Summarize the statistics of the day
    return f"Total number of errands: {total_errands}\nTotal number of clients: {len(total_clients)}"

def main():
    print("Welcome to the mail office!")
    running = True
    opening_hour = 9
    closing_hour = 18
    while running:

        choice = input("Would you like to change the opening hour? (y/n)\nEnter here: ")
        if choice == "y":
            opening_hour = int(input("What will be the new opening hour?\nEnter here: "))
            if opening_hour <= 0 or opening_hour >= 22:
                opening_hour = int(input("Stop joking and enter an actual hour. . .\nEnter here: "))
        else: print("The opening hour of the office will be 09:00")

        choice = input("\nWould you like to change the closing hour? (y/n)\nEnter here: ")
        if choice == "y":
            closing_hour = int(input("What will be the new closing hour?\nEnter here: "))
            if closing_hour <= 0 or closing_hour >= 24:
                closing_hour = int(input("Stop joking and enter an actual hour. . .\nEnter here: "))
        else: print("The closing hour of the office will be 18:00")

        print(time_passage(opening_hour, closing_hour))

        choice = input("Do you wish to simulate another day at the office? (y/n)\nEnter here: ")
        if choice == "n":
            running = False
    else:
        print("See you another time!")
    
if __name__ == "__main__":
    main()
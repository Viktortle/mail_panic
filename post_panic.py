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
    # Sannolikheten för ärenden
    number_of_errands = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4]
    return choice(number_of_errands)

def time_passage(hour, minutes, closing_hour):
    # Definerar loopens variabler
    time_pass = sleep(1)
    queue = []
    total_errands = 0
    total_clients = []
    serving = 0

    # Startar arbetsdagen
    while hour < closing_hour or len(queue) > 0:
        time_pass
        # Kontrollerar om det kommer någon eller inte och ställer dem i kö
        if randint(1,5) == 1:
            queue.append(Client(f"Client {len(total_clients) + 1}", random_errands()))
            total_clients.append(queue[-1])
            total_errands += total_clients[-1].get_errands()
            if len(queue) == 1:
                print(f"{queue[0].get_name()} was the only one in the queue, they come to the front desk right away.\n")
                serving = queue.pop(0).get_errands() * 2
            elif serving > 0:
                print(f"{queue[-1].get_name()} joins the queue as number {len(queue)}.\n")

        # Kassören arbetar med ärenden
        serving -= 1

        # Räkna minuter och timmar
        minutes += 1
        if minutes == 60:
            minutes = 0
            hour += 1
        if hour == 24:
            hour = 0

    # Sammanställer dagens statistik
    return f"Total number of errands: {total_errands}\n Total number of clients: {len(total_clients)}"


def main():

    print("Welcome to the mail office!")
    running = True
    hour = 9
    minutes = 0
    closing_hour = 18
    while running:

        choice = input("Would you like to change the opening hour? (y/n)\nEnter here: ")
        if choice == "y":
            hour = input("What will be the new opening hour?\nEnter here: ")
        else: print("The opening hour of the office will be 09:00")

        choice = input("Would you like to change the closing hour? (y/n)\nEnter here: ")
        if choice == "y":
            closing_hour = input("What will be the new closing hour?\nEnter here: ")
        else: print("The closing hour of the office will be 18:00")

        print(time_passage(hour, minutes, closing_hour))
    
if __name__ == "__main__":
    main()
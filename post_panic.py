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
    number_of_errands = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4]
    return choice(number_of_errands)

def main():
    hour = 9
    minutes = 0
    time_pass = sleep(1)
    queue = []
    total_errands = 0
    total_clients = []
    serving = 0

    while hour < 18 or len(queue) > 0:
        time_pass
        if randint(1,5) == 1:
            queue.append(Client(f"Client {len(total_clients) + 1}", random_errands()))
            total_clients.append(queue[-1])
            total_errands += total_clients[-1].get_errands()
            if len(queue) == 1:
                print(f"{queue[0].get_name()} was the only one in the queue, they come to the front desk right away.")
                serving = queue.pop(0).get_errands() * 2
            elif serving > 0:
                print(f"{queue[-1].get_name()} joins the queue as number {len(queue)}.")
        serving -= 1
        minutes += 1
        if minutes == 60:
            minutes = 0
            hour += 1
    else:
        print(f"Total number of errands: {total_errands}\n Total number of clients: {len(total_clients)}")

if __name__ == "__main__":
    main()
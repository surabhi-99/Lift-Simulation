#Source website link: https://docs.python.org/3/ which is Python's official documentation 
class Lift:
    def __init__(self, lift_id, max_floors):
        self.id = lift_id
        self.current_floor = 0
        self.state = 'CLOSE'
        self.max_floors = max_floors
        self.destination_queue = []
        self.time_taken = 0

    def add_request(self, start_floor, dest_floor):
        # Adding a request to the destination queue
        self.destination_queue.append((start_floor, dest_floor))

    def process_next_request(self):
        if not self.destination_queue:
            return False  # No request to process
        
        start_floor, dest_floor = self.destination_queue.pop(0)
        self.move_to_floor(start_floor)
        self.open_and_close_door()  # Opening door to let passenger in
        self.move_to_floor(dest_floor)
        self.open_and_close_door()  # Opening door to let passenger out
        return True

    def move_to_floor(self, floor):
        # Moving the lift to the specified floor
        while self.current_floor != floor:
            if self.current_floor < floor:
                self.current_floor += 1
            else:
                self.current_floor -= 1
            self.time_taken += 1  # Each move takes 1 unit of time

    def open_and_close_door(self):
        self.state = 'OPEN'
        self.time_taken += 1  # Opening door takes 1 unit of time
        self.state = 'CLOSE'
        self.time_taken += 1  # Closing door takes 1 unit of time


class Building:
    def __init__(self, num_lifts, num_floors):
        self.lifts = [Lift(i, num_floors) for i in range(num_lifts)]
        self.num_floors = num_floors

    def dispatch_request(self, start_floor, dest_floor):
        # To find the best lift to handle the request
        selected_lift = min(self.lifts, key=lambda lift: abs(lift.current_floor - start_floor))
        selected_lift.add_request(start_floor, dest_floor)

    def simulate(self):
        for lift in self.lifts:
            while lift.process_next_request():
                pass

def main():
    # Inputs
    num_lifts = int(input("No of Lifts: "))
    num_floors = int(input("No of Floors: "))

    building = Building(num_lifts, num_floors)
    
    requests = [
        (0, 7),
        (3, 0),
        (4, 6)  
    ]

    for start_floor, dest_floor in requests:
        building.dispatch_request(start_floor, dest_floor)

    building.simulate()

    # Output simulation results
    for lift in building.lifts:
        print(f"LIFT {lift.id}: {lift.time_taken} SECONDS")

if __name__ == "__main__":
    main()

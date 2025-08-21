# Virtual Train Route Planner (Simple Version)

class Station:
    def __init__(self, name):
        self.name = name
        self.next = None
        self.prev = None


class TrainRoute:
    def __init__(self):
        self.head = None
        self.current = None

    def add_station(self, name):
        new_station = Station(name)
        if not self.head:
            self.head = new_station
            self.head.next = self.head
            self.head.prev = self.head
            self.current = self.head
        else:
            last = self.head.prev
            last.next = new_station
            new_station.prev = last
            new_station.next = self.head
            self.head.prev = new_station
        print(f"Station '{name}' added.")

    def show_route(self):
        if not self.head:
            print("No stations in the route.\n")
            return
        curr = self.head
        print("Train Route:")
        while True:
            print(f"- {curr.name}")
            curr = curr.next
            if curr == self.head:
                break
        print()

    def move_forward(self):
        if not self.current:
            print("No route available.\n")
            return
        self.current = self.current.next
        print(f"🚆 Moved forward to: {self.current.name}\n")

    def move_backward(self):
        if not self.current:
            print("No route available.\n")
            return
        self.current = self.current.prev
        print(f"🚆 Moved backward to: {self.current.name}\n")

    def current_station(self):
        if not self.current:
            print("No current station.\n")
        else:
            print(f"📍 You are at: {self.current.name}\n")


def main():
    route = TrainRoute()

    while True:
        print("1. Add Station")
        print("2. Show Route")
        print("3. Current Station")
        print("4. Move Forward")
        print("5. Move Backward")
        print("6. Exit")
        choice = input("Choose option: ")

        if choice == "1":
            name = input("Station name: ")
            route.add_station(name)
        elif choice == "2":
            route.show_route()
        elif choice == "3":
            route.current_station()
        elif choice == "4":
            route.move_forward()
        elif choice == "5":
            route.move_backward()
        elif choice == "6":
            break
        else:
            print("Invalid choice.\n")


if __name__ == "__main__":
    main()

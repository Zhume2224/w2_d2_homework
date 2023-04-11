
# from src import bus_stop
#note: this is important


class Bus:
    def __init__(self,route_number,destination):
        self.route_number=route_number
        self.destination=destination
        self.passengers=[]

    def drive(self):
        return "Brum brum"

    def passenger_count(self):
        return len(self.passengers)

    def pick_up(self,person_added):
        self.passengers.append(person_added)


    def drop_off(self,person_removed):
        self.passengers.remove(person_removed)

    def empty_bus(self):
        self.passengers.clear()

   #note difficult. logic wriiten in bus_test.py
    def pick_up_from_stop(self,busstop):
        for pax in busstop.queue:
            self.passengers.append(pax)
        


        
        


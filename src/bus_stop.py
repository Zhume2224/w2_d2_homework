class BusStop:
    def __init__(self,name):
        self.name=name
        self.queue=[] 
        #note:will get filled with instances of the Person class.

    def add_to_queue(self,person):
        self.queue.append(person)

    def remove_from_queue(self,person):
         self.queue.remove(person)



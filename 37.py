# building with 15 floors and the first floor reserved for 
# the ground floor (described simply as "1").

class Elevator():
    def __init__(self, person: str) -> None:
        self.person = person
        self.actual_floor = 1

    def up(self):
        if self.actual_floor < 15:
            self.actual_floor += 1
            print(f"{self.person} is going up to the {self.actual_floor} floor")
        else:
            print(f"{self.person} He's already on the top floor and can't go \
any higher.")
    
    def down(self):
        if self.actual_floor > 1:
            self.actual_floor -= 1
            print(f"{self.person} is going down to the {self.actual_floor} \
floor")
        else:
            print(f"{self.person} He's already on the first floor and can't go \
any lower.")


person1 = Elevator('Kai')
person1.down()
person1.up()

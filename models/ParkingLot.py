from .Car import Car

class ParkingLot:
    def __init__(self, slotsCount):
        self.slotsCount = 0
        self.slots = []
        for i in range(slotsCount):
            self.slots.append(None)
        print("Created a parking lot with", slotsCount, "slots")

    def park(self, regNo, color):
        index = 0        
        while index < len(self.slots):            
            if self.slots[index] is None:
                break
            index = index + 1

        if index >= len(self.slots):
            print("Sorry, parking lot is full")
            return
        else:
            self.slots[index] = Car(regNo, color)
            self.slotsCount = self.slotsCount + 1
            print("Allocated slot number:", (index+1))

    def leave(self, slotNo):
        if self.slots[slotNo-1] is not None:
            self.slots[slotNo-1] = None
            self.slotsCount = self.slotsCount - 1
        print("Slot number", slotNo, "is free")

    def status(self):
        if self.slotsCount > 0:
            print("Slot No.\tRegistration No\tColour")
        for i in range(len(self.slots)):
            if self.slots[i] is not None:
                row = str(i+1) + '\t' + self.slots[i].getRegNo() + '\t' + self.slots[i].getColor()
                print(row)

    def registrationNumbersForCarsWithColour(self, color):
        ans = ""
        for car in self.slots:
            if car is not None and car.getColor() == color:
                if ans == "":
                    ans = car.getRegNo()
                else:
                    ans = ans + ", " + car.getRegNo()
        print(ans)

    def slotNumbersForCarsWithColour(self, color):
        ans = ""
        for i in range(len(self.slots)):
            if self.slots[i] is not None and self.slots[i].getColor() == color:
                if ans == "":
                    ans = str(i+1)
                else:
                    ans = ans + ", " + str(i+1)
        print(ans)

    def slotNumberForRegistrationNumber(self, regNo):        
        for i in range(len(self.slots)):
            if self.slots[i] is not None and self.slots[i].getRegNo() == regNo:
                print(str(i+1))
                return
        print("Not found")

## ===== Imported Module(s) =====
import sys
from utils.validate import validateInput
from models.ParkingLot import ParkingLot

## ===== Global Variable(s) =====
myParkingLot = None

## ===== Main Function(s) =====
def processQuery(type, query):    
    if type == 'create_parking_lot':
        global myParkingLot
        myParkingLot= ParkingLot(int(query[0]))
    if type == 'park':
        myParkingLot.park(query[0], query[1])
    if type == 'leave':
        myParkingLot.leave(int(query[0]))
    if type == 'status':
        myParkingLot.status()
    if type == 'registration_numbers_for_cars_with_colour':
        myParkingLot.registrationNumbersForCarsWithColour(query[0])
    if type == 'slot_numbers_for_cars_with_colour':
        myParkingLot.slotNumbersForCarsWithColour(query[0])
    if type == 'slot_number_for_registration_number':
        myParkingLot.slotNumberForRegistrationNumber(query[0])

def main(argv):
    try:
        inputFile = open('functional_spec/fixtures/file_input.txt')
        inputs = inputFile.readlines()
        for input in inputs:
            query = input.split(' ')
            validateInput(query)

            # preProcess the inputs
            for i in range(len(query)):
                query[i] = query[i].replace('\n', '')
                query[i] = query[i].replace('\t', '')
                query[i] = query[i].replace('\r', '')
            type = query[0]
            params = query[1:]
            processQuery(type, params)
    except Exception as e:
        print(e)

if __name__ == "__main__":
   main(sys.argv)

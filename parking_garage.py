import random

class ParkingGarage():

    """A simple Class to model a parking garage with payments and space numbers"""
    def __init__(self):
        self.tickets = [] #Actually make this a randomly generated list of 4 digit numbers
        self.parkingSpaces = [] #Could randomly generate numbers as strings between 1 - 99
        while len(set(self.parkingSpaces)) < 10:
            self.parkingSpaces.append(str(random.randint(1,100)))
        list(set(self.parkingSpaces))
        while len(set(self.tickets)) < 10: #Removes duplicates and adds new numbers
            self.tickets.append(str(random.randint(1000,10000)))
        list(set(self.parkingSpaces))
        self.currentTicket = {}        

    def takeTicket(self):
        for x in self.parkingSpaces:
            print(x)
        while True:
            space = input('Please choose a space from the list above. ')
            if space in self.parkingSpaces:
                break
            else:
                print('Sorry, that space is not available.')
        number = self.tickets.pop()# 4 digit number pops off of randomly generated list
        print('Your ticket # is ' + number + '. Please save it for reference.')
        self.currentTicket[number] = [False, self.parkingSpaces.pop(self.parkingSpaces.index(space))]
        print('Please pay your ticket when ready.')

    def payForParking(self):
        number = input('What is your ticket number? ')
        try:
            if self.currentTicket[number][0] is True:
                '\nYour ticket has already been paid.'
            else:
                print('\nYour space is number ' + self.currentTicket[number][1] + '.')
                payment = input('$2.40/hr. How much would you like to pay? ')
                if '$' in payment: #Ensures that $ is in user input
                    print('Ticket has been paid, thank you. You have 15 minutes to leave.')
                    self.currentTicket[number][0] = True
                else:
                    print('You need to enter a valid dollar amount. Please try again.')
        except:
            print('That ticket number does not exist.')

    def leaveGarage(self):
        number = input('What is your ticket number? ')
        try:
            print('Your space is number ' + self.currentTicket[number][1] + '.')
            if self.currentTicket[number][0] is True:
                print('\nYour ticket has been paid and you may leave. Thank you, have a nice day!')
                self.parkingSpaces.append(self.currentTicket[number][1]) 
                self.tickets.append(number) #Moves space number and ticket # back to list of spaces
                del self.currentTicket[number] #deletes the ticket from the dictionary
            else:
                print('You have not yet paid. Please do so.')
        except:
            print('That ticket number does not exist.')

bo_park = ParkingGarage()

while True:
    response = input('\nWhat would you like to do? You can:\nPark and take a \
ticket by typing "park," \nPay for parking with "pay,"\nexit the garage \
with "exit,"\nLeave this program with "end." ')
    if response == 'end':
        break
    if response == 'park':
        bo_park.takeTicket()
    if response == 'pay':
        bo_park.payForParking()
    if response == 'exit':
        bo_park.leaveGarage()
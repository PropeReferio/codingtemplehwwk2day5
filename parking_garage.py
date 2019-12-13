#Your parking gargage class should have the following methods:
#- takeTicket
#- This should decrease the amount of tickets available by 1
#- This should decrease the amount of parkingSpaces available by 1
#- payForParking
#- Display an input that waits for an amount from the user and store it in a variable
#- If the payment variable is not empty then -> display a message to the user that their ticket has been paid and they have 15mins to leave
#- This should update the "currentTicket" dictionary key "paid" to True
#- leaveGarage
#- If the ticket has been paid, display a message of "Thank You, have a nice day"
#- If the ticket has not been paid, display an input prompt for payment
#- Once paid, display message "Thank you, have a nice day!"
#- Update parkingSpaces list to increase by 1
#- Update tickets list to increase by 1

#You will need a few attributes as well:
#- tickets -> integer
#- parkingSpaces -> list of str numbers
#- currentTicket -> dictionary
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
        self.currentTicket[number] = [False, self.parkingSpaces.pop(self.parkingSpaces.index(space))] #Use remove and append if it doesn't work
        print('Please pay your ticket when ready.')
        #Need pop method to move parking space # from list to dictionary

    def payForParking(self):
        number = input('What is your ticket number? ')
        try:
            if self.currentTicket[number][0] is True:
                'Your ticket has already been paid.'
            else:
                print('Your space is number ' + self.currentTicket[number][1] + '.')
                payment = input('$2.40/hr. How much would you like to pay? ')
                if '$' in payment:
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
                print('Your ticket has been paid and you may leave. Thank you, have a nice day!')
                self.parkingSpaces.append(self.currentTicket[number][1])
                self.tickets.append(number)
                del self.currentTicket[number]
            else:
                print('You have not yet paid. Please do so.')
        except:
            print('That ticket number does not exist.')
    #- If the ticket has been paid, display a message of "Thank You, have a nice day"
#- If the ticket has not been paid, display an input prompt for payment
#- Once paid, display message "Thank you, have a nice day!"
#- Update parkingSpaces list to increase by 1
#- Update tickets list to increase by 1
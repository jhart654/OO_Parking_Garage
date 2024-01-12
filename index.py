class parkingGarage:
    pass
    

    def __init__(self, tickets, parkingSpaces, currentTickets):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTickets = currentTickets
        self.currentTickets = {
            'Paid' : "False"
        }
         

    def takeTicket(self):
        self.tix = int(input('How many tickets would you like to purchase? '))
        self.availableTix = self.tickets - self.tix
        self.availableSpaces = self.parkingSpaces - self.tix
        
        
    def payForParking(self):
        print(f'You have selected to purchase {self.tix} parking ticket(s).')
        self.payment = self.tix * 5
        print(f'Your total is ${self.payment}')
        while True:
            self.checkout = int(input('Please pay full amount. $'))
            self.total = 0
            self.total = self.payment - self.checkout
            if self.total > 0:
                print(f'You have ${self.total} left to pay.')
            elif self.total == 0:
                self.currentTickets['Paid'] = 'True'
                break
   
        print('Your ticket has been paid. You now have 15 minutes to exit the garage')        
        

    def leaveGarage(self):
        if self.total == 0:
            print('Thank You, have a nice day')
        else:
            input('Please make payment: $ ')
            print('Thank you, have a nice day')
        self.availableSpaces += self.tix 
        self.availableTix += self.tix 
        print(f'Available Spaces: {self.availableSpaces}')
        print(f'Available Tickets: {self.availableTix}')

garage1 = parkingGarage(300, 300, 0)
garage1.takeTicket() 
garage1.payForParking()
garage1.leaveGarage()
            

    


'''
traveller class
attribute - name , destination , fare per person
method - calculate fare of total number of persons

'''

class Traveller:
    def __init__(self,name,destination,fareperperson):
        self.name=name
        self.destination=destination
        self.fareperperson=fareperperson

    def calculatefare(self,numberofpersons):
        print (self.fareperperson*numberofpersons)
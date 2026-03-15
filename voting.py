#voting eligibility
class VotingEligibility :
    def __init__(self):
        self.name = input("Enter your name:")
        self.age = int(input("Enter your age:"))
    def candidate(self):
        if self.age < 18 :
            print("you are not eligible")
        else :
            print("you are eligible")
obj1 = VotingEligibility()
obj1.candidate()

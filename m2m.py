import random

"""The crew is made up of character objects"""


class Crew(object):
    def __init__(self, full_crew_b=True):
        if full_crew_b:
            self.crew_roles = full_crew_list
        else:
            self.crew_roles = limited_crew_list

        self.full_crew = {}
        for role in self.crew_roles:
            self.full_crew[role] = Character(role, self.crew_roles)

    def char_select(self, crew_role):
        return self.full_crew[crew_role]

    def list_crew(self):
        for crewmember in self.full_crew:
            print self.full_crew[crewmember]

"""
Character objects store trait, description, and flag/trigger information about specific characters
Because the characters are part of an emergent story (hopefully), they will change with time.
"""


class Character(object):
    def __init__(self, role, crew_reference):
        self.name = ""
        self.name_val_1 = random.randint(0, len(first_names)-1)
        self.name_val_2 = random.randint(0, len(last_names)-1)
        self.name = first_names.pop(self.name_val_1) + " " + last_names.pop(self.name_val_2)
        self.role = role.lower()
        self.role_description = ""
        self.traits = []

        self.role_description = role_description[self.role]
        self.traits = role_trait_base[self.role]

        for i in range(len(self.traits)):
            self.traits[i] = self.traits[i] + random.randint(1, 2)

        self.INTELLIGENCE = self.traits[0]
        self.PHYSICAL = self.traits[1]
        self.MECHANICAL = self.traits[2]
        self.SCIENCE = self.traits[3]
        self.LEADERSHIP = self.traits[4]
        self.CHARISMA = self.traits[5]

        self.opinion = {}
        for role in crew_reference:
            self.opinion[role] = random.randint(0, 5) + 1

        for role in self.opinion:
            if role == self.role:
                self.opinion[role] = 99

        self.enemyList = {}
        for role in crew_reference:
            self.enemyList[role] = False

        self.strain = 0

    def __repr__(self):
        return self.name + ": " + self.role.capitalize() + " - " + self.role_description + ". Stats: " + str(self.traits) + '\n'

    def check_rel(self, other):
        if self.opinion[other] == 99:
            return "N/A"
        elif self.opinion[other] > 5:
            return "friendly"
        elif self.opinion[other] > 0:
            return "good"
        elif self.opinion[other] == 0:
            return "neutral"
        elif self.opinion[other] < -5:
            return "sour"
        else:
            return "hostile"

    def lower_rel(self, other, amount=1):
        self.opinion[other] -= amount

    def raise_rel(self, other, amount=1):
        self.opinion[other] += amount

    def become_enemy(self, other):
        if other in self.enemyList:
            self.enemyList[other] = True
        else:
            print ("invalid")

    def emnity_ends(self, other):
        if other in self.enemyList:
            self.enemyList[other] = False
        else:
            print("invalid")

# The ship is where the action happens, it can sustain damage and must survive the journey


class Ship:
    def __init__(self):
        self.name = raw_input("Please enter the name of the ship: ")
        self.difficulty = raw_input("Please enter difficulty of 1,2,3 or 4")
        self.systems = systems_list
        self.system_stats = {}
        for system in self.systems:
            self.system_stats[system] = 100

    def system_status(self):
        for item in self.system_stats.keys():
            print (str(self.system_stats[item]) + "% : " + item)


class MainGame:
    def __init__(self):
        self.ship = Ship()
        self.crew = Crew()


systems_list = ["life support", "main engine", "maneuvering engines", "descent", "fuel systems"]
safeguards = ["life support safeguards", "main engine safeguards", "descent safeguards", "fuel systems safeguards"]
limited_crew_list = ["captain", "first officer", "mechanic", "science officer"]
full_crew_list = ["captain", "first officer", "mechanic", "science officer", "technician", "doctor", "soldier"]

role_description = {"captain": "The commander of the ship, the captain has high LEADERSHIP and CHARISMA",
                    "science officer": "Charged with leading the science mission, "
                                       "the chief science officer has high SCIENCE and INTELLIGENCE",
                    "technician": "Knowing all of the technical systems of the ship, "
                                  "the mechanic has high MECHANICAL and INTELLIGENCE",
                    "mechanic": "Being the primary repairperson on board, "
                                "the mechanic has high MECHANICAL and PHYSICAL",
                    "first officer": "The second in commmand, The first officer has high LEADERSHIP and INTELLIGENCE",
                    "doctor": "The chief Medical officer, the doctor has high INTELLIGENCE AND CHARISMA",
                    "soldier": "Along to protect the crew, the Soldier has very high PHYSICAL"
                    }

role_trait_base = {"captain": [2, 2, 2, 2, 4, 4],
                   "science officer": [4, 1, 2, 5, 2, 2],
                   "technician": [4, 2, 4, 2, 2, 2],
                   "mechanic": [2, 5, 4, 2, 2, 1],
                   "first officer": [4, 2, 2, 2, 4, 2],
                   "doctor": [4, 2, 1, 3, 2, 4],
                   "soldier": [2, 7, 2, 1, 2, 1]}

first_names = ['Anneliese', 'Effie', 'Tyra', 'Bell', 'Kirk', 'Jerald', 'Yuonne', 'Leeanne', 'Lyndsey', 'Lura', 'Inger',
               'Celestine', 'Melania', 'Tambra', 'Randy', 'Teena', 'Conchita', 'Gracia', 'Casandra', 'Olevia',
               'Eufemia', 'Rita', 'Shanon', 'Lan', 'Hunter', 'Trinidad', 'Phillip', 'Merrie', 'Melony', 'Page',
               'Teresia', 'Elfreda', 'Madaline', 'Exie', 'Hilton', 'Rodrick', 'Nu', 'Margot', 'Trina', 'Shalon', 'Zona',
               'Marianne', 'Kaitlyn', 'Greta', 'Sergio', 'Del', 'Clinton', 'Caroline', 'Maynard', 'Marti', 'David',
               'Adrian', 'Jim', 'John']
last_names = ['Smith', "Mombassa", "Carson", "Jackson", 'Dean', "Orwell", "Abe", "Cartwright", "Lee", "Ching", "Zhou",
              "O'Leary", "White", "Brown", "Blackstone", "Yens", "Nordquist", "Wooster", "Butler", "Ivanov", "Roman",
              "Yeng", "Dickey", "Zamboni", "Doctor", "Peters", "Patella", "Patel", "Chomsky", "Badiwallah", "Abdul",
              "al Saud", "Hobbes", "Ali"]

crew = Crew(True)

crew.list_crew()
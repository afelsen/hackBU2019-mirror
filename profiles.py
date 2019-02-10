class Attribute:
    def __init__(self, yours, preference, scale):
        self.yours = yours
        self.preference = preference
        self.scale = scale

class Profile:
    def __init__(self, name,
    gender, genderPreference,
    height, heightPreference, heightScale,
    weight, weightPreference, weightScale,
    age, agePreference, ageScale,
    religion, religionPreference, religionScale,
    politics, politicsScale,
    introExtrovert, introExtrovertPreference, introExtrovertScale,
    smoke, smokePreference, smokeScale,
    messyNeat, messyNeatPreference, messyNeatScale,
    dogCat, dogCatScale):

        #Basic self info
        self.name = name

        self.gender = gender
        self.genderPreference = genderPreference


        #Basic items with scales (age,height,weight)
        self.height = Attribute(height,heightPreference,heightScale)
        self.weight = Attribute(weight, weightPreference, weightScale)
        self.age = Attribute(age, agePreference, ageScale)

        #Basic items with preferences
        self.religion = Attribute(religion, religionPreference, religionScale)
        self.politics = Attribute(politics,politics,politicsScale)
        self.introExtrovert = Attribute(introExtrovert,introExtrovertPreference,introExtrovertScale)
        self.smoke = Attribute(smoke, smokePreference, smokeScale)
        self.messyNeat = Attribute(messyNeat, messyNeatPreference, messyNeatScale)

        #Random
        self.dogCat = Attribute(dogCat,dogCat, dogCatScale)

    def __str__(self):
        return str(self.name)

    def find_hated(self,profileList):
        hatred = 0
        for profile in profileList:
            if (profileList[p].gender != self.genderPreference) or not(profileList[p].age.yours in self.age.preference) or (self.gender != profileList[p].genderPreference) or not (self.age.yours in profileList[p].age.preference) :
                continue
            for k in self.__dict__:
                if k == "name" or k == "gender" or k == "genderPreference":
                    continue
                elif k == "height" or k == "weight" or k == "age":
                    val = abs(self.__dict__[k].yours-profileList[p].__dict__[k].yours)**2/100
                    if val <= 5:
                        hatred += val
                    else:
                        hatred += 5
                else:
                    if self.__dict__[k].yours != profileList[p].__dict__[k].yours:
                        hatred += 1

        matchList.append(Oppositeness)

    def find_opposite(self,profileList):

        matchList = []
        for p in range(len(profileList)):

            Oppositeness = 0
            #Break if the person is outside of your age or gender preference (or you're outside of theirs) - For these items, we do not want the opposite
            if (profileList[p].gender != self.genderPreference) or not(profileList[p].age.yours in self.age.preference) or (self.gender != profileList[p].genderPreference) or not (self.age.yours in profileList[p].age.preference) :
                continue

            for k in self.__dict__:
                if k == "name" or k == "gender" or k == "genderPreference":
                    continue
                elif k == "height" or k == "weight" or k == "age":
                    val = abs(self.__dict__[k].yours-profileList[p].__dict__[k].yours)**2/100
                    if val <= 5:
                        Oppositeness += val
                    else:
                        Oppositeness += 5
                else:
                    if self.__dict__[k].yours != profileList[p].__dict__[k].yours:
                        Oppositeness += 1


            matchList.append(Oppositeness)



        maxMatch = 0
        for o in matchList:
            maxMatch = max(o,maxMatch)
            print(o)
        return profileList[p]

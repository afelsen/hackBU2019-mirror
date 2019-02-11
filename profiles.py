class Attribute:
    def __init__(self, yours, preference, scale):
        self.yours = yours
        self.preference = preference
        self.scale = scale
    # def __str__(self):
    #     return str(self.yours)

class Profile:
    def __init__(self, name,
    gender, genderPreference,
    height, heightPreference, heightScale,
    age, agePreference,
    religion, religionScale,
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
        self.age = Attribute(age, agePreference,1)

        #Basic items with preferences
        self.religion = Attribute(religion, religion, religionScale)
        self.politics = Attribute(politics,politics,politicsScale)
        self.introExtrovert = Attribute(introExtrovert,introExtrovertPreference,introExtrovertScale)
        self.smoke = Attribute(smoke, smokePreference, smokeScale)
        self.messyNeat = Attribute(messyNeat, messyNeatPreference, messyNeatScale)

        #Random
        self.dogCat = Attribute(dogCat,dogCat, dogCatScale)

    def __str__(self):
        return str(self.name)

    def getProfileList(self):
        return [self.name,
        self.gender, self.genderPreference,
        self.height.yours, self.height.preference, self.height.scale,
        self.age.yours, self.age.preference,
        self.religion.yours , self.religion.scale,
        self.politics.yours,self.politics.scale,
        self.introExtrovert.yours, self.introExtrovert.preference, self.introExtrovert.scale,
        self.smoke.yours, self.smoke.preference, self.smoke.scale,
        self.messyNeat.yours, self.messyNeat.preference, self.messyNeat.scale,
        self.dogCat.yours, self.dogCat.scale]

    def find_hated(self,profileList):
        matchList = []
        for p in range(len(profileList)):
            hatred = 0
            #checks you are the correct gender/age for the other person and vice versa
            if (profileList[p].gender != self.genderPreference) or not(profileList[p].age.yours in self.age.preference) or (self.gender != profileList[p].genderPreference) or not(self.age.yours in profileList[p].age.preference):
                matchList.append(0)
                continue
            for k in self.__dict__:
                if k == "name" or k == "gender" or k == "genderPreference" or k == "age":
                    continue
                #calculates the amount of difference for hieght, weight, and age
                elif k == "height":
                    #if your H/W is bigger/smaller than thier preference, add the difference squared times 100
                    if self.__dict__[k].yours > profileList[p].__dict__[k].preference[-1]:
                        val = abs(self.__dict__[k].yours - profileList[p].__dict__[k].preference[-1])**2/100
                        if val <= 5:
                            hatred += val
                        else:
                            hatred += 5
                    elif self.__dict__[k].yours < profileList[p].__dict__[k].preference[0]:
                        val = abs(self.__dict__[k].yours - profileList[p].__dict__[k].preference[0])**2/100
                        if val <= 5:
                            hatred += val
                        else:
                            hatred += 5
                    #if their H/W is bigger/smaller than your preference, add the difference squared times 100
                    if profileList[p].__dict__[k].yours > self.__dict__[k].preference[-1]:
                        val = abs(profileList[p].__dict__[k].yours - self.__dict__[k].preference[-1])**2/100
                        if val <= 5:
                            hatred += val
                        else:
                            hatred += 5
                    elif profileList[p].__dict__[k].yours < self.__dict__[k].preference[0]:
                        val = abs(profileList[p].__dict__[k].yours - self.__dict__[k].preference[0])**2/100
                        if val <= 5:
                            hatred += val
                        else:
                            hatred += 5
                #for all other params, add the scale if different
                else:
                    if self.__dict__[k].preference != profileList[p].__dict__[k].yours:
                        hatred += 1 * self.__dict__[k].scale
                    if self.__dict__[k].yours != profileList[p].__dict__[k].preference:
                        hatred += 1 * self.__dict__[k].scale
            matchList.append(hatred)
        maxMatch = 0
        worstPerson = 0
        for i in range(len(profileList)):
            if matchList[i] > maxMatch:
                maxMatch = matchList[i]
                worstPerson = i
            print(profileList[i].name + ":" + str(matchList[i]))
        print(matchList)

        return profileList[worstPerson].getProfileList()

    def find_opposite(self,profileList):
        matchList = []
        for p in range(len(profileList)):
            Oppositeness = 0
            #Break if the person is outside of your age or gender preference (or you're outside of theirs) - For these items, we do not want the opposite
            if (profileList[p].gender != self.genderPreference) or not(profileList[p].age.yours in self.age.preference) or (self.gender != profileList[p].genderPreference) or not (self.age.yours in profileList[p].age.preference) :
                matchList.append(0)
                continue
            for k in self.__dict__:
                if k == "name" or k == "gender" or k == "genderPreference" or k == "age":
                    continue
                #calculates the amount of difference for hieght, weight, and age
                elif k == "height":
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
        worstPerson = 0
        for i in range(len(profileList)):
            if matchList[i] > maxMatch:
                maxMatch = matchList[i]
                worstPerson = i
            print(profileList[i].name + ":" + str(matchList[i]))
        print(matchList)
        return profileList[worstPerson].getProfileList()

    def find_friend_zone(self,profileList):
        matchList = []
        for p in range(len(profileList)):
            awkwardness = 0
            #checks you are the correct gender/age for the other person and vice versa
            if (profileList[p].gender != self.genderPreference) or not(profileList[p].age.yours in self.age.preference) or (self.gender != profileList[p].genderPreference) or not (self.age.yours in profileList[p].age.preference):
                matchList.append(0)
                continue
            for k in self.__dict__:
                if k == "name" or k == "gender" or k == "genderPreference" or k == "age":
                    continue
                #calculates the amount of difference for hieght, weight, and age
                elif k == "height":
                    #if your H/W is bigger/smaller than thier preference, add the difference squared times 100
                    if self.__dict__[k].yours > profileList[p].__dict__[k].preference[-1]:
                        val = abs(self.__dict__[k].yours - profileList[p].__dict__[k].preference[-1])**2/100
                        if val <= 5:
                            awkwardness += val
                        else:
                            awkwardness += 5
                    elif self.__dict__[k].yours < profileList[p].__dict__[k].preference[0]:
                        val = abs(self.__dict__[k].yours - profileList[p].__dict__[k].preference[0])**2/100
                        if val <= 5:
                            awkwardness += val
                        else:
                            awkwardness += 5
                    #if their H/W is bigger/smaller than your preference, add the difference squared times 100
                    if profileList[p].__dict__[k].yours > self.__dict__[k].preference[-1]:
                        val = abs(profileList[p].__dict__[k].yours - self.__dict__[k].preference[-1])**2/100
                        if val <= 5:
                            awkwardness += val
                        else:
                            awkwardness += 5
                    elif profileList[p].__dict__[k].yours < self.__dict__[k].preference[0]:
                        val = abs(profileList[p].__dict__[k].yours - self.__dict__[k].preference[0])**2/100
                        if val <= 5:
                            awkwardness += val
                        else:
                            awkwardness += 5
                #for all other params, add the scale if different for you or same for them
                else:
                    if self.__dict__[k].preference != profileList[p].__dict__[k].yours:
                        awkwardness += 1 * self.__dict__[k].scale
                    if self.__dict__[k].yours == profileList[p].__dict__[k].preference:
                        awkwardness += 1 * self.__dict__[k].scale
            matchList.append(awkwardness)
        maxMatch = 0
        worstPerson = 0
        for i in range(len(profileList)):
            if matchList[i] > maxMatch:
                maxMatch = matchList[i]
                worstPerson = i
            print(profileList[i].name + ":" + str(matchList[i]))
        print(matchList)
        return profileList[worstPerson].getProfileList()

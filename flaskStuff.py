from flask import Flask, render_template, request
from profiles import Profile
import json
import ast

app = Flask(__name__)

@app.route("/index.html")
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/results.html", methods = ['POST'])
@app.route('/results', methods = ['POST'])
def results():


    name = request.form['name']
    Gender = request.form['Gender']
    PGender = request.form['pGender']
    Height = request.form['Height']
    pHeight = request.form['pHeight']
    heightScale = request.form['heightScale']
    Age = request.form['Age']
    pAge = request.form['pAge']
    religion = request.form['Religion']
    religionScale = request.form['religionScale']
    politics = request.form['Politics']
    politicsScale = request.form['politicsScale']
    introExtrovert = request.form['IntroExtro']
    pIntroExtrovert = request.form['PIntroExtro']
    introExtrovertScale = 1#request.form['IntroExtroScale']
    smoke = request.form['Smoker']
    pSmoke = request.form['Psmoker']
    smokeScale = request.form['smokeScale']
    messyNeat = request.form['MessyNeat']
    pMessyNeat = request.form['PMessyNeat']
    messyNeatScale = request.form['messyNeatScale']
    dogCat = request.form['DogCat']
    dogCatScale = request.form['dogCatScale']

    #List of all of the values
    userValues = [name,Gender,PGender,Height,pHeight,heightScale,Age,pAge,religion,religionScale,politics,politicsScale,introExtrovert,pIntroExtrovert,introExtrovertScale,smoke,pSmoke,smokeScale,messyNeat,pMessyNeat, messyNeatScale,dogCat,dogCatScale]

    #Convert values to proper form (turn to integer, list)
    for i in range(len(userValues)):
        #Integers
        if isinstance(userValues[i],int) or userValues[i].isdigit():
            userValues[i] = int(userValues[i])
        #List
        elif len(userValues[i]) > 0 and userValues[i][0] == "[":
            comma = userValues[i].index(",")
            num1 = ""
            num2 = ""
            for j in range(1,comma):
                num1 += userValues[i][j]
            for j in range(comma+1,len(userValues[i])-1):
                num2 += userValues[i][j]
            num1 = int(num1)
            num2 = int(num2)
            userValues[i] = list(range(num1,num2+1))

    #Create profile
    profile0 = Profile(userValues[0],userValues[1],userValues[2],userValues[3],userValues[4],userValues[5],userValues[6],userValues[7],userValues[8],userValues[9],userValues[10],userValues[11],userValues[12],userValues[13],userValues[14],userValues[15],userValues[16],userValues[17],userValues[18],userValues[19], userValues[20],userValues[21],userValues[22])

    #Junk profiles (for testing)
    profile1 = Profile("joe","Male","Female",72,list(range(50,90)),5,20,list(range(18,50)),"Jewish",5,"Democrat",5,"Introvert","Extrovert",5,"No","Yes",5,"Messy","Messy",5,"Cat",5)
    profile2 = Profile("Jane","Female","Male",68,list(range(40,100)),5,19,list(range(18,24)),"Buddhist",5,"Independent",9,"Extrovert","Extrovert",5,"Yes","Yes",5,"Neat","Neat",5,"Dog",5)
    profile3 = Profile("Mary","Female","Male",62,list(range(73,77)),2,18,list(range(18,21)),"Christian",1,"Republican",10,"Extrovert","Extrovert",7,"No","No",5,"Neat","Messy",2,"Dog",4)
    profile4 = Profile("Jackie","Female","Male",65,list(range(67,80)),5,42,list(range(18,30)),"Muslim",5,"Republican",5,"Introvert","Introvert",5,"No","No",5,"Neat","Neat",5,"Cat",5)

    profileList = [profile1,profile2,profile3,profile4]

    newopposite = profile0.find_opposite(profileList)
    newhated = profile0.find_hated(profileList)
    newfriend = profile0.find_friend_zone(profileList)

    #Printing
    # opposite = profile0.find_opposite(profileList)
    # newopposite = []
    # i = 0
    # for k in opposite.__dict__:
    #     if i>2:
    #         for key in opposite.__dict__[k].__dict__:
    #             newopposite.append(opposite.__dict__[k].__dict__[key])
    #     else:
    #         newopposite.append(str(opposite.__dict__[k]))
    #     i+=1
    #
    # hated = profile0.find_hated(profileList)
    # newhated = []
    # i = 0
    # for k in hated.__dict__:
    #     if i>2:
    #         for key in hated.__dict__[k].__dict__:
    #             newhated.append(hated.__dict__[k].__dict__[key])
    #     else:
    #         newhated.append(str(hated.__dict__[k]))
    #     i+=1
    #
    # friend = profile0.find_friend_zone(profileList)
    # newfriend = []
    # i = 0
    # for k in friend.__dict__:
    #     if i>2:
    #         for key in friend.__dict__[k].__dict__:
    #             newfriend.append(friend.__dict__[k].__dict__[key])
    #     else:
    #         newfriend.append(str(friend.__dict__[k]))
    #     i+=1

    return render_template("results.html", answers = (userValues,newopposite,newhated,newfriend))

@app.route('/ProfileCreation.html')
@app.route('/ProfileCreation')
def ProfileCreation():
    return render_template("ProfileCreation.html")

@app.route("/about.html")
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact.html")
@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/ProfileMatch.html")#, methods=['POST'])
@app.route("/ProfileMatch")
def ProfileMatch():
    return render_template("ProfileMatch.html")


if __name__ == "__main__":
    app.run(debug=True)

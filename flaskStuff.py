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
    pAge = request.form['pAge1']
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


    profile0 = Profile(name,Gender,PGender,Height,pHeight,heightScale,Age,pAge,religion,religionScale,politics,politicsScale,introExtrovert,pIntroExtrovert,introExtrovertScale,smoke,pSmoke,smokeScale,messyNeat,pMessyNeat, messyNeatScale,dogCat,dogCatScale)

    profile1 = Profile("joe","M","F",72,list(range(50,90)),5,20,list(range(18,50)),"Jewish",5,"D",5,"I","E",5,"N","Y",5,"M","M",5,"C",5)
    profile2 = Profile("Jane","F","M",68,list(range(40,100)),5,19,list(range(18,24)),"Buddhist",5,"I",9,"E","E",5,"Y","Y",5,"N","N",5,"D",5)
    profile3 = Profile("Mary","F","M",62,list(range(73,77)),2,18,list(range(18,21)),"Christian",1,"R",10,"E","E",7,"N","N",5,"N","M",2,"D",4)
    profile4 = Profile("Jackie","F","M",65,list(range(67,80)),5,42,list(range(18,30)),"Muslim",5,"R",5,"I","I",5,"N","N",5,"N","N",5,"C",5)

    profileList = [profile2,profile1,profile4,profile3]

    opposite = profile0.find_opposite(profileList)
    newopposite = []
    i = 0
    for k in opposite.__dict__:
        if i>2:
            for key in opposite.__dict__[k].__dict__:
                newopposite.append(opposite.__dict__[k].__dict__[key])
        else:
            newopposite.append(str(opposite.__dict__[k]))
        i+=1

    hated = profile0.find_hated(profileList)
    newhated = []
    i = 0
    for k in hated.__dict__:
        if i>2:
            for key in hated.__dict__[k].__dict__:
                newhated.append(hated.__dict__[k].__dict__[key])
        else:
            newhated.append(str(hated.__dict__[k]))
        i+=1

    friend = profile0.find_friend_zone(profileList)
    newfriend = []
    i = 0
    for k in friend.__dict__:
        if i>2:
            for key in friend.__dict__[k].__dict__:
                newfriend.append(friend.__dict__[k].__dict__[key])
        else:
            newfriend.append(str(friend.__dict__[k]))
        i+=1

    return render_template("results.html", answers = ((name,Gender,PGender,Age,pAge,Height,pHeight,heightScale,religion,religionScale,politics,politicsScale,introExtrovert,pIntroExtrovert,introExtrovertScale,smoke,pSmoke,smokeScale,messyNeat,pMessyNeat, messyNeatScale,dogCat,dogCatScale),(newopposite),(newhated),(newfriend)))

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

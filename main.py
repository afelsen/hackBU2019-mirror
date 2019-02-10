from profiles import Profile

def main():
    profile1 = Profile("joe","M","F",72,list(range(50,90)),5,20,list(range(18,50)),5,"Jewish",5,"D",5,"I","E",5,"N","Y",5,"M","M",5,"C",5)
    profile2 = Profile("Jane","F","M",68,list(range(40,100)),5,19,list(range(18,24)),5,"Buddhist",5,"I",9,"E","E",5,"Y","Y",5,"N","N",5,"D",5)
    profile3 = Profile("Mary","F","M",62,list(range(73,77)),2,18,list(range(18,21)),5,"Christian",1,"R",10,"E","E",7,"N","N",5,"N","M",2,"D",4)
    profile4 = Profile("Jackie","F","M",65,list(range(67,80)),5,42,list(range(18,30)),5,"Muslim",5,"R",5,"I","I",5,"N","N",5,"N","N",5,"C",5)

    profileList = [profile2,profile1,profile4,profile3]
    print(profile1.find_opposite(profileList))

    print()

    print(profile1.find_hated(profileList))

    print()

    print(profile1.find_friend_zone(profileList))

main()

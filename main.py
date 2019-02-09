from profiles import Profile

def main():
    profile1 = Profile("joe","M","F",72,list(range(50,90)),5,150,list(range(110,170)),5,20,list(range(18,50)),5,"Jewish","Christian",5,"D",5,"I","E",5,"N","Y",5,"M","M",5,"C",5)
    profile2 = Profile("Jane","F","M",68,list(range(40,100)),5,140,list(range(0,1000)),5,19,list(range(18,24)),5,"Buddhist","Hindu",5,"I",9,"E","E",5,"Y","Y",5,"N","N",5,"D",5)
    profile3 = Profile("Mary","F","M",62,list(range(73,77)),2,130,list(range(100,250)),7,18,list(range(18,21)),5,"Christian","Satanist",1,"R",10,"E","E",7,"N","N",5,"N","M",2,"D",4)
    profile4 = Profile("Jackie","F","M",65,list(range(67,80)),5,180,list(range(120,300)),5,42,list(range(18,30)),5,"Muslim","Muslim",5,"R",5,"I","I",5,"N","N",5,"N","N",5,"C",5)

    profileList = [profile1,profile3,profile4,profile2]
    print(profile1.find_opposite(profileList))

main()

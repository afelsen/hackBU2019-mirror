import pickle

def main():
    #Read the database list, delete robots
    with open('profileInformation.txt', 'rb') as input:
        data = pickle.load(input)
        for profile in data:
            if profile.robot == "Yes":
                data.remove(profile)
    #Write list back to database
    with open('profileInformation.txt', 'wb') as output:
        pickle.dump(data, output, pickle.HIGHEST_PROTOCOL)
main()

import pickle

#This resets the database
def main():
    with open('profileInformation.txt', 'wb') as output:
        list = []
        pickle.dump(list, output, pickle.HIGHEST_PROTOCOL)
main()

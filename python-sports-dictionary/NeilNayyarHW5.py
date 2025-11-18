

def readSportsFile(filePath):
    sports = []
    try:
        # Open the file in read mode.
        myFile = open(filePath, "r")

        #read the first line to get number of sports
        firstLine = myFile.readline().rstrip("\n")
        sportsCount = int(firstLine)
        print("Number of sports:", sportsCount)

        # read the other lines to get sport types
        for nextLine in myFile:
            nextLine = nextLine.rstrip("\n")
            print(nextLine)
            sports.append(nextLine)

        myFile.close()

        return sports

    except IOError:
        print("Error opening file")



def readPlayedFile(sports, filePath="played.txt"):

    # create a dictionary and add the sports

    playedCounts = {}
    for sport in sports:
        playedCounts[sport] = 0

    try:
        # Open the file in read mode.
        myFile = open(filePath, "r")

        # Process each line to count the sport plays.
        for nextLine in myFile:
            nextLine = nextLine.rstrip("\n")
            if nextLine:
                if nextLine in playedCounts:
                    playedCounts[nextLine] += 1

        # Closing the file.
        myFile.close()

    except IOError:
        print("error opening file")

    return playedCounts


def main():
    #use the readsports function to read the file
    sports = readSportsFile("sports.txt")



    # use read function to read the file
    playedCounts = readPlayedFile(sports, "played.txt")

    # Display
    print("\nReport:")
    for sport in sports:
        print(f"{sport}: {playedCounts[sport]}")



main()

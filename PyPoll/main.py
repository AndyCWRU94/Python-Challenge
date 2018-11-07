import os
import csv

csvpath = os.path.join('election_data.csv')

voter = []
county = []
candidate = []

with open(csvpath) as electionfile:
    csvreader = csv.reader(electionfile, delimiter=",")
    skipheader = next(csvreader)

    for row in csvreader:
        voter.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

    print("Election Results")
    print("---------------------------------------------------")

#The total number of votes cast
    totalvotes = len(voter)
    print("The total number of votes cast: " + str(totalvotes))

    print("---------------------------------------------------")
#A complete list of candidates who received votes
    khan = "Khan"
    correy = "Correy"
    li = "Li"
    otool = "O'Tooley"

# The percentage of votes each candidate won
    # Percentage for Khan
    print("")
    khanvote = candidate.count(khan)
    khanperc = round((khanvote / totalvotes) * 100)
    print("Khan: " + str(khanperc) + "% ")

    # Percentage for Correy
    print("")
    correyvote = candidate.count(correy)
    correyperc = round((correyvote / totalvotes) * 100)
    print("Correy: " + str(correyperc) + "% ")

    # Percentage for Li
    print("")
    livote = candidate.count(li)
    liperc = round((livote / totalvotes) * 100)
    print("Li: " + str(liperc) + "% ")

    # Percentage for O'Tooley
    print("")
    otoolvote = candidate.count(otool)
    otoolperc = round((otoolvote / totalvotes) * 100)
    print("O'Tool: " + str(otoolperc) + "% ")


#The total number of votes each candidate won
    print("--------------------------------------------------")
    print("Khan: (" + str(khanvote) + ")")
    print("Correy: (" + str(correyvote) + ")")
    print("Li: (" + str(livote) + ")")
    print("O'Tool: (" + str(otoolvote) + ")")

    # The winner of the election based on popular vote.
    w_list = [khanvote, correyvote, livote, otoolvote]
    winner = max(w_list)
    print("--------------------------------------------------")
    if winner == khanvote:
        print("Winner is: " + khan)
    elif winner == correyvote:
        print("Winner is: " + correy)
    elif winner == livote:
        print("Winner is: " + li)
    else:
        print("Winner is: " + otool)


    distination = os.path.join('pypoll.txt')
    with open(distination, "w") as file:
        file.writelines("Election Results" + "\n")
        file.writelines("------------------" + "\n")
        file.writelines("Total Votes: " + str(totalvotes) + "\n")
        file.writelines("------------------" + "\n")
        file.writelines("Khan: " + str(khanperc) + "%" + "  " + "(" + str(khanvote) + ")" + "\n")
        file.writelines("Correy: " + str(correyperc) + "  " + "(" + str(correyvote) + ")" + "\n")
        file.writelines("Li: " + str(liperc) + "%" + "  " + "(" + str(livote) + ")" + "\n")
        file.writelines("O'Tooley: " + str(otoolperc) + "%" + "  " + "(" + str(otoolvote) + ")" + "\n")
        file.writelines("" + "\n")
        file.writelines("------------------" + "\n")
        if winner == khanvote:
            file.writelines("Winner is: " + khan + "\n")
        elif winner == correyvote:
            file.writelines("Winner is: " + correy + "\n")
        elif winner == livote:
            file.writelines("Winner is: " + li + "\n")
        else:
            file.writelines("Winner is: " + otool + "\n")
def main():

    trying_2()


def create_count():
    text_file = open("WorldSeriesWinners.txt", "r")

    TeamWins = {}

    for line in text_file:
        spaces = line.split("\n")
        for word in spaces:
            if word in TeamWins:
                TeamWins[word] += 1
            else:
                TeamWins[word] = 1
    print(TeamWins)
    for TextWord in TeamWins.keys():
        print(TextWord.rstrip(" "), ":", TeamWins[TextWord])

    text_file.close()


def trying_2():
    same_file = open("WorldSeriesWinners.txt", "r")
    team_year = {}
    first_year = 1903
    team_year[first_year] = "no"
    for line in same_file:
        if first_year < 2009:
            team_year[first_year] = line.strip()
            if first_year == 1903 or first_year == 1993:
                first_year += 2
            else:
                first_year += 1

    print(team_year)


main()
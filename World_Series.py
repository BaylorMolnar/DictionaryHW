def main():

    year = input("Enter a year between 1903 and 2008(excluding 1904 and 1994): ")

    team = years_and_teams(year)
    amount = create_count(team)

    print(
        "In",
        year,
        "the winner of the World Series was",
        team,
        "who have won the World Series",
        amount,
        "times.",
    )


def create_count(team_name):
    text_file = open("WorldSeriesWinners.txt", "r")

    TeamWins = {}

    for line in text_file:
        spaces = line.split("\n")
        for word in spaces:
            if word in TeamWins:
                TeamWins[word] += 1
            else:
                TeamWins[word] = 1

    # for TextWord in TeamWins.keys():
    # print(TextWord.rstrip(" "), ":", TeamWins[TextWord])

    value = TeamWins.get(team_name)

    return value
    text_file.close()


def years_and_teams(year_):
    same_file = open("WorldSeriesWinners.txt", "r")
    team_year = {}
    first_year = 1903
    for line in same_file:
        if first_year < 2009:
            team_year[str(first_year)] = line.strip()
            if first_year == 1903 or first_year == 1993:
                first_year += 2
            else:
                first_year += 1

    value = team_year.get(str(year_))

    return value

    same_file.close()


main()
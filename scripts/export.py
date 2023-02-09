import requests

requests.packages.urllib3.disable_warnings()

leagueId = "1399468022"
seasonId = "2022"
periodId = "19"

url = "https://fantasy.espn.com/apis/v3/games/ffl/seasons/{}/segments/0/leagues/{}".format(seasonId, leagueId)

teams = []
rosters = []
matchups = []

def get_teams():
    global teams
    data = requests.get(url, params = {"view": "mTeam"}, verify=False).json()
    for index in range(len(data["teams"])):
        team = []
        team.append(str(data)[str(data).find("firstName", str(data).find(data["teams"][index]["owners"][0]) - 100) + 13 : str(data).find("id", str(data).find(data["teams"][index]["owners"][0]) - 100) - 4][:1].upper() + str(data)[str(data).find("firstName", str(data).find(data["teams"][index]["owners"][0]) - 100) + 13 : str(data).find("id", str(data).find(data["teams"][index]["owners"][0]) - 100) - 4][1:] + " " + str(data)[str(data).find("lastName", str(data).find(data["teams"][index]["owners"][0]) - 100) + 12 : str(data).find("notificationSettings", str(data).find(data["teams"][index]["owners"][0]) - 100) - 4][:1].upper() + str(data)[str(data).find("lastName", str(data).find(data["teams"][index]["owners"][0]) - 100) + 12 : str(data).find("notificationSettings", str(data).find(data["teams"][index]["owners"][0]) - 100) - 4][1:])
        team.append(data["teams"][index]["name"].replace("  ", " ").strip())
        team.append(str(data["teams"][index]["divisionId"]).replace("0", "East").replace("1", "West"))
        team.append(str(data["teams"][index]["record"]["overall"]["wins"]) + "-" + str(data["teams"][index]["record"]["overall"]["losses"]))
        team.append(data["teams"][index]["waiverRank"])
        team.append(data["teams"][index]["transactionCounter"]["acquisitions"])
        team.append(data["teams"][index]["transactionCounter"]["trades"])
        team.insert(0, data["teams"][index]["id"])
        teams.append(team)
    '''TESTING'''
    for team in teams:
        print()
        print(team)
        print()

def get_rosters():
    global rosters
    data = requests.get(url, params = {"view": "mRoster"}, verify=False).json()
    for index in range(len(data["teams"])):
        roster = [None] * 18
        for num in range(len(data["teams"][index]["roster"]["entries"])):
            player = []
            player.append(data["teams"][index]["roster"]["entries"][num]["lineupSlotId"])
            player.append(data["teams"][index]["roster"]["entries"][num]["playerPoolEntry"]["player"]["fullName"])
            player.append(round(data["teams"][index]["roster"]["entries"][num]["playerPoolEntry"]["player"]["stats"][3]["appliedTotal"], 1))
            player.append(round(data["teams"][index]["roster"]["entries"][num]["playerPoolEntry"]["player"]["stats"][3]["appliedAverage"], 1))
            player.append(data["teams"][index]["roster"]["entries"][num]["playerPoolEntry"]["ratings"]["0"]["positionalRanking"])
            if player[0] == "":
                print("ERROR: No lineup slot received.")
            elif player[0] == 0:
                if roster[0] == None:
                    roster[0] = player
                else:
                    roster[1] = player
            elif player[0] == 2:
                if roster[2] == None:
                    roster[2] = player
                else:
                    roster[3] = player
            elif player[0] == 4:
                if roster[4] == None:
                    roster[4] = player
                else:
                    roster[5] = player
            elif player[0] == 6:
                roster[6] = player
            elif player[0] == 23:
                roster[7] = player
            elif player[0] == 16:
                roster[8] = player
            elif player[0] == 17:
                roster[9] = player
            elif player[0] == 20:
                if roster == None:
                    pass
                elif roster[10] == None:
                    roster[10] = player
                elif roster[11] == None:
                    roster[11] = player
                elif roster[12] == None:
                    roster[12] = player
                elif roster[13] == None:
                    roster[13] = player
                elif roster[14] == None:
                    roster[14] = player
                elif roster[15] == None:
                    roster[15] = player
                elif roster[16] == None:
                    roster[16] = player
                else:
                    pass
            elif player[0] == 21:
                roster[17] = player
            else:
                print("Received lineup slot: {}".format(player[0]))
        for num in range(len(roster)):
            if roster[num] == None:
                roster[num] = ["-", "None", "-", "-", "-"]
            else:
                pass
        for num in range(len(roster)):
            roster[num].pop(0)
        roster.insert(0, data["teams"][index]["id"])
        rosters.append(roster)
    '''TESTING'''
    for roster in rosters:
        print()
        print(roster)
        print()

def get_matchups():
    global matchups
    data = requests.get(url, params = {"view": "mBoxscore", "scoringPeriodId": "{}".format(periodId.replace("18", "17").replace("19", "17"))}, verify=False).json()
    for index in range(int(periodId.replace("15", "14").replace("16", "15").replace("17", "15").replace("18", "15").replace("19", "15")) * 4 - 4, int(periodId.replace("15", "14").replace("16", "15").replace("17", "15").replace("18", "15").replace("19", "15")) * 4):
        matchup = [None] * 18
        for num in range(len(data["schedule"][index]["away"]["rosterForCurrentScoringPeriod"]["entries"])):
            player = []
            player.append(data["schedule"][index]["away"]["rosterForCurrentScoringPeriod"]["entries"][num]["lineupSlotId"])
            player.append(data["schedule"][index]["away"]["rosterForCurrentScoringPeriod"]["entries"][num]["playerPoolEntry"]["player"]["fullName"])
            player.append(round(data["schedule"][index]["away"]["rosterForCurrentScoringPeriod"]["entries"][num]["playerPoolEntry"]["appliedStatTotal"], 1))
            if player[0] == "":
                    print("ERROR: No lineup slot received.")
            elif player[0] == 0:
                if matchup[0] == None:
                    matchup[0] = player
                else:
                    matchup[1] = player
            elif player[0] == 2:
                if matchup[2] == None:
                    matchup[2] = player
                else:
                    matchup[3] = player
            elif player[0] == 4:
                if matchup[4] == None:
                    matchup[4] = player
                else:
                    matchup[5] = player
            elif player[0] == 6:
                matchup[6] = player
            elif player[0] == 23:
                matchup[7] = player
            elif player[0] == 16:
                matchup[8] = player
            elif player[0] == 17:
                matchup[9] = player
            elif player[0] == 20:
                if matchup == None:
                    pass
                elif matchup[10] == None:
                    matchup[10] = player
                elif matchup[11] == None:
                    matchup[11] = player
                elif matchup[12] == None:
                    matchup[12] = player
                elif matchup[13] == None:
                    matchup[13] = player
                elif matchup[14] == None:
                    matchup[14] = player
                elif matchup[15] == None:
                    matchup[15] = player
                elif matchup[16] == None:
                    matchup[16] = player
                else:
                    pass
            elif player[0] == 21:
                matchup[17] = player
            else:
                print("Received lineup slot: {}".format(player[0]))
        for num in range(len(matchup)):
            if matchup[num] == None:
                matchup[num] = ["-", "None", 0.0]
            else:
                pass
        for num in range(len(matchup)):
            matchup.append(matchup[num][1:3])
        matchup = matchup[18:]
        matchup.insert(0, data["schedule"][index]["away"]["teamId"])
        matchups.append(matchup)
    for index in range(int(periodId.replace("15", "14").replace("16", "15").replace("17", "15").replace("18", "15").replace("19", "15")) * 4 - 4, int(periodId.replace("15", "14").replace("16", "15").replace("17", "15").replace("18", "15").replace("19", "15")) * 4):
        matchup = [None] * 18
        for num in range(len(data["schedule"][index]["home"]["rosterForCurrentScoringPeriod"]["entries"])):
            player = []
            player.append(data["schedule"][index]["home"]["rosterForCurrentScoringPeriod"]["entries"][num]["lineupSlotId"])
            player.append(data["schedule"][index]["home"]["rosterForCurrentScoringPeriod"]["entries"][num]["playerPoolEntry"]["player"]["fullName"])
            player.append(round(data["schedule"][index]["home"]["rosterForCurrentScoringPeriod"]["entries"][num]["playerPoolEntry"]["appliedStatTotal"], 1))
            if player[0] == "":
                    print("ERROR: No lineup slot received.")
            elif player[0] == 0:
                if matchup[0] == None:
                    matchup[0] = player
                else:
                    matchup[1] = player
            elif player[0] == 2:
                if matchup[2] == None:
                    matchup[2] = player
                else:
                    matchup[3] = player
            elif player[0] == 4:
                if matchup[4] == None:
                    matchup[4] = player
                else:
                    matchup[5] = player
            elif player[0] == 6:
                matchup[6] = player
            elif player[0] == 23:
                matchup[7] = player
            elif player[0] == 16:
                matchup[8] = player
            elif player[0] == 17:
                matchup[9] = player
            elif player[0] == 20:
                if matchup == None:
                    pass
                elif matchup[10] == None:
                    matchup[10] = player
                elif matchup[11] == None:
                    matchup[11] = player
                elif matchup[12] == None:
                    matchup[12] = player
                elif matchup[13] == None:
                    matchup[13] = player
                elif matchup[14] == None:
                    matchup[14] = player
                elif matchup[15] == None:
                    matchup[15] = player
                elif matchup[16] == None:
                    matchup[16] = player
                else:
                    pass
            elif player[0] == 21:
                matchup[17] = player
            else:
                print("Received lineup slot: {}".format(player[0]))
        for num in range(len(matchup)):
            if matchup[num] == None:
                matchup[num] = ["-", "None", 0.0]
            else:
                pass
        for num in range(len(matchup)):
            matchup.append(matchup[num][1:3])
        matchup = matchup[18:]
        matchup.insert(0, data["schedule"][index]["home"]["teamId"])
        matchups.append(matchup)
    matchups = [matchups[0]] + [matchups[4]] + [matchups[1]] + [matchups[5]] + [matchups[2]] + [matchups[6]] + [matchups[3]] + [matchups[7]]
    '''TESTING'''
    for matchup in matchups:
        print()
        print(matchup)
        print()

def get_scoreboards():
    pass

def get_standings():
    pass

def get_projections():
    pass

def get_schedules():
    pass

def get_brackets():
    pass

def get_activity():
    pass

#get_teams()
#get_rosters()
#get_matchups()
#get_scoreboards()
#get_standings()
#get_projections()
#get_schedules()
#get_brackets()
#get_activity()
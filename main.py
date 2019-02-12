from GET_Data import GET_RESULTS, GET_TABLE, GET_CROSS_TABLE, CREATE_CSV, GET_ALL
from GET_Calc import GET_ALL_GOALS, GET_ATT_DEF_VALUE, GET_ATT_DEF_ANALYSE, GET_ESTIMATE_GOALS_POISSON , GET_POINTS, GET_SEASON, GET_STATS_FROM_CLUB, CALC_SEASON_POISSON, GET_ALL_CLUBS



url = "https://www.dfb.de/bundesliga/spieltagtabelle/?spieledb_path=/competitions/12/seasons/17683/matchday&spieledb_path=%2Fcompetitions%2F12%2Fseasons%2F17820%2Fmatchday%2F13"
#url = "https://www.dfb.de/2-bundesliga/spieltagtabelle/?no_cache=1&spieledb_path=%2Fcompetitions%2F3%2Fseasons%2Fcurrent%2Fmatchday%2F3"
#url = "https://www.dfb.de/3-liga/spieltagtabelle/?no_cache=1&spieledb_path=%2Fcompetitions%2F4%2Fseasons%2Fcurrent%2Fmatchday%2F3"


#GET_ALL(url)

#print(GET_TABLE(url))

#print(GET_RESULTS(url))

#print(GET_CROSS_TABLE(url))
#print(GET_CROSS_TABLE(doc)[6][6])

#CREATE_CSV(url)




file = "./Python_Projects/Football/CSV/1_Bundesliga_2018_2019.csv"


#print(GET_ALL_CLUBS(file))

#print(GET_ALL_GOALS(file))

#print(GET_STATS_FROM_CLUB("Eintracht Frankfurt", file, 1))

# [Games_Sum, [Games_Home, [Goals, Goals_AVG, Trend], [Hits, Hits_AVG, Trend]], 
#             [Games_Out,  [Goals, Goals_AVG, Trend], [Hits, Hits_AVG, Trend]]]


#print(GET_ATT_DEF_VALUE("Borussia Dortmund", file))

# [ATT_Home, DEF_Home, ATT_Out, DEF_Out]

#print(GET_ATT_DEF_ANALYSE("Borussia Dortmund", file))

#print(GET_ESTIMATE_GOALS_POISSON("Eintracht Frankfurt", "Bayern München", file))

#print(GET_POINTS("Bayern München", file))

#print(GET_SEASON("Eintracht Frankfurt", file))

print(CALC_SEASON_POISSON("Eintracht Frankfurt", file))

# [[Day, Location, Opponent, [Estimate_Goals, [Poisson], 
#                             Estimate_Hits,  [Poisson]], 
#                           [[Real_Result],   [Difference], [Trend(Club_Goals, Club_Hits)]]]  


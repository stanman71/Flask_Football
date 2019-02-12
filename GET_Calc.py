# Error: ImportError: Missing required dependencies ['dateutil']
# >>> Try pd.test()
# >>> pip install python-dateutil pytz --force-reinstall --upgrade


import pandas as pd
import numpy as np
from scipy.stats import poisson


def GET_ALL_CLUBS(file):

    df = pd.read_csv(file, delimiter=",")   
    df = df.Team_1.unique()  
    df.sort()

    return(df)



def GET_ALL_GOALS(file):

    df = pd.read_csv(file, delimiter=",")
    df = df.loc[df['Status'] == "PASS"]

    return_list = []

    Sum = int(df.shape[0] / 9)

    # home goals
    df_1         = df["Tore_Team_1"]
    Heim         = int(df_1.sum())
    Heim_AVG     = df_1.mean()
    Heim_AVG     = round(Heim_AVG, 2)

    # away goals
    df_2         = df["Tore_Team_2"]
    Aus          = int(df_2.sum())
    Aus_AVG      = df_2.mean()
    Aus_AVG      = round(Aus_AVG, 2)

    Complete     = Heim + Aus
    Complete_AVG = Heim_AVG + Aus_AVG

    return_list.append(Sum)
    return_list.append(Complete)
    return_list.append(Complete_AVG) 
    return_list.append(Heim)
    return_list.append(Heim_AVG)
    return_list.append(Aus)
    return_list.append(Aus_AVG)

    return(return_list)



def GET_STATS_FROM_CLUB(Club, file, day = 34):  
    
    df = pd.read_csv(file, delimiter=",")
    df = df.loc[df['Status'] == "PASS"]
    df = df.loc[df['Spieltag'] <= day]

    return_list = [] 
    list_Heim = []  
    list_Aus = []   

    # table home
    df_heim_0 = df.loc[df['Team_1'] == Club]
    Sum_Heim = df_heim_0.shape[0]

    # table away
    df_aus_0 = df.loc[df['Team_2'] == Club]  
    Sum_Aus = df_aus_0.shape[0]

    Sum = Sum_Heim + Sum_Aus

    # home goals (home)
    df_heim_1      = df_heim_0["Tore_Team_1"]
    Heim_Goals     = int(df_heim_1.sum())
    Heim_Goals_AVG = df_heim_1.mean()
    Heim_Goals_AVG = round(Heim_Goals_AVG, 2)

    list_Heim_Goals = []

    try:
        # progression home goals (home)
        Last_5 = df_heim_1[-5:]
        Last_5 = sum(Last_5) / float(len(Last_5))
        Last_5 = round(Last_5, 2)

        Trend_Heim_Goals = Last_5 - Heim_Goals_AVG
        Trend_Heim_Goals  = round(Trend_Heim_Goals, 2)

        list_Heim_Goals.append(Heim_Goals) 
        list_Heim_Goals.append(Heim_Goals_AVG)
        list_Heim_Goals.append(Trend_Heim_Goals)
    except:
        pass

    # away goals (home)
    df_heim_2      = df_heim_0["Tore_Team_2"]
    Heim_Hits      = int(df_heim_2.sum())
    Heim_Hits_AVG  = df_heim_2.mean()
    Heim_Hits_AVG  = round(Heim_Hits_AVG, 2)

    list_Heim_Hits = []

    try:
        # progression away goals (home)
        Last_5 = df_heim_2[-5:]
        Last_5 = sum(Last_5) / float(len(Last_5))
        Last_5 = round(Last_5, 2)

        Trend_Heim_Hits = Last_5 - Heim_Hits_AVG
        Trend_Heim_Hits  = round(Trend_Heim_Hits, 2)

        list_Heim_Hits.append(Heim_Hits)
        list_Heim_Hits.append(Heim_Hits_AVG)
        list_Heim_Hits.append(Trend_Heim_Hits)
    except:
        pass

    list_Heim.append(Sum_Heim)
    list_Heim.append(list_Heim_Goals)
    list_Heim.append(list_Heim_Hits)

    # progression away goals (home)
    df_aus_1       = df_aus_0["Tore_Team_2"]
    Aus_Goals      = int(df_aus_1.sum())
    Aus_Goals_AVG  = df_aus_1.mean()
    Aus_Goals_AVG  = round(Aus_Goals_AVG, 2)

    try:
        # progression away goals (home)
        Last_5 = df_aus_1[-5:]
        Last_5 = sum(Last_5) / float(len(Last_5))
        Last_5 = round(Last_5, 2)

        Trend_Aus_Goals = Last_5 - Aus_Goals_AVG
        Trend_Aus_Goals  = round(Trend_Aus_Goals, 2)

        list_Aus_Goals = []
        list_Aus_Goals.append(Aus_Goals) 
        list_Aus_Goals.append(Aus_Goals_AVG)
        list_Aus_Goals.append(Trend_Aus_Goals)
    except:
        pass

    # away goals (away)
    df_aus_2       = df_aus_0["Tore_Team_1"]
    Aus_Hits       = int(df_aus_2.sum())
    Aus_Hits_AVG   = df_aus_2.mean()
    Aus_Hits_AVG   = round(Aus_Hits_AVG, 2)

    try:
        # progression away goals (away)
        Last_5 = df_aus_2[-5:]
        Last_5 = sum(Last_5) / float(len(Last_5))
        Last_5 = round(Last_5, 2)

        Trend_Aus_Hits = Last_5 - Aus_Hits_AVG
        Trend_Aus_Hits  = round(Trend_Aus_Hits, 2)

        list_Aus_Hits = []
        list_Aus_Hits.append(Aus_Hits) 
        list_Aus_Hits.append(Aus_Hits_AVG)
        list_Aus_Hits.append(Trend_Aus_Hits)

        list_Aus.append(Sum_Aus)
        list_Aus.append(list_Aus_Goals)
        list_Aus.append(list_Aus_Hits)
    except:
        pass

    return_list.append(Sum)
    return_list.append(list_Heim)
    return_list.append(list_Aus) 


    return(return_list)   



def GET_ATT_DEF_VALUE(Club, file):

    # https://www.onlinemathe.de/forum/Fussballergebnisse-Berechnen-Formel

    return_list = []

    # home

    # Verhältnis von den (durchschnittlichen) Heimtoren/Heimtreffern des Vereins zu den 
    # (durchschnittlichen) Heimtoren aller Vereine

    ATT_Heim = (GET_STATS_FROM_CLUB(Club, file)[1][1][1])/(GET_ALL_GOALS(file)[4])
    ATT_Heim = round(ATT_Heim, 2)
    DEF_Heim = (GET_STATS_FROM_CLUB(Club, file)[1][2][1])/(GET_ALL_GOALS(file)[6])
    DEF_Heim = round(DEF_Heim, 2)

    # away
 
    # Verhältnis von den (durchschnittlichen) Auswärtztoren/Auswärtztreffern des Vereins zu den 
    # (durchschnittlichen) Auswärtztoren aller Vereine

    ATT_Aus  = (GET_STATS_FROM_CLUB(Club, file)[2][1][1])/(GET_ALL_GOALS(file)[6])
    ATT_Aus  = round(ATT_Aus, 2)
    DEF_Aus  = (GET_STATS_FROM_CLUB(Club, file)[2][2][1])/(GET_ALL_GOALS(file)[4])
    DEF_Aus  = round(DEF_Aus, 2)

    return_list.append(ATT_Heim)
    return_list.append(DEF_Heim)
    return_list.append(ATT_Aus)
    return_list.append(DEF_Aus)

    return(return_list)



def GET_ATT_DEF_ANALYSE(Club, file):

    from sklearn.metrics import r2_score

    X = []
    Y = []
    X_Pred = []
    Y_Pred = []
    day = []

    data = CALC_SEASON_POISSON(Club, file)

    for i in range(0,34):

        try:
            X.append(data[i][4][0][0])
            Y.append(data[i][4][0][1])
        except:
            break

        X_Pred.append(data[i][3][0])
        Y_Pred.append(data[i][3][2])

        day.append(data[i][0])

    r2_X = r2_score(X, X_Pred)
    r2_Y = r2_score(Y, Y_Pred)

    return(X, X_Pred, Y, Y_Pred, day, r2_X, r2_Y)



def GET_ESTIMATE_GOALS_POISSON(Club_1, Club_2, file):

    # https://www.onlinemathe.de/forum/Fussballergebnisse-Berechnen-Formel
    # https://www.wettstern.com/sportwetten-mathematik/poisson-saisonwetten
    # https://www.wettstern.com/sportwetten-mathematik/poisson-wetten#angriffsstaerke

    return_list = []

    Goals_Club_1 = GET_ATT_DEF_VALUE(Club_1, file)[0] * GET_ALL_GOALS(file)[4] * GET_ATT_DEF_VALUE(Club_2, file)[3]
    Goals_Club_1 = round(Goals_Club_1, 2)
    Goals_Club_2 = GET_ATT_DEF_VALUE(Club_1, file)[1] * GET_ALL_GOALS(file)[6] * GET_ATT_DEF_VALUE(Club_2, file)[2]
    Goals_Club_2 = round(Goals_Club_2, 2)

    goals = []
    goals.append(Goals_Club_1)
    goals.append(Goals_Club_2)   

    # calculate poisson
    # http://muthu.co/poisson-distribution-with-python/


    for i in range (0, len(goals)):
 
        array = []
        element = goals[i]

        rv = poisson(element)  # Average
        for num in range(0,5):
            array.append(round(rv.pmf(num) * 100, 2))

        club = []
        club.append(element)    # Goals
        club.append(array)      # Poisson

        return_list.append(club)

    return(return_list)



def GET_POINTS(Club, file):

    df = pd.read_csv(file, delimiter=",")
    df = df.loc[df['Status'] == "PASS"]

    return_list = []    
 
    df = df[(df.Team_1 == Club) | (df.Team_2 == Club)]

    # prevent error massage
    
    df = df.copy()

    # cases
 
    conditions = [
        (df['Team_1'] == Club) & ((df['Tore_Team_1']) >  (df['Tore_Team_2'])), 
        (df['Team_1'] == Club) & ((df['Tore_Team_1']) == (df['Tore_Team_2'])),
        (df['Team_1'] == Club) & ((df['Tore_Team_1']) <  (df['Tore_Team_2'])),
        (df['Team_2'] == Club) & ((df['Tore_Team_1']) >  (df['Tore_Team_2'])),
        (df['Team_2'] == Club) & ((df['Tore_Team_1']) == (df['Tore_Team_2'])),
        (df['Team_2'] == Club) & ((df['Tore_Team_1']) <  (df['Tore_Team_2']))]

    choices = [3, 1, 0, 0, 1, 3]
    df['Points'] = np.select(conditions, choices)
    
    Sum        = df['Points'].sum()
    Complete   = df['Points'].values.tolist()   # convert to list
    AVG_Points = df['Points'].mean()
    AVG_Points = round(AVG_Points, 2)

    # progression
    
    Last_5 = Complete[-5:]
    Last_5 = sum(Last_5) / float(len(Last_5))
    Last_5 = round(Last_5, 2)

    Trend = Last_5 - AVG_Points
    Trend = round(Trend, 2)

    return_list.append(Sum)
    return_list.append(AVG_Points)
    return_list.append(Trend)        
    return_list.append(Complete)

    return(return_list)



def GET_SEASON(Club, file):

    df = pd.read_csv(file, delimiter=",")
    
    return_list = []
  
    df = df[(df.Team_1 == Club) | (df.Team_2 == Club)]

    # get clubnames
    Club_1  = df['Team_1'].values.tolist()
    Club_2  = df['Team_2'].values.tolist()

    # only with results
    df_goals = df[(df.Status == "PASS")]

    # get goals
    Goals_1 = df_goals['Tore_Team_1'].values.tolist()
    Goals_2 = df_goals['Tore_Team_2'].values.tolist()

    # create array
    for i in range (0, len(Club_1)):

        club_names = []
        club_names.append(Club_1[i])
        club_names.append(Club_2[i])

        try:
            goals = []
            goals.append(int(Goals_1[i]))
            goals.append(int(Goals_2[i]))
        except:
            pass

        day = []
        day.append(i+1)
        day.append(club_names)
        day.append(goals)

        return_list.append(day)

    return(return_list)



def CALC_SEASON_POISSON(Club, file):

    return_list = []

    season = GET_SEASON(Club, file)

    ########################
    # block estimate results
    ########################

    for i in range (0, len(season)):
        result = GET_ESTIMATE_GOALS_POISSON(season[i][1][0], season[i][1][1], file)

        day = []

        day.append(season[i][0])

        if season[i][1][0] == Club:
            day.append("H")
            day.append(season[i][1][1])   # Gegner

            estimate = []
            estimate.append(result[0][0])         # Tore Club
            estimate.append(result[0][1])         # Poisson Tore Club        
            estimate.append(result[1][0])         # Hits Club       
            estimate.append(result[1][1])         # Poisson Hits Club
            day.append(estimate)
        
        else:
            day.append("A")
            day.append(season[i][1][0])   # Gegner

            estimate = []
            estimate.append(result[1][0])         # Tore Club
            estimate.append(result[1][1])         # Poisson Tore Club        
            estimate.append(result[0][0])         # Hits Club       
            estimate.append(result[0][1])         # Poisson Hits Club
            day.append(estimate)

        ####################
        # block real results
        ####################

        real_result = []

        # real result

        if day[1] == "H":
            try:
                real_result_goals = []
                real_result_goals.append(season[i][2][0])    
                real_result_goals.append(season[i][2][1])
                real_result.append(real_result_goals)
            except:
                real_result_goals = []
                real_result.append(real_result_goals)

        else:
            try:
                real_result_goals = []
                real_result_goals.append(season[i][2][1])    
                real_result_goals.append(season[i][2][0])
                real_result.append(real_result_goals)            
            except:
                real_result_goals = []
                real_result.append(real_result_goals)

        # add difference

        if day[1] == "H":
            try:        
                diff = []
                diff.append(round((season[i][2][0]) - (result[0][0]), 2))     
                diff.append(round((season[i][2][1]) - (result[1][0]), 2))     
                real_result.append(diff)
            except:
                diff = []
                real_result.append(diff)       

        if day[1] == "A":
            try:        
                diff = []
                diff.append(round((season[i][2][1]) - (result[1][0]), 2))     
                diff.append(round((season[i][2][0]) - (result[0][0]), 2))     
                real_result.append(diff)
            except:
                diff = []
                real_result.append(diff)      
              
        # add trend

        trend = GET_STATS_FROM_CLUB(Club, file, i + 1)

        if day[1] == "H" and day[0] == (trend[0]):
            
                trend_list = []
                trend_list.append(trend[1][1][2])
                trend_list.append(trend[1][2][2])
                real_result.append(trend_list)

        elif day[1] == "A" and day[0] == trend[0]:
       
            trend_list = []
            trend_list.append(trend[2][1][2])
            trend_list.append(trend[2][2][2])
            real_result.append(trend_list)

        else:
            trend_list = []
            real_result.append(trend_list)        


        day.append(real_result)

        return_list.append(day)

    return(return_list)

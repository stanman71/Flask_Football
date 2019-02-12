import requests
from bs4 import BeautifulSoup
import sys, csv , operator, time


########################
# GET_BASICINFO
########################

def GET_BASICINFO(url, doc):
 
    info = []

    # league

    if "bundesliga" in url:
        liga = "1_Bundesliga"

        if "2-bundesliga" in url:
            liga = "2_Bundesliga"

    if "3-liga" in url:
        liga = "3_Bundesliga"

    info.append(liga)


    # day

    for option in doc.find_all('option', selected=True):
        info.append(option.text)    

    info[2] = info[2].split(" ")[1]

    if int(info[2]) < 10:
        info[2] = "0" + info[2]

    return(info)




########################
# GET_RESULTS
########################

def GET_RESULTS(url):

    r = requests.get(url)
    doc = BeautifulSoup(r.text, "html.parser")

    data_results = GET_BASICINFO(url, doc)

    # results  

    content = doc.select_one(".table-match-comparison")

    for data in content.findAll('a', href=True):
        data = data.text.splitlines()

        if data != [' Vergleich'] and data != [' Schema']:       
            data_results.extend(data)

    return(data_results)




########################
# GET_Table
########################

def GET_TABLE(url):

    r = requests.get(url)
    doc = BeautifulSoup(r.text, "html.parser")

    table = GET_BASICINFO(url, doc)

    content = doc.find("div", {"id": "tabular"})

    rows = content.find_all('tr')

    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]

        table.append([ele for ele in cols if ele])

    return(table)




########################
# GET_Cross_Table
########################

def GET_CROSS_TABLE(url):

    r = requests.get(url)
    doc = BeautifulSoup(r.text, "html.parser")

    cross_table = GET_BASICINFO(url, doc)

    content = doc.select_one(".cross-tab")

    # get clubs

    club_list = []

    for club in content.findAll('img'):
        club = club.get('title')

        if club not in club_list:  
            club_list.append(club)


    # get cross_table

    rows = content.find_all('tr')

    for i, row in enumerate(rows):
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]

        cross_table.append([ele for ele in cols if ele])
    
        if i < len(rows)-1:
            cross_table.append(club_list[i])
        
    return(cross_table)



########################
# Create CSV
########################

def CREATE_CSV(url):

    data = GET_RESULTS(url)

    season = data[1].replace("/", "_")

    file = "./Python_Projects/Football/CSV/" + data[0] + "_" + season + ".csv"


    # check CSV content

    exist_entry = False

    try:
        with open(file, mode='r', encoding='utf-8') as f:
            spamreader = csv.reader(f)      

            for row in spamreader:
                if row is not None:
                    exist_entry = True              

    except:
        pass
    

    # write content

    with open(file, mode='a', encoding="utf-8", newline='') as result_file:
        result_writer = csv.writer(result_file, delimiter=',')

        # add header
        if exist_entry == False:
            result_writer.writerow(["Spieltag", "Status", "Team_1", "Team_2", "Tore_Team_1", "Tore_Team_2"])

        for i in range (3, len(data), 3):
            goals = data[i+1].split(" : ")

            if goals[0] is not "-":
                Status = "PASS"
                result_writer.writerow([data[2], Status, data[i], data[i+2], goals[0], goals[1]])                    
                # data[2]   > Spieltag
                # Status    > ausgetragen ?
                # data[i]   > Team_1
                # data[i+2] > Team_2 
                # goals[0]  > Tore_Team_1
                # goals[1]  > Tore_Team_2

            else:
                Status = "OPEN"
                result_writer.writerow([data[2], Status, data[i], data[i+2], "", ""])   


        print("CSV updated")



########################
# DELETE_CSV
########################

def DELETE_CSV(url):

    data = GET_RESULTS(url)

    season = data[1].replace("/", "_")
    file = "./CSV/" + data[0] + "_" + season + ".csv"    
    
    f = open(file, "w+") # delete CSV content
    f.close()    



########################
# GET_ALL
########################

def GET_ALL(url): 
    
    if url[-2:-1] is not "F":
        url = url[:-2] 
    elif url[-1:] is not "F":
        url = url[:-1]

    DELETE_CSV(url)

    i = 1
    while i < 35:
        url_temp = url + str(i)
        CREATE_CSV(url_temp)
        time.sleep(5)
        i = i + 1

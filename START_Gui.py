from GET_Calc import GET_ALL_GOALS, GET_POINTS, GET_SEASON, CALC_SEASON_POISSON, GET_ALL_CLUBS, GET_ATT_DEF_ANALYSE
from BUILD_Graph import build_graph

from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap 


file = "./CSV/1_Bundesliga_2018_2019.csv"


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1
Bootstrap(app)


# landing Page
@app.route('/', methods=['GET'])
def index():

    dropdown_list = GET_ALL_CLUBS(file)

    name = request.args.get("name")
    age  = request.args.get("age")

    # input formular with checkbox
    if request.args.get('checkbox') == "on":  

        return render_template('index.html',
                                site1="Index", 
                                name=name, 
                                age=age,
                                check=True,
                                dropdown_list=dropdown_list
                                )

    return render_template('index.html',
                        site1="Index",                                       
                        name=name, 
                        age=age,
                        dropdown_list=dropdown_list                   
                        )


# club information
@app.route('/club', methods=['GET', 'POST']) 
def club():

    club_name = request.args.get("club")    
    dropdown_list = GET_ALL_CLUBS(file)

    # input dropdown (add value to the url)
    if request.method == "GET":     

        if club_name != None:       
 
            return render_template('club.html',
                                    site1="Index", 
                                    club_name=club_name,
                                    dropdown_list=dropdown_list,
                                    )
   
    # input buttons
    if request.method == "POST": 

        # match plan
        if 'Button_1' in request.form:

            season = GET_SEASON(club_name, file) 

            return render_template('club.html',
                                    site1="Index", 
                                    club_name=club_name,
                                    dropdown_list=dropdown_list,
                                    season=season
                                    )

        # points
        if 'Button_2' in request.form:

            y  = GET_POINTS(club_name, file)[3]            
            x  = list(range(1, (len(y)+1) ))        

            values = (x, y)

            graph_table = build_graph(values, "plot")  

            return render_template('club.html',
                                    site1="Index",                            
                                    club_name=club_name,
                                    dropdown_list=dropdown_list,
                                    graph_table=graph_table
                                    )


        # analyse ATT / DEF
        if 'Button_3' in request.form:

            anaylse = GET_ATT_DEF_ANALYSE(club_name, file)

            y1_1 = GET_ATT_DEF_ANALYSE(club_name, file)[0]
            y1_2 = GET_ATT_DEF_ANALYSE(club_name, file)[1]
            x1   = GET_ATT_DEF_ANALYSE(club_name, file)[4]

            y2_1 = GET_ATT_DEF_ANALYSE(club_name, file)[2]
            y2_2 = GET_ATT_DEF_ANALYSE(club_name, file)[3]
            x2   = GET_ATT_DEF_ANALYSE(club_name, file)[4]

            values_1 = (x1, y1_1, y1_2)
            values_2 = (x2, y2_1, y2_2)           

            graph_goals = build_graph(values_1, "plot")
            graph_hits = build_graph(values_2, "plot")

            return render_template('club.html',
                                    site1="Index",                              
                                    club_name=club_name,
                                    dropdown_list=dropdown_list,
                                    att_value=round(anaylse[5],3),
                                    def_value=round(anaylse[6],3),
                                    graph_goals=graph_goals,
                                    graph_hits=graph_hits                             
                                    )


        # win / lost
        if 'Button_4' in request.form:

            anaylse = GET_ATT_DEF_ANALYSE(club_name, file)

            y1_1 = GET_ATT_DEF_ANALYSE(club_name, file)[1] 
            y1_2 = GET_ATT_DEF_ANALYSE(club_name, file)[3]  
            x1   = GET_ATT_DEF_ANALYSE(club_name, file)[4]

            y2_1 = GET_ATT_DEF_ANALYSE(club_name, file)[0] 
            y2_2 = GET_ATT_DEF_ANALYSE(club_name, file)[2] 
            x2   = GET_ATT_DEF_ANALYSE(club_name, file)[4]

            values_1 = (x1, y1_1, y1_2)
            values_2 = (x2, y2_1, y2_2)           

            graph_real = build_graph(values_1, "plot")
            graph_pred = build_graph(values_2, "plot")

            return render_template('club.html',
                                    site1="Index",                              
                                    club_name=club_name,
                                    dropdown_list=dropdown_list,
                                    graph_real=graph_real,
                                    graph_pred=graph_pred                             
                                    )


        # poisson
        if 'Button_5' in request.form:
            poisson = CALC_SEASON_POISSON(club_name, file) 

            return render_template('club.html',
                                    site1="Index",                              
                                    club_name=club_name,
                                    dropdown_list=dropdown_list,
                                    poisson=poisson
                                    )


# update diagram
@app.after_request
def add_header(response):
    # response.cache_control.no_store = True
    if 'Cache-Control' not in response.headers:
        response.headers['Cache-Control'] = 'no-store'
    return response


if __name__ == '__main__':
    app.debug = True
    app.run()



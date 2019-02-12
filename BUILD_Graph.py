# for image update
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import io
import base64

def build_graph(values, type):

    x_coordinates = values[0]
    y_coordinates = values[1]
    
    try:
        y2_coordinates = values[2]
    except:
        y2_coordinates = None


    img = io.BytesIO()
    
    if type == "plot":    
        plt.plot(x_coordinates, y_coordinates)

        if y2_coordinates is not None:
            plt.plot(x_coordinates, y2_coordinates)

    if type == "scatter":    
        plt.scatter(x_coordinates, y_coordinates)

        if y2_coordinates is not None:
            plt.scatter(x_coordinates, y2_coordinates)
            plt.fill_between(y_coordinates, y2_coordinates, color='grey', alpha='0.5')  

    plt.savefig(img, format='png')
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    
    return 'data:image/png;base64,{}'.format(graph_url)


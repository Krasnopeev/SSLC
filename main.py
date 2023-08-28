import os

from flask import Flask, request, render_template

from backend import get_data

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["APPLICATION_ROOT"] = "/"


# get_data 
# {date} string in format '2023-07-15'
# {interval} integer value. Time for which lightning discharges accumulate (in minutes)   


@app.route('/', methods=["GET", "POST"])
async def main():
    if request.method == "POST":
        # Get shops data from OpenStreetMap
        data = get_data(request.form["date"], request.form["count"])
        
        start = request.form["start"]
        start = request.form["end"]

        step = request.form["end"]
        

        markers = ''
        
        for i in data:
            # Create the marker
            #markers += "var marker = L.marker([{latitude}, {longitude}]).addTo(map);".format(latitude=i['lat'], longitude=i['lon'])
            markers += "var marker = L.circle([{latitude}, {longitude}], {{color: 'red', fillColor: '#ff1', fillOpacity: 0.5, colorOpacity: 0.5, radius: 5000}}).addTo(map);".format(latitude=i['lat'], longitude=i['lon'])
        
        #print(markers)
        # Render the page with the map
        return render_template('results.html', markers=markers, date=request.form["date"])
    
    else:
        # Render the input form
        return render_template('input.html')

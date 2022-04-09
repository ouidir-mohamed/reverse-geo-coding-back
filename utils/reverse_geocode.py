
import  requests
from utils.nearest_city import getCommuneWilayaLine
# local server
def reverseGeoCode(lat:str,lng:str):
    response =requests.get('http://localhost:4000/v1/reverse?point.lat={}&point.lon={}&size=1&layers=street,venue,address'.format(lat,lng))
    feature=response.json()["features"][0]["properties"]
    try:
        output=feature["name"]+", "+getCommuneWilayaLine(lat,lng)
        print(output)
        
    except:
        output=feature["label"]+getCommuneWilayaLine(lat,lng)
    return(output)

# mapbox 
# def reverseGeoCode(lat:str,lng:str):
#     response =requests.get('https://api.mapbox.com/geocoding/v5/mapbox.places/{},{}.json?access_token=pk.eyJ1IjoibW9vb29vZSIsImEiOiJja3J0cXM1dW4ybjVjMnZubzQzYnN0a2M1In0.gE4hsOBmMiDXsIkXwtyqmQ'.format(lng,lat))
#     return(response.json()["features"][0]["place_name"])
    
    
    
    

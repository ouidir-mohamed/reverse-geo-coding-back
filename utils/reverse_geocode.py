
import  requests
from utils.nearest_city import getCommuneWilayaLine



def reverseGeoCode(lat:str,lng:str):
    response =requests.get('http://localhost:4000/v1/reverse?point.lat={}&point.lon={}&size=1&layers=street,venue,address'.format(lat,lng))
    feature=response.json()["features"][0]["properties"]
    try:
        output=feature["name"]+", "+getCommuneWilayaLine(lat,lng)
        
    except:
        output=feature["label"]+getCommuneWilayaLine(lat,lng)
    return(output)

    
    
    

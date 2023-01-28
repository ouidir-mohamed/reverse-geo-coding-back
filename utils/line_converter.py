import re

from utils.reverse_geocode import reverseGeoCode
def convertLatLngLine(line:str):
    try:
        expression="^(.+?) - \(Lat:(.+?), Lng:(.+?)\)"
        x=re.search(expression,line)
        horraire= x.group(1)
        lat= x.group(2)
        lng=x.group(3)
    
    # print(horraire,lat,lng)
        code =reverseGeoCode(lat,lng)
        return horraire+' - '+code
    except:
        return line



def convertLatLngLineFake(line:str):
    try:
        expression="^(.+?) - \(Lat:(.+?), Lng:(.+?)\)"
        x=re.search(expression,line)
        horraire= x.group(1)
        lat= x.group(2)
        lng=x.group(3)
    
    # print(horraire,lat,lng)
        # code =reverseGeoCode(lat,lng)
        return horraire+' - '+"Fake Place Name"
    except:
        return line



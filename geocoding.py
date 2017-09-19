
import requests  
import urllib
def geocode(address, city, state, zip_code):
    try:
        location_param = ("%s+%s+%s+%s" % ("Pedernera", "Posadas", "Misiones", "2037"))
        #url_request = "http://nominatim.openstreetmap.org/search?q=" + location_param + "&format=json&polygon_geojson=1"
        #url_request = "maps.googleapis.com/maps/api/geocode/json?address=%s&sensor=false" % location_param
        url_request = "http://graphhopper.com/api/1/geocode?q=" + location_param + "&key=482bc777-d6d9-49fa-97f0-785a086467e4"        
        result = requests.get(url_request)
        data = result.json()
        #location = data['results'][0]['geometry']['location']
        #location = json.dumps(data["hits"][0]["point"])
        lat = location = json.dumps(data["hits"][0]["point"]["lat"])
        lng = location = json.dumps(data["hits"][0]["point"]['lng'])
        return lat, lng
    except Exception:
        return None
        
geocode("Pedernera", "Posadas", "Misiones", "202037")


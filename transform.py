import json
data = json.load(open('USCities.json'))
new_data={}
for i in data:
    if i["state"] == "FL":
        #i["zip_code"] = str(i["zip_code"])
        #i["latitude"] = str(i["latitude"])
        #i["longitude"] = str(i["longitude"])
        new_data[str(i['zip_code']).zfill(5)] = i
json.dump(json.dumps(new_data),open('SelectUSCitiesZipData.json','w'))

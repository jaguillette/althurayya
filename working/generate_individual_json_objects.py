import json, codecs

# 1. read CSV data
# 2. open JSON > write one big JSON, save individual records
# 3. save all data....

tsvFile = "/Users/romanov/Documents/GitProjects/maximromanov.github.io/projects/althurayya/working/0_CornuData_Initial/Cornu_All_Final_Reformatted.txt"

places = "/Users/romanov/Documents/GitProjects/maximromanov.github.io/projects/althurayya/places/"
routes = "/Users/romanov/Documents/GitProjects/maximromanov.github.io/projects/althurayya/routes/"
master = "/Users/romanov/Documents/GitProjects/maximromanov.github.io/projects/althurayya/master/"

#################################
def placeholder():
    with open("output/enhanced_dataset.json", 'r',encoding='utf-8') as fp:
        db = json.load(fp)
    geojson = {"type":"FeatureCollection","features":[]}
    for k,v in db.items():
        if 'geo' in v:
            feature = {"type":"Feature","geometry":{"type":"Point","coordinates":[v['geo']['x_coord'],v['geo']['y_coord']]}}
            feature['properties'] = v
            geojson['features'].append(feature)
    with open("output/enhanced_dataset.geojson","w",encoding='utf-8') as fp:
        json.dump(geojson,fp,sort_keys=True)
#################################

def generateJSONdata(tsvFile):
    geojson = {"type":"FeatureCollection","features":[]}
    
    with open(tsvFile, "r", encoding="utf8") as f1:
        data = f1.read().split("\n")

        n = data[0].split("\t")
        #print(n)

        for l in data[1:]:
            l = l.split("\t")

            uri = l[7]

            d = {}
            for i in range(0,len(l)):
                d[n[i]] = l[i]

            #input(d)

            # writing a feature
            feature = {"type":"Feature","geometry":{"type":"Point","coordinates":[float(l[1]),float(l[2])]}}
            feature['properties'] = d
            geojson['features'].append(feature)
            
            geojsonSingle = {"type":"FeatureCollection","features":[]}
            geojsonSingle['features'].append(feature)

            with open(places+"%s.geojson" % uri,"w",encoding='utf-8') as fp:
                json.dump(geojsonSingle,fp,sort_keys=True)

    with open(master+"places.geojson","w",encoding='utf-8') as fp:
        json.dump(geojson,fp,sort_keys=True)

        


generateJSONdata(tsvFile)
print("Tada!")

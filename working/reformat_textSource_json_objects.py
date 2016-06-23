import json, codecs

# 1. read CSV data
# 2. open JSON > write one big JSON, save individual records
# 3. save all data....

jsonFile = "/Users/romanov/Documents/GitProjects/maximromanov.github.io/projects/althurayya/working/0_TextSources/index_a.json"

test = "/Users/romanov/Documents/GitProjects/maximromanov.github.io/projects/althurayya/master/places.geojson"

places = "/Users/romanov/Documents/GitProjects/maximromanov.github.io/projects/althurayya/places/"
routes = "/Users/romanov/Documents/GitProjects/maximromanov.github.io/projects/althurayya/routes/"
master = "/Users/romanov/Documents/GitProjects/maximromanov.github.io/projects/althurayya/master/"


def readJson(jsonFile):
    with open(jsonFile, 'r', encoding='utf-8') as fp:
        db = json.loads(fp.read())
        for i in db['features']:
            for k,v in i.items():
                print(k)
                input(v)
            
            input()



readJson(jsonFile)


def generateJSONdata(tsvFile):
    geojson = {"type":"FeatureCollection","features":[]}
    
    with open(tsvFile, "r", encoding="utf8") as f1:
        data = f1.read().split("\n")

        n = data[0].split("\t")
        n = ["regNum"]+n
        n = ['region_code', 'region_spelled',
             'coord_lon', 'coord_lat',
             'top_type_hom', 'top_type_orig',
             'toponym_translit', 'toponym_arabic',
             'cornu_URI',
             'toponym_translit_other', 'toponym_arabic_other',
             'toponym_search',
             'toponym_buckwalter']
        print(n)
        #input()

        for l in data[1:]:
            l = l.split("\t")
            input(l)
            try:
                l = [prov[l[0]]] + l
            except:
                print(prov[l[0]])
                l = ["lacking"] + l

            uri = l[8]

            # cornu data dic
            d = {}
            for i in range(0,len(l)):
                d[n[i]] = l[i]

            # adding other fields
            d["coord_certainty"] = "certain"
            refs = ["muCjamBuldan", "kitabAnsab"]

            #input(d)

            # writing a feature
            #feature = {"type":"Feature","geometry":{"type":"Point","coordinates":[float(l[2]),float(l[3])]}}
            feature = {"type":"Feature","geometry":{"type":"Point","coordinates":[float(l[2]),float(l[3])]}, "properties": {"cornuData": d, "textual_sources_uris": refs}}
            #feature['properties'] = d
            geojson['features'].append(feature)
            
            geojsonSingle = {"type":"FeatureCollection","features":[]}
            geojsonSingle['features'].append(feature)

            with open(places+"%s.geojson" % uri,"w",encoding='utf-8') as fp:
                json.dump(geojsonSingle,fp,sort_keys=True, indent=4,ensure_ascii=False)

    with open(master+"places.geojson","w",encoding='utf-8') as fp:
        json.dump(geojson,fp,sort_keys=True, indent=4, ensure_ascii=False)



        


#generateJSONdata(tsvFile)

print("Tada!")

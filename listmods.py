import json
import os

addons_path = "./"
directory_contents = os.listdir(addons_path)
mods = []


for dir in directory_contents: 
    if os.path.isdir(dir):
        files = os.listdir(addons_path+dir)
        for file in files: 
            file_path= addons_path+dir+"/"+file
            if file.__contains__("ServerData.json") and os.stat(file_path).st_size != 0:
                #print(dir, file_path,os.path.getsize(file_path))
                #utf-8 with BOM encoding
                with open(file_path, 'r+', encoding="utf_8_sig") as f:
                    data = json.loads(f.read())
                    mod ={
                        "modId": data['id'],
                        "name": data['name'],
                        "version": data["revision"]['version']
                    }
                    mods.append(mod)


if len(mods)>1:
    with open('mods.json', 'w') as f:
        json.dump(mods, f)
        print("The json file is created")


#example: Input
# {
#     "id": "5614E4816F653D1A",
#     "name": "Sample Mod - Workbench Plugin",
#     "revision": {
#         "version": "1.0.1",
#         "dependencies": [],
#         "scenarios": [],
#         "downloaded": true
#     }
# }

#example: Output
# {
#     "modId": "596B3717B10FFB07",
#     "name": "MapAndDrive",
#     "version": "1.0.1"
# }
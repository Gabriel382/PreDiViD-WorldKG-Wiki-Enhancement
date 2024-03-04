
import time

def save_in_file(lista):
    with open("nplanet_osm.ttl", '+a') as fd:
        fd.write(''.join(lista))

def checklist(label, lista):
    return label in lista

our_list = ["wkgs:Village",
            "wkgs:County",
            "wkgs:City",
            "wkgs:State",
            "wkgs:Country",
            "wkgs:Island",
            "wkgs:Continent",
            "wkgs:Region",
            "wkgs:Municipality"]

start = time.time()
count = 0
last_object = []
prefix = False
next_object = False
entities = 0
with open("planet_osm.ttl") as file:
    for line in file:
        last_object += [line]
        count = count + 1
        if line == "\n":
            if prefix:
                if checklist(last_object[0].split(" ")[-2],our_list):
                    save_in_file(last_object)
                    entities += 1
                last_object = []
            # Prefixes
            else:
                prefix = True
                save_in_file(last_object)
                last_object = []
end =  time.time()
print("Execution time in seconds: ",(end-start))
print("No of lines printed: ",count)

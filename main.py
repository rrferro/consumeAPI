import requests
import json
import os

response = requests.get("https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow")
#print(type(response))

#creating a new empty dict
global new_dict
new_dict = {"questions": []}

global count
count = 0

for data in response.json()['items']:
    #print(data["tags"])
    res = next((sub for sub in data["tags"] if sub == "python"), None)   
    #print(res) 
    if (res == "python"):
        count = count + 1       
        new_dict["questions"].append({'Title': data['title'], 'Link': data['link'], 'View Count': data['view_count'] , 'answered': data['is_answered']})
        #print(f"{data['title']}, {data['link']}, {data['is_answered']}, {data['view_count']}")
        #print(f"res variable is: {res}")
        #print(type(data)) # this is a dict
        #print(type(data["tags"])) # this is a list   
#print(new_dict)
#print(count)
      
        # Serializing json
json_object = json.dumps(new_dict, indent=4)
 
# Writing to questions.json
with open(r"%s\questions.json" % os.path.dirname(__file__), "w") as outfile:
    outfile.write(json_object)

#Printing the current working directory
#print(os.getcwd())


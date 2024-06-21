import requests
import json

response = requests.get("https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow")
#print(type(response))

#creating a new empty dict
new_dict = {}

for data in response.json()['items']:
    res = next((sub for sub in data["tags"] if sub == "python"), None)
    if (res == "python"):       
        new_dict.update({"Title": data['title'], "Link": data['link'], "View Count": data['view_count'] , "answered": data['is_answered']})
       # print(f"{data['title']}, {data['link']}, {data['is_answered']}, {data['view_count']}")
        #print(data["link"]) working just for link
        #print(type(res))
        #print(f"res variable is: {res}")
        #print(type(data)) # this is a dict
        #print(type(data["tags"])) # this is a list
        
        
print(type(new_dict))
print(new_dict)
        
        #add elements to a dictionary
        

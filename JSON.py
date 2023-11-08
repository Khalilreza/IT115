import json


delta = {

    'name': 'Khalil Reza',
    'age': 23,
    'city': 'Seattle, WA',
    'interests': ['Footbal','Hiking','Exploring'],
    'is_student': True

}

with open('data.json', 'w') as json_file:
    json.dump(delta, json_file, indent=4)

print('data has been written to data.json')
#Im making a change to my file to prove that I saved something.

#create funtion to read the data form the JSON file
with open('data.json', "r") as json_file:#r stands for reading. Rreading from the Json file
    loaded_data =  json.load(json_file)#create object to load the data from the json file

#confirmation fucntion that files have been loaded
print('Data loaded form data.json:')
print(loaded_data)


#Call loaded data in the key value pair to edit
loaded_data['age'] = 27
#append into the interest array with the correct key
loaded_data['interests'].append('im secretly a filipino ninja')



#use with statement to moidify the code in the json file
with open('data.json', 'w') as json_file:
    json.dump(loaded_data, json_file, indent=4)

#Print confirmation
print('Modified data to data.json file')
print('Modified data to data.json file')


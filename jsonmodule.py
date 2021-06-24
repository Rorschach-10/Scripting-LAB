import json

employee_data = '''
{
"people" : [{
"name" : "Kanitin",
"email" : ["K.singngam@hotmail.com"],
"married" : false
},
{
"name" : "Fifa",
"email" : ["K.f@hotmail.com"],
"married" : true
}]
}
'''

print(employee_data)
print()

data = json.loads(employee_data)
print(data)
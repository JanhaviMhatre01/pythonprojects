'''
/**********************************************************************************
* Purpose: Create a JSON file having Inventory Details for Rice, Pulses and Wheats
* with properties name, weight, price per kg.
*
* @author : Janhavi Mhatre
* @python version 3.7
* @platform : PyCharm
* @since 5-1-2019
*
***********************************************************************************/
'''
import json
inventory = {}
inventory['rice'] = """{ 
                    "name" : "basmati",
                    "price" : 100,
                    "weight" : 20
                 }
                 {
                    "name" : "kolam",
                    "price" : 70,
                    "weight" : 22

                 }
          """
inventory['rice'] = {
                    "name" : "kolam",
                    "price" : 70,
                    "weight" : 22

                 }

inventory['pulses'] = {
                    "name" : "dry beans",
                    "price" : 140,
                    "weight" : 200

                 }
inventory['pulses'] = {
                    "name" : "dry peas",
                    "price" : 103,
                    "weight" : 25

                 }

inventory['wheat'] = {
                    "name" : "emmer",
                    "price" : 200,
                    "weight" : 250

                 }
inventory['wheat'] = {
                        "name": "spelt",
                        "price" : 100,
                        "weight" : 150
                 }

# inventory = """
# {
#     "rice": [
#                 {
#                     "name" : "basmati",
#                     "price" : 100,
#                     "weight" : 20
#
#                 },
#                 {
#                     "name" : "kolam",
#                     "price" : 70,
#                     "weight" : 22
#
#                 }
#             ],
#     "pulses": [
#                 {
#                     "name" : "dry beans",
#                     "price" : 140,
#                     "weight" : 200
#                 },
#                 {
#                     "name" : "dry peas",
#                     "price" : 103,
#                     "weight" : 25
#                 }
#                ],
#     "wheat":  [
#                 {
#                     "name" : "emmer",
#                     "price" : 200,
#                     "weight" : 250
#                 },
#
#                 {
#                     "name" : "spelt",
#                     "price" : 100,
#                     "weight" : 150
#                 }
#                 ]
# }
#
# """


data = json.dumps(inventory)


with open("/home/admin1/bridgelabz_pythonproj/samplejson.txt","+w") as f:
    f.write(data)

with open("/home/admin1/bridgelabz_pythonproj/samplejson.txt","r") as f:
    s = f.read()
    read_data = json.loads(s)
print(read_data)
print(inventory['rice']['name'])

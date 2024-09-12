import json
import os

DATA_File = "data/person.json"

def read_data():
	if not os.path.exists(DATA_File):
		return[]
		with open(DATA_File,'r') as file:
			return json.load(file)
def write_data(data):
	with open(DATA_File,'w') as file:
		json.dump(data,file,indent=2)
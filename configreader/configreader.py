import json

# read file
# with open('config.json', 'r') as myfile:
#     data=myfile.read()
#
# # parse file
# obj = json.loads(data)
#
# # show values
# print("QT-Main-Title: " + str(obj['title']))
# print("QT-Amount-Sub-Screen: " + str(obj['amount_sub_screen']))
# print("Config-Param1: " + str(obj['param1']))
# print("Config-Param2: " + str(obj['param2']))
#
# for par in obj['param2']:
# 	# check if string is unicode, then decode
# 	if isinstance(par, unicode):
# 		# decode unicode string to utf-8
# 		print( par.decode() )
# 	else:
# 		print( par )


class ConfigReader():

	def read_config(self, filename: str):
		file = open(filename, "r")
		print(type(file)) # get type of file
		print(file.read())

	def get_part_from_config(self, filename: str, part: str) -> dict:
		file = open(filename, "r")
		data=file.read()
		obj = json.loads(data)
		print("read config part: " + part)
		print(obj[part])
		return obj[part]

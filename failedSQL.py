# Failed code

# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="yourusername",
#   password="yourpassword"
# )

# print(mydb)

def distanceCalculator(uid1, uid2):
	distance = 0
	if uid2 in uid1.connections:
		distance = 1
		return distance
	else:
		for x in uid1.connections:
			if x = uid2:
				distance = 2
				return distance
			else: 
				for y in x.connections:
					if y = uid2:
						distance = 3
						return distance

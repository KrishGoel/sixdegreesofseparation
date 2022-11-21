import json
import pandas as pd
from math import inf

with open('./data/users.json', 'r') as f: # Opening the file in 'r' (reading) mode
	users = json.load(f)

connections = [[0 for i in users] for i in users]
for i in range(len(users)):
	for j in range(len(users)):
		if j in users[i]["connections"]:
			connections[i][j] = 1
# Connections is the adjacency matrix with all weights = 1 (may be updated later to indicate the strength of the bond)

def find_all_distances(connections, start, end=-1):
    n = len(connections)

    dist = [inf]*n
    dist[start] = connections[start][start]  # 0

    spVertex = [False]*n
    parent = [-1]*n

    path = [{}]*n

    for count in range(n-1):
        minix = inf
        u = 0

        for v in range(len(spVertex)):
            if spVertex[v] == False and dist[v] <= minix:
                minix = dist[v]
                u = v

        spVertex[u] = True
        for v in range(n):
            if not(spVertex[v]) and connections[u][v] != 0 and dist[u] + connections[u][v] < dist[v]:
                parent[v] = u
                dist[v] = dist[u] + connections[u][v]

    for i in range(n):
        j = i
        s = []
        while parent[j] != -1:
            s.append(j)
            j = parent[j]
        s.append(start)
        path[i] = s[::-1]

    return (dist[end], path[end]) if end >= 0 else (dist, path)


def find_shortest_path(connections, start, end=-1):
    return find_all_distances(connections, start, end)[1]


def find_shortest_distance(connections, start, end=-1):
    return find_all_distances(connections, start, end)[0]

# Runner
print("""
Welcome to 6ix Degrees Of Separation
""")
while True:
    print("""
    ------ MENU ------
    1. Enlist all the users in the database
    2. Get the distance and path between 2 people
    3. Exit
    """)

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print(pd.DataFrame(users))
    elif choice == 2:
        source = int(input("Enter the UID of the 1st user: "))
        destination = int(input("Enter the UID of the 2nd user: "))

        if find_shortest_path(connections, source, destination) == inf:
            print("No social connection exists")
        else:
            print("The shortest path between", users[source]["name"], "and", users[destination]["name"], "is", find_shortest_distance(connections, source, destination), "social units")
            print("""
            The path is """, end="")
            for i in find_shortest_path(connections, source, destination):
                if i == find_shortest_path(connections, source, destination)[-1]:
                    print(users[i]["name"])
                else:
                    print(users[i]["name"], end = " -> ")

    elif choice == 3:
        break
    else:
        print("Enter a valid input from the menu")
    
    else: 
        print("Invalid input")
import json
with open('./data/users.json', 'r') as f: # Opening the file in 'r' (reading) mode
	users = json.load(f)

connections = [[0 for i in users] for i in users]
for i in range(len(users)):
	for j in range(len(users)):
		if j in users[i]["connections"]:
			connections[i][j] = 1

for i in connections:
	print(i)
# Connections is the adjacency matrix with all weights = 1 (may be updated later to indicate the strength of the bond)

from math import inf

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

print(find_shortest_path(connections, 0, 9))
print(find_shortest_distance(connections, 0, 9))
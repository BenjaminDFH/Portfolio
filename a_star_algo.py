# *** PSEUDO CODE ***
# OPEN // the set of nodes to be evaluated (unvisited nodes)
# CLOSED // the set of nodes already evaluated (visited nodes)
# add the start node to OPEN (the only value in the list)
#
# LOOP
#   CURRENT = node in OPEN  with the lowest f_cost
#   remove CURRENT from OPEN
#   add CURRENT to closed
#
#   if current is the target node // path has been found
#       return
#
#   for each NEIGHBOUR of the CURRENT node
#       if NEIGHBOUR is not traversable or NEIGHBOUR is in CLOSED
#           skip to the next NEIGHBOUR
#
#       if new path to NEIGHBOUR is shorter OR NEIGHBOUR is not in OPEN
#           set f_cost fo NEIGHBOUR
#           set parent of NEIGHBOUR to CURRENT
#           if NEIGHBOUR is not in OPEN
#               add NEIGHBOUR to OPEN

def f(g, h, n):
    return g[n] + h[n]

def a_star_algo(cost, heuristic, start, target):
    path_set = []
    open_list = [start]
    closed_list = []
    path_len = {start: 0}
    parent_node = {start: start}
    while open_list:
        node = min(open_list, key=lambda x: f(path_len, heuristic, x))
        if node in target:
            fv_n = f(path_len, heuristic, node)
            reconstruct = []
            aux = node
            while parent_node[aux] != aux:
                reconstruct.append(aux)
                aux = parent_node[aux]
            reconstruct.append(aux)
            reconstruct.reverse()
            path_set.append((reconstruct, fv_n))
            open_list.remove(node)
            continue
        path_cost = cost[node]
        for index, weight in enumerate(path_cost):
            if weight > 0:
                if index not in open_list and index not in closed_list:
                    open_list.append(index)
                    parent_node[index] = node
                    path_len[index] = path_len[node] + weight
                else:
                    if path_len[index] > path_len[node] + weight:
                        path_len[index] = path_len[node] + weight
                        parent_node[index] = node
                        if index in closed_list:
                            closed_list.remove(index)
                            open_list.append(index)
        open_list.remove(node)
        closed_list.append(node)
    if path_set:
        path_set = sorted(path_set, key=lambda x: x[1])
        path = path_set[0][0]
    else:
        path = []
    return path

give_cost = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 5, 9, -1, 6, -1, -1, -1, -1, -1],
             [0, -1, 0, 3, -1, -1, 9, -1, -1, -1, -1],
             [0, -1, 2, 0, 1, -1, -1, -1, -1, -1, -1],
             [0, 6, -1, -1, 0, -1, -1, 5, 7, -1, -1],
             [0, -1, -1, -1, 2, 0, -1, -1, -1, 2, -1],
             [0, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1],
             [0, -1, -1, -1, -1, -1, -1, 0, -1, -1, -1],
             [0, -1, -1, -1, -1, 2, -1, -1, 0, -1, 8],
             [0, -1, -1, -1, -1, -1, -1, -1, -1, 0, 7],
             [0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0]]

start = 1
give_goals = [6, 7, 10]
heuristic = [0, 5, 7, 3, 4, 6, 0, 0, 6, 5, 0]

getPath = a_star_algo(give_cost, heuristic, start, give_goals)

print(getPath)

file = open("24-1.in", "r")
# file = open("24-1.in.sample", "r")


def sum_bridge(bridge):
    val = 0
    for i in range(len(bridge)):
        val += bridge[i][0]
        val += bridge[i][1]
    return val


def find_max(start, bridges, visited_nodes, bridge_values, cache):
    # print("{}".format(visited_nodes))
    new_visited_nodes = visited_nodes.copy()
    continuing = False
    for next_node in bridges[start]:
        if (start, next_node) not in new_visited_nodes and (next_node, start) not in new_visited_nodes:
            new_visited_nodes.append((start, next_node))
            # if tuple(new_visited_nodes) not in cache:
            #    cache.add(tuple(new_visited_nodes))
            find_max(next_node, bridges, new_visited_nodes, bridge_values, cache)
            new_visited_nodes.remove((start, next_node))
            continuing = True

    if not continuing:
        bridge_val = sum_bridge(visited_nodes)
        # print("{} || Sum: {}".format(visited_nodes, bridge_val))
        if len(visited_nodes) in bridge_values:
            bridge_values[len(visited_nodes)].append(bridge_val)
        else:
            bridge_values[len(visited_nodes)] = [bridge_val]

bridges = {}
cache = set()
for line in file:
    start, end = [int(x) for x in line.strip().split('/')]

    if start in bridges:
        bridges[start].append(end)
    else:
        bridges[start] = [end]

    if end in bridges:
        bridges[end].append(start)
    else:
        bridges[end] = [start]

# print(bridges)
visited_nodes = []
bridge_values = {}
find_max(0, bridges, visited_nodes, bridge_values, cache)
print(max(bridge_values[max(bridge_values.keys())]))

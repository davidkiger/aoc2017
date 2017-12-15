import pprint


file = open("7-1.in", "r")


def get_weight(node):
    weight = node_hash[node]['weight']
    child_weights = []
    child_weights_set = set()
    for child in node_hash[node]['children']:
        w = get_weight(child)
        child_weights.append(w)
        child_weights_set.add(w)

    if len(child_weights_set) > 1:
        print("====")
        print(node)
        print(child_weights_set)
        print("----")
        for child in node_hash[node]['children']:
            print("{} : {}".format(child, get_weight(child)))
        print("====")

    return(weight + sum(child_weights))

node_hash = {}
for line in file:
    if "->" in line:
        node, child_str = line.strip().split(" -> ")
        children = child_str.split(", ")
        node, weight = node.split(" (")
        weight = weight[:-1]
    else:
        node = line.strip()
        node, weight = node.split(" (")
        weight = weight[:-1]
        children = []
    node_hash[node.strip()] = {"weight": int(weight), "children": children}

get_weight('ahnofa')

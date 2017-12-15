file = open("12-1.in", "r")
# file = open("12-1.in.sample", "r")

def parse_node(node_id, children):
    for child in children:
        if child not in connected:
            connected.add(child)
            parse_node(child, connections[child])

connections = {}
for line in file:
    node_id, con_str = line.strip().split(" <-> ")
    connections[int(node_id)] = [int(x) for x in con_str.split(", ")]

connected = set()
parse_node(0, connections[0])

print(len(connected))

file = open("7-1.in", "r")
# file = open("7-1.in.sample", "r")

nodes = []
all_children = []
for line in file:
    if "->" in line:
        node, child_str = line.strip().split(" -> ")
        children = child_str.split(", ")
        all_children = all_children + children
    else:
        node = line.strip()
        children = []
    nodes.append({"node": node.strip(), "children": children})

for node in nodes:
    node_name, _ = node['node'].split(" ")
    if node_name not in all_children:
        print(node_name)

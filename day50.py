#Write a program to detect Cycle in a directed graph.
print ("\nWilson - Day 50 of #100DaysOfCode\n")
print("Write a program to detect Cycle in a directed graph.")

def is_cyclic_directed(graph):
    def dfs(node, visited, rec_stack):
        visited[node] = True
        rec_stack[node] = True

        for neighbor in graph[node]:
            if not visited[neighbor]:
                if dfs(neighbor, visited, rec_stack):
                    return True
            elif rec_stack[neighbor]:
                return True

        rec_stack[node] = False
        return False

    num_nodes = len(graph)
    visited = [False] * num_nodes
    rec_stack = [False] * num_nodes

    for node in range(num_nodes):
        if not visited[node]:
            if dfs(node, visited, rec_stack):
                return True

    return False

def print_directed_graph(graph):
    for node, neighbors in graph.items():
        print(f"{node} -> {', '.join(map(str, neighbors))}")

directed_graph = {0: [1], 1: [2], 2: [0, 3], 3: [3]}

print("Directed Graph:")
print_directed_graph(directed_graph)

if is_cyclic_directed(directed_graph):
    print("directed graph contains a cycle")
else:
    print("directed graph does not contain a cycle")

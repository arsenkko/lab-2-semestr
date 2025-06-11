def read_tree(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        root = int(lines[0])
        tree = {}
        for line in lines[1:]:
            u, v = map(int, line.strip().split())
            if u not in tree:
                tree[u] = []
            tree[u].append(v)
    return root, tree

def BFS(root, tree):
    queue = [(root, 1)] 
    front = 0 

    while front < len(queue):
        node, depth = queue[front]
        front += 1

        if node not in tree:
            return depth

        for child in tree[node]:
            queue.append((child, depth + 1))

    return 0

def main():
    root, tree = read_tree(r'C:\IT\lab5.2semestr\input.txt')
    min_depth = BFS(root, tree)
    print("Мінімальна глибина дерева:", min_depth)
    with open(r'C:\IT\lab5.2semestr\output.txt', 'w') as out:
        out.write(str(min_depth))

if __name__ == "__main__":
    main()

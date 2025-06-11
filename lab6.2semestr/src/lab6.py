from collections import defaultdict, deque

def main():
    with open(r'C:\IT\lab6.2semestr\govern.in', 'r') as file:
        lines = file.read().splitlines()

    graph = defaultdict(list)
    indegree = defaultdict(int)
    all_docs = set()

    for line in lines:
        doc, prereq = line.split()
        graph[prereq].append(doc)
        indegree[doc] += 1
        all_docs.add(doc)
        all_docs.add(prereq)


    queue = deque()
    for doc in all_docs:
        if indegree[doc] == 0:
            queue.append(doc)

    order = []

    while queue:
        current = queue.popleft()
        order.append(current)

        for neighbor in graph[current]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    with open(r'C:\IT\lab6.2semestr\govern.out', 'w') as out_file:
        for doc in order:
            out_file.write(doc + '\n')

if __name__ == "__main__":
    main()

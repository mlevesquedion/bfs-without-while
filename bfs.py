def bfs(G):
    queue = [0]
    seen = set(queue)
    for x in queue:
        print(x)
        for neighbor in G[x]:
            if neighbor not in seen:
                queue.append(neighbor)


G = [
    [1, 3], [2], [], []]

if __name__ == "__main__":
    bfs(G)

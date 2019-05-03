def depth_first_search(problem, node, visited = set()):
    token = problem.token(node)
    if token in visited: return
    # we have tried this node already
    visited = visited.union(set([token]))
    # create new set that contains the node
    if problem.goal(node): return [node]
    # base case
    for n_succ in problem.succ(node):
        sol = depth_first_search(problem, n_succ, visited)
        if sol:
            #first path is returned
            return [node] + sol

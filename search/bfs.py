    search_struct = util.Queue()
    successors = problem.getSuccessors(problem.getStartState())

    path_actions = {}

    for ea in successors:
        search_struct.push(ea)

    find_goal = False

    visited_pos = set()
    visited_pos.add(problem.getStartState())

    # 开始遍历：如果栈不空，且没有到达目标结点(请填充如下两个条件)：
    while (not search_struct.isEmpty()) and (not find_goal):
        node = search_struct.pop()
        if not problem.isGoalState(node[0]):
            # 如果该节点没被访问
            if not node[0] in visited_pos:
                visited_pos.add(node[0])
            # filter的意思是对sequence中的所有item依次执行 function(item)
            choice_successors = filter(lambda v: v[0] not in visited_pos, problem.getSuccessors(node[0]))

            for ea in choice_successors:
                search_struct.push(ea)
                path_actions[ea[0]] = node

        else:
            path = []
            while node and not problem.getStartState() == node[0]:
                if node:
                    path.append(node[1])
                if path_actions.has_key(node[0]):
                    node = path_actions[node[0]]
                else:
                    break
            path.reverse()
            find_goal = True

    return path
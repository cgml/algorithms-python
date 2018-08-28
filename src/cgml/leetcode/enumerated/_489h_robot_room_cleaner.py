class Solution(object):
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        mem = {0: {0: 1}}
        robot.clean()
        self.helper((0, 0), mem, robot, -1, 0)
        self.helper((0, 0), mem, robot, 0, -1)
        self.helper((0, 0), mem, robot, 1, 0)
        self.helper((0, 0), mem, robot, 0, 1)

    def helper(self, state, mem, robot, tr, tc):
        if mem.get(tr) is None or mem[tr].get(tc) is None:
            mem[tr] = mem.get(tr, {})
            mem[tr][tc] = 1
        else:
            return
        nstate = self.move(state, (tr, tc), robot)
        if state == nstate: return
        robot.clean()
        self.helper(nstate, mem, robot, tr - 1, tc)
        self.helper(nstate, mem, robot, tr, tc - 1)
        self.helper(nstate, mem, robot, tr + 1, tc)
        self.helper(nstate, mem, robot, tr, tc + 1)
        self.move(nstate, state, robot)

    def move(self, state, nstate, robot):
        if state == nstate: return state
        r = True
        if state[0] > nstate[0]:
            robot.turnLeft()
            r = robot.move()
            robot.turnRight()
        elif state[1] > nstate[1]:
            r = robot.move()
        elif state[0] < nstate[0]:
            robot.turnRight()
            r = robot.move()
            robot.turnLeft()
        else:
            robot.turnRight()
            robot.turnRight()
            r = robot.move()
            robot.turnRight()
            robot.turnRight()
        return nstate if r else state


class SolutionDFS(object):
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        self.dfs(robot, 0, 0, 0, 1, set())

    def dfs(self, robot, x, y, direction_x, direction_y, visited):
        robot.clean()
        visited.add((x, y))

        for k in range(4):
            neighbor_x = x + direction_x
            neighbor_y = y + direction_y
            if (neighbor_x, neighbor_y) not in visited and robot.move():
                self.dfs(robot, neighbor_x, neighbor_y, direction_x, direction_y, visited)
                robot.turnLeft()
                robot.turnLeft()
                robot.move()
                robot.turnLeft()
                robot.turnLeft()
            robot.turnLeft()
            direction_x, direction_y = -direction_y, direction_x
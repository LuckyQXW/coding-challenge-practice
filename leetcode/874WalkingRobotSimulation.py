# Nothing special, just simulate robot moves with code
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        pos = [0, 0]
        degree = 90
        ans = 0
        obs = set()
        for item in obstacles:
            obs.add(tuple(item))
        for command in commands:
            if command == -1:
                degree = (degree - 90) % 360
            elif command == -2:
                degree = (degree + 90) % 360
            else:
                i = command
                if degree == 0:
                    while (i > 0 and (pos[0] + 1, pos[1]) not in obs):
                        pos[0] += 1
                        i -= 1
                elif degree == 90:
                    while (i > 0 and (pos[0], pos[1] + 1) not in obs):
                        pos[1] += 1
                        i -= 1  
                elif degree == 180:
                    while (i > 0 and (pos[0] - 1, pos[1]) not in obs):
                        pos[0] -= 1
                        i -= 1
                elif degree == 270:
                    while (i > 0 and (pos[0], pos[1] - 1) not in obs):
                        pos[1] -= 1
                        i -= 1
                ans = max(ans, pos[0] ** 2 + pos[1] ** 2)
        return ans  # Make sure to double check indentation!
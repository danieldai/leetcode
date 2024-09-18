from typing import List


class Solution:
    def __init__(self) -> None:
        self.candidates = []
        self.path = []

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        self.backtracking(tickets, [False] * len(tickets))
        # print(self.candidates)
        result = ["JFK"]

        for tickets in self.candidates[0]:
            result.append(tickets[-1])

        return result

    def backtracking(self, tickets, used):
        if len(self.path) == len(tickets):
            self.candidates.append(self.path[:])
            return
        
        for i in range(len(tickets)):
            departure = self.path[-1][-1] if self.path else "JFK"
            if tickets[i][0] != departure:
                continue

            if used[i]:
                continue

            used[i] = True
            self.path.append(tickets[i])
            self.backtracking(tickets, used)
            self.path.pop()
            used[i] = False


class Solution2:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.adj = {}

        # sort by the destination alphabetically
        # 根据航班每一站的重点字母顺序排序
        tickets.sort(key=lambda x:x[1])

        # get all possible connection for each destination
        # 罗列每一站的下一个可选项
        for u,v in tickets:
            if u in self.adj: self.adj[u].append(v)
            else: self.adj[u] = [v]

        # 从JFK出发
        self.result = []
        self.dfs("JFK")  # start with JFK

        return self.result[::-1]  # reverse to get the result

    def dfs(self, s):
        # if depart city has flight and the flight can go to another city
        while s in self.adj and len(self.adj[s]) > 0:
            # 找到s能到哪里，选能到的第一个机场
            v = self.adj[s][0]  # we go to the 1 choice of the city
            # 在之后的可选项机场中去掉这个机场
            self.adj[s].pop(0)  # get rid of this choice since we used it
            # 从当前的新出发点开始
            self.dfs(v)  # we start from the new airport

        self.result.append(s)  # after append, it will back track to last node, thus the result list is in reversed order

        
        print(self.result)


if __name__ == "__main__":
    tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
    result = Solution2().findItinerary(tickets)
    print(result)
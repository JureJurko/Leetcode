class DSU:
    def __init__(self, n):
        self.rank = {}
        self.par = {}

        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0
    
    def find(self, x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x
    
    def union(self, x, y):
        p_x = self.find(x)
        p_y = self.find(y)

        if self.rank[p_x] > self.rank[p_y]:
            self.par[p_y] = p_x
        elif self.rank[p_x] < self.rank[p_y]:
            self.par[p_x] = p_y
        else:
            self.par[p_x] = p_y
            self.rank[p_y] += 1
        return True
        



class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dsu = DSU(len(accounts))
        email_to_account = {}

        for i, account in enumerate(accounts):
            for j in range(1, len(account)):
                if account[j] in email_to_account:
                    dsu.union(i, email_to_account[account[j]])
                else:
                    email_to_account[account[j]] = i
        
        emailGroup = defaultdict(list)

        for e, i in email_to_account.items():
            leader = dsu.find(i)
            emailGroup[leader].append(e)

        res = []
        for i, emails in emailGroup.items():
            name = accounts[i][0]
            res.append([name] + sorted(emailGroup[i]))
        return res















        
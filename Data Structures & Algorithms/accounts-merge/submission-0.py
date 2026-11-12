class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)

        parent = [i for i in range(n)]
        rank = [1] * n

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(u, v):
            a, b = find(u), find(v)
            if a == b:
                return False
            if rank[a] < rank[b]:
                a, b = b, a
            
            parent[b] = a
            rank[a] += rank[b]
            return True


        email_to_account = {}

        for i, account in enumerate(accounts):
            for e in account[1:]:
                if e in email_to_account:
                    union(i, email_to_account[e])
                else:
                    email_to_account[e] = i

        email_group = defaultdict(list)

        for email, ind in email_to_account.items():
            leader = find(ind)
            email_group[leader].append(email)

        res = []

        for i, emails in email_group.items():
            name = accounts[i][0]
            res.append([name] + sorted(emails))

        return res

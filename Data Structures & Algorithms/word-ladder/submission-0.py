class Solution:
    # Simply copied from the solution wtf
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if (endWord not in wordList) or (beginWord == endWord):
            return 0

        n, m = len(wordList), len(wordList[0])
        adj = [[] for _ in range(n)]
        mp = {}
        for i in range(n):
            mp[wordList[i]] = i

        for i in range(n):
            for j in range(i + 1, n):
                cnt = 0
                for k in range(m):
                    if wordList[i][k] != wordList[j][k]:
                        cnt += 1
                if cnt == 1:
                    adj[i].append(j)
                    adj[j].append(i)

        q, res = deque(), 1
        visit = set()
        for i in range(m):
            for c in range(97, 123):
                if chr(c) == beginWord[i]:
                    continue
                word = beginWord[:i] + chr(c) + beginWord[i + 1:]
                if word in mp and mp[word] not in visit:
                    q.append(mp[word])
                    visit.add(mp[word])

        while q:
            res += 1
            for i in range(len(q)):
                node = q.popleft()
                if wordList[node] == endWord:
                    return res
                for nei in adj[node]:
                    if nei not in visit:
                        visit.add(nei)
                        q.append(nei)

        return 0
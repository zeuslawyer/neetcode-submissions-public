class UnionFind:
    def __init__(self, n):
        self.parentOf = {i:i for i in range(n)}
        self.rankOf ={i:0 for i in range(n)}
    
    def union(self, n1, n2) -> bool:
        p1, p2 = self.findParent(n1), self.findParent(n2)
        
        if p1 == p2: return False # no union possible
        
        # union done
        r1, r2 = self.rankOf[p1], self.rankOf[p2]
        if r1 > r2: 
            self.parentOf[p2] = p1
        elif r2 > r1:
            self.parentOf[p1] = p2
        else:
            # they're equal rankOf
            self.parentOf[p2] = p1
            self.rankOf[p1] += 1

        return True
    
    def findParent(self, n) -> int:
        # if n != self.parentOf[n]:
        #     self.parentOf[n] = self.findParent(self.parentOf[n])
        # return self.parentOf[n]
        # Alt -- FIND THE ROOT PARENT
        par = self.parentOf[n]
        while par != self.parentOf[par]:
            par = self.parentOf[par]
        
        self.parentOf[n] = par
        return par


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))

        # construct map and union related accounts
        emailToIdx = {}
        for i in range(len(accounts)):
            emails = accounts[i][1:] # slice off the name
            for e in emails:
                if not e in emailToIdx:
                    emailToIdx[e] = i
                else:
                    # email already in the map
                    uf.union(i, emailToIdx[e])
        
        # collect and sort emails for each unique accounts
        combinedEmails = {} # map of parent index to all related account emails

        for i in range(len(accounts)):
            par = uf.findParent(i)
            parAcc = accounts[par]
            relatedAcc = accounts[i]
            if par not in combinedEmails:
                combinedEmails[par] = set()
            combinedEmails[par].update(parAcc[1:] + relatedAcc[1:])

        res = []

        for accIdx in combinedEmails:
            emails = sorted(combinedEmails[accIdx])
            name = accounts[accIdx][0]
            res.append([name] + emails)
        
        return res

        

        


        
            

       
       
        newaccounts = []
       
        
        return newaccounts



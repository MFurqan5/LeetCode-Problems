class Solution(object):
    def resultArray(self, nums, k, queries):
        n = len(nums)
        
        def merge(L, R):
            VL, PL = L
            VR, PR = R
            V = [0] * k
            for p in range(k):
                V[p] += VL[p]
            for p in range(k):
                if VR[p]:
                    V[(p * PL) % k] += VR[p]
            P = (PL * PR) % k
            return (V, P)
        
        def make_leaf(val):
            r = val % k
            V = [0] * k
            V[r] += 1
            return (V, r)
        
        size = 1
        while size < n:
            size *= 2
        
        # Identity: empty segment — product = 1, no indices
        ID = ([0] * k, 1)
        
        tree = [ID] * (2 * size)
        for i in range(n):
            tree[size + i] = make_leaf(nums[i])
        for i in range(size - 1, 0, -1):
            tree[i] = merge(tree[2 * i], tree[2 * i + 1])
        
        res = []
        for idx, val, start, x in queries:
            # Point update
            p = size + idx
            tree[p] = make_leaf(val)
            p //= 2
            while p:
                tree[p] = merge(tree[2 * p], tree[2 * p + 1])
                p //= 2
            
            # Query range [start, n-1]
            l, r = start + size, n - 1 + size
            left_acc = ID
            right_acc = ID
            while l <= r:
                if l % 2 == 1:
                    left_acc = merge(left_acc, tree[l])
                    l += 1
                if r % 2 == 0:
                    right_acc = merge(tree[r], right_acc)
                    r -= 1
                l //= 2
                r //= 2
            
            total = merge(left_acc, right_acc)
            V, _ = total
            res.append(V[x])
        
        return res
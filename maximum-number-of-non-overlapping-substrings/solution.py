class Solution(object):
    def maxNumOfSubstrings(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        
        first = {}
        last = {}
        for i, c in enumerate(s):
            if c not in first:
                first[c] = i
            last[c] = i
        
        intervals = []
        for c in first:
            start = first[c]
            end = last[c]
            i = start
            while i <= end:
                ch = s[i]
                if first[ch] < start:
                    end = -1
                    break
                end = max(end, last[ch])
                i += 1
            
            if end != -1:
                intervals.append((start, end))
        
        intervals.sort(key=lambda x: (x[1], x[0]))
        
        result = []
        last_end = -1
        for start, end in intervals:
            if start > last_end:
                result.append(s[start:end + 1])
                last_end = end
        
        return result
class Solution(object):
    def braceExpansionII(self, expression):
        """
        :type expression: str
        :rtype: List[str]
        """
        def parse(i):
            # Returns (set_of_words, next_index)
            result = set()
            current = {""}
            
            while i < len(expression):
                c = expression[i]
                if c == '{':
                    sub, i = parse(i + 1)
                    current = {a + b for a in current for b in sub}
                elif c == '}':
                    result |= current
                    return result, i + 1
                elif c == ',':
                    result |= current
                    current = {""}
                    i += 1
                else:
                    current = {a + c for a in current}
                    i += 1
            
            result |= current
            return result, i
        
        words, _ = parse(0)
        return sorted(words)
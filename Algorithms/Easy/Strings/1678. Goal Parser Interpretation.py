# https://leetcode.com/problems/goal-parser-interpretation/

def interpret(self, command: str) -> str:
        res = []
        
        for i in range(0,len(command)):
            if command[i] == 'G':
                res.append('G')
            if command[i] == '(' and command[i+1]==')':
                res.append('o')
            if command[i] == 'a' and command[i+1]=='l':
                res.append('al')
        return ''.join(res)

# Runtime: 42 ms
# Memory Usage: 13.9 MB

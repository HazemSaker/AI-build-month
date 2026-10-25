class Solution:
    def isValid(self, s: str) -> bool:
        visited = []

        for i in range(len(s)):
            if not visited:
                visited.append(s[i])
            elif visited[-1] == "(" and s[i] == ")":
                visited.pop(-1)
            elif visited[-1] == "[" and s[i] == "]":
                visited.pop(-1)
            elif visited[-1] == "{" and s[i] == "}":
                visited.pop(-1)
            else:
                visited.append(s[i])
           
        return not bool(visited)
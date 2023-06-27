class Solution:
    def decodeString(self, s: str) -> str:
            stack = []
            for c in s:
                if c == ']':
                    decoded_str = ''
                    while stack[-1] != '[':
                        decoded_str = stack.pop() + decoded_str
                    stack.pop()  # Pop '['
                    k_str = ''
                    while stack and stack[-1].isdigit():
                        k_str = stack.pop() + k_str
                    k = int(k_str)
                    decoded_str *= k
                    for dc in decoded_str:
                        stack.append(dc)
                else:
                    stack.append(c)
            return ''.join(stack)
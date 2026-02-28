def is_valid_parentheses(s: str) -> bool:
    stack = []
    # Map closing brackets to their matching opening brackets
    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    
    for char in s:
        # If it's a closing bracket
        if char in pairs:
            # Pop the top element if stack isn't empty, else use a dummy value
            top_element = stack.pop() if stack else '#'
            
            # If the popped element doesn't match the required opening bracket
            if pairs[char] != top_element:
                return False
        else:
            # It's an opening bracket, push it onto the stack
            stack.append(char)
            
    # If the stack is empty, all brackets were matched correctly
    return len(stack) == 0
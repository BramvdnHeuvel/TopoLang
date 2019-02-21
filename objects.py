def test_levels(data_set):
    """Check if all brackets are done correctly."""
    stack = []
    haakjes = {'{': '}', '[': ']', '(': ')'}

    for sign in data_set:
        char = sign[0]

        if char in haakjes:
            stack.append((haakjes[char],sign))
            current_line = sign[1]
            current_column = sign[2]
        
        if len(stack) > 0 and char == stack[-1][0]:
            stack.pop()
            # TODO: Make sure the closing bracket is followed by an operator, a closing bracket of or a ;.
    
    return stack == []
import sys
import re

# A dictionary to convert Roman numerals to integers
roman_to_int_map = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50,
    'C': 100, 'D': 500, 'M': 1000
}

def roman_to_int(roman):
    """
    Convert Roman numeral to integer.

    Args:
        roman (str): A Roman numeral string.

    Returns:
        int: The integer value of the Roman numeral.

    Raises:
        KeyError: If the Roman numeral contains invalid characters.
    """
    total = 0
    prev_value = 0
    
    # Loop through each character from right to left
    for char in reversed(roman): 
        value = roman_to_int_map[char]  # Get integer value for char
        if value < prev_value:
            total -= value  # Subtract if current value is less than previous
        else:
            total += value  # Otherwise, add it
        prev_value = value  # Update previous value
    return total

def int_to_roman(num):
    """
    Convert integer to Roman numeral.

    Args:
        num (int): An integer value.

    Returns:
        str: The Roman numeral representation.

    Raises:
        ValueError: If num <= 0 or num > 3999.
    """
    if num <= 0:
        raise ValueError("Negative numbers can't be represented in Roman numerals.")
    if num > 3999:
        raise ValueError("You're going to need a bigger calculator.")
        
    result = ""
    values = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
        (1, 'I')
    ]
    
    # Loop through values and create the Roman numeral
    for value, numeral in values:
        while num >= value:  # While num is larger than value
            result += numeral  # Add the numeral to result
            num -= value  # Subtract value from num
    return result

def evaluate_expression(expression):
    """
    Evaluate a math expression with Roman numerals.

    Args:
        expression (str): The expression with Roman numerals.

    Returns:
        str: Result as a Roman numeral or an error message.

    Raises:
        ValueError: If the expression has invalid syntax.
        ZeroDivisionError: If dividing by zero.
    """
    # Replace Roman numerals with their integer values in the expression
    expression = re.sub(r'\b([IVXLCDM]+)\b', lambda match: str(roman_to_int(match.group(0))), expression)
    
    try:
        expression = expression.replace("[", "(")
        expression = expression.replace("]",")")
        result = eval(expression)  # Evaluate the expression
        
        if result == 0:
            return "0 does not exist in Roman numerals."
        elif result < 0:
            return "Negative numbers can't be represented in Roman numerals."
        elif result > 3999:
            return "You're going to need a bigger calculator."
        elif isinstance(result, float):
            return "There is no concept of a fractional number in Roman numerals."
        else:
            return int_to_roman(result)  # Convert result back to Roman numeral
    except (ValueError, SyntaxError, TypeError):
        return "I don't know how to read this."
    except ZeroDivisionError:
        return "I don't know how to read this."  # Division by zero case

def main():
    """
    Main function to run the calculator.

    Returns:
        None
    """
    if len(sys.argv) < 2:  # If no input provided
        print("I don't know how to read this.")
        return
    
    input_expression = ' '.join(sys.argv[1:])  # Combine arguments into a single expression
    result = evaluate_expression(input_expression)  # Evaluate the expression
    print(result)  # Print the result

# Run the main function when script is executed
if __name__ == "__main__":
    
    main()

import re

def extract_review_number(input_string):
    # Regular expression pattern to match a number followed by a space and "review"
    pattern = r'(\d+)\s+review'
    
    # Search for the pattern in the input string
    match = re.search(pattern, input_string)
    
    # If a match is found, return the number as an integer
    if match:
        return int(match.group(1))
    
    # If no match is found, return None
    return None

# Test examples
print(extract_review_number("This product has 5 reviews and is highly recommended."))  # Output: None
print(extract_review_number("This product has 5 review and is highly recommended."))   # Output: 5
print(extract_review_number("There are 10 review on this product."))                   # Output: 10
print(extract_review_number("10 reviews"))  
print(extract_review_number("No reviews available."))                                  # Output: None

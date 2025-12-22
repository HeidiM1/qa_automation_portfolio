# My day 1 Extra Practice - making it feel real
def test_qa_mindset():
    """Testing is just checking if things work as expected"""

#Example 1: Testing a simple calculation
    print("Test 1: Basic Math Check")
    result = 10 * 2
    expected = 20
    assert result == expected, f"Math failed:  {result} != {expected}"
    print("Calculator works")
#Example 2: Testing string functionality (like checking error messages)"
    print ("\nTest 2: String validation")
    error_message = "Invalid username"
    assert "Invalid" in error_message, "Error message missing key word"
    print ("Error message contains 'Invalid'")

#Example 3: Testing a list (like checking drop down options)
    print("\nTest 3: Dropdown options check")
    dropdown_options = ["Admin", "User", "Guest"]
    assert "User" in dropdown_options, "User option missing"
    print("Dropdown contains 'User' role")

    print("\nAll QA-style checks passed! This is the mindset")



if __name__ == "__main__":
    test_qa_mindset()
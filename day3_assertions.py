# DAY 3: Professional Test Structure
# Learning to use assertions instead of print()


def test_with_proper_assertions():
    # Real test use assert, not print() checking

    print("Testing with assertions")
    print ("=" * 50 )
    
    #example 1: Simple Assertion
    result = 10 * 2
    expected = 20
    assert result == expected, f"Math failed: {result} != {expected}"
    print("simple assertion passed")
    
    #Example 2: Testing login logic 
    users_db = {"admin": "Admin123!", "user": "Password123"}

    username = "admin"
    assert username in users_db, f"User {username} should exsist"
    assert users_db[username] == "Admin123!", "Password should match"
    print("Login validation passed")

    #Example 3: Testing error cases
    invalid_user = "hacker"
    try:
        assert invalid_user in users_db, "Should fail for non-exsisting user"
        print("Should have failed")
    except AssertionError as e:
        print(f"Correctly rejected: {e}")
        



def run_tests():
    # professional test runner"""
    tests = [test_with_proper_assertions]

    print("\n Running test suite")
    for test in tests: 
        try:
            test()
            print(f"    {test.__name__}: PASS")
        except AssertionError as e:
            print(f"    {test.__name__}: FAIL - {e}")
        except Exception as e:
            print(f"    {test.__name__}: ERROR - {e}")

    print("\n Day 3 complete: using assertions like a pro!")


if __name__ == "__main__":
    run_tests()

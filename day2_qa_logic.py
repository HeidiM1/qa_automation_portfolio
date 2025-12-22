#Day 2: translating manual QA thinking to code
#Thinking like a manual tester, coding like an automator.



def test_login_scenarios():
    """Testing login functionality  - just like you would manually"""

    print("\n" + "=" * 50)
    print("Manual Test Scenario: Login Functionality")
    print("=" * 50)

    #simulated database (normally this would be a real database)
    valid_users = {
        "admin": "admin@123",
        "qa_tester": "TestPass!23",
        "user": "simple123"
        }
    
    username = "qa_tester"
    password = "password123"

    # Test Case 1: valid credentials (happy path)
    print("\n Test case 1: Valid Credentials")
    print("  Manual step: Enter currect username and password")
    valid_users = {
        "admin": "admin@123",
        "qa_tester": "TestPass!23",
        "user": "simple123"
        }
    
    username = "qa_tester"
    password = "password123"

#Manual: Click login, verify dashboard appears
#Automated: Check if credentials match

    if username in valid_users and valid_users[username] == password:
        print("  PASS: login successful (dashboard would load)")
        result = True
    else:
        print(" FAIL: Login failed")
        result = False

    #Test case 2: Wrong password (negative test)
    print("\n Test Case 2: wrong password")
    print("  Manual step: enter valig username with wrong password")
    valid_users = {
        "admin": "admin@123",
        "qa_tester": "TestPass!23",
        "user": "simple123"
        }
    
    username = "qa_tester"
    password = "password123"
    
    if username in valid_users and valid_users[username] == password:
        print("FAIL: Should have rejected wrong password")
        result = False
    else:
        print("  PASS: Correctly rejected invalid credentials")
        result = True

    #test case 3 : non-exsistent user
    print("\n Test case 3: non-exsistent user")
    print("  Manual step: enter username that dosen't exsist")

    valid_users = {
            "admin": "admin123",
            "testuser": "password123",
            "guest": "guest123"
            }
    username = "nonexsistent"
    password = "anything"

    if username in valid_users:
        print("FAIL: User shouldn't exsist")
        result = False
    else:
        print("  PASS: Correctly identified unknown user")
        result = True

def test_form_validation():
    """Testing form fields - like checking required fields manually"""

    print("\n" + "=" * 50)
    print("MANUAL TEST SCENARIO: Form Validation ")
    print("=" * 50)

    #simulating a form submission
    form_data = {
         "username": "heidi123",
         "email": "heidi@example.com",
         "password": "", #empty, should fail
         "terms_accepted": True
    }

    print("\n Test Case: Required Fields Check")
    print("   Manual step: submit firm with missing required field")

    errors = []

    #Check each field (just like you would manually)
    if not form_data["username"]:
         errors.append("Username is required")
    if not form_data["email"]:
         errors.append("Email is required")
    if not form_data["password"]:
         errors.append("password is required")
    if not form_data["terms_accepted"]:
         errors.append("must accept terms")
        
    #Manual: verify error message appears
    #Automated: Check if we got the expected error
    if "password is required" in errors:
         print("   PASS: Correctly flagged missing password")
         print(f"   Error messages: {errors}")
    else:
         print("FAIL: Should have flagged missing password")

def test_boundry_values():
     #Testing edge cases - like you would in exploratory testing

    print("\n" + "=" * 50)
    print("MANUAL TEST SCENARIO: Boundry Testing ")
    print("=" * 50)

    #Testing age field boundries
    print("Test Case: Age field boundries")
    print("Manual Step: Try Entering edge case values")

    test_ages = [0,1,17,18,99,100,101] #boundry values

    for age in test_ages:
         #business rule: age must be 18-100
        if 18 <= age <= 100:
            print(f"Age {age}: valid")
        else:
            print(f"Age {age}: Invalid")


if __name__ == "__main__":
    print("\n DAY 2: From Manual QA to Automation Thinking")
    print("Converting manual test cases to automated logic   \n")

    test_login_scenarios()
    test_form_validation()
    test_boundry_values()

    print("\n" + "=" * 50)
    print("SUMMARY: You just automated 3 manual test scenarios!")
    print("These are exact check you'd do manually")
    print("now running in code. This is automation thinking")
    print("=" * 50)
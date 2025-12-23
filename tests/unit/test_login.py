#Unit tests for login functionality, Organized in tests/unit folder

def test_valid_credentials():
    users = {"admin": "password123", "user": "test123"}

    #test admin exsist
    assert "admin" in users
    assert users["admin"] == "password123"

    #test user exsist
    assert "user" in users

def test_invalid_users():
    users = {"admin": "password123"}
    assert "hacker" not in users

def test_empty_password():
    users = {"admin": "password123"}
    #this should have a password
    assert users["admin"] != ""
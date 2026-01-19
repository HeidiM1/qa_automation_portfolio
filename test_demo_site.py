"""
Smooth learning with a stable demo site
No CAPTCHAs, no cookies, no regional issues
Just pure automation learning
"""

from playwright.sync_api import sync_playwright

def test_login_form():
    """Test a simple login form - foundational skill"""
    
    print("Testing login form on demo site...")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # Go to predictable demo site
        page.goto("https://the-internet.herokuapp.com/login")
        
        # Take screenshot
        page.screenshot(path="demo_login_page.png")
        print("Screenshot: demo_login_page.png")
        
        # Fill login form
        page.fill("#username", "tomsmith")
        page.fill("#password", "SuperSecretPassword!")
        print("testing with correct credentials")
        
        # Click login
        page.click("button[type='submit']")
        
        # Wait for success
        page.wait_for_selector("#flash")
        
        # Verify success message
        success_text = page.locator("#flash").inner_text()
        print(f"DEBUG: Actual text received: '{success_text}'")
        assert "You logged into a secure area!" in success_text
        
        page.screenshot(path="demo_login_success.png")
        print("Screenshot: demo_login_success.png")
        print("✓ Login successful")
        
        # Logout
        page.click("a[href='/logout']")
        page.wait_for_selector("#flash")
        
        logout_text = page.locator("#flash").inner_text()
        assert "You logged out of the secure area!" in logout_text
        
        page.screenshot(path="demo_logout_success.png")
        print("Screenshot: demo_logout_success.png")
        print("✓ Logout successful")
        
        browser.close()
        
        print("\n✅ COMPLETE: Login/logout flow automated successfully")
        return True
    
        #Custom verification: Check page title
        page_title = page_title()
        print(f"Page Title after login: {page_title}")
        assert "Secure Area" in page_title


        #Custom verification: Check URL contains "secure"
        current_url = page_url
        print(f"Current URL: {current_url}")
        assert "secure" in current_url

        
if __name__ == "__main__":
    test_login_form()

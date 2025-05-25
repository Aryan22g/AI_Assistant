from selenium import webdriver

def open_url_in_browser(query_or_url, browser="chrome"):
    """
    Opens the given URL or search query in the specified browser using Selenium.
    If the input is not a full URL, performs a Google search.
    """
    # Check if input looks like a URL
    if query_or_url.startswith("http://") or query_or_url.startswith("https://"):
        url = query_or_url
    else:
        # Treat as search query
        from urllib.parse import quote_plus
        search_query = quote_plus(query_or_url)
        url = f"https://www.google.com/search?q={search_query}"

    driver = None
    try:
        if browser.lower() == "chrome":
            driver = webdriver.Chrome()
        elif browser.lower() == "firefox":
            driver = webdriver.Firefox()
        else:
            print(f"Unsupported browser: {browser}")
            return

        driver.get(url)
        print("Page title:", driver.title)
        input("Press Enter to close the browser...")  # Keeps the browser open until you press Enter

    except Exception as e:
        print("Error:", e)
    finally:
        if driver:
            driver.quit()

open_url_in_browser("https://www.python.org", browser="chrome")  # Opens the website
open_url_in_browser("python download", browser="chrome")         # Performs a Google search

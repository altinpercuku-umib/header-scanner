import requests


# Security Headers We Want To Check For :

SECURITY_HEADERS = {
    "Strict-Transport-Security": (
        "Forces browsers to always use HTTPS for this site, "
        "which protects visitors from downgrade and man-in-the-middle attacks."
    ),
    "Content-Security-Policy": (
        "Controls which scripts, styles and other resources the page may load, "
        "which is the main defense against cross-site scripting (XSS)."
    ),
    "X-Frame-Options": (
        "Stops other sites from embedding this page in an iframe, "
        "which prevents clickjacking attacks."
    ),
    "X-Content-Type-Options": (
        "Stops browsers from guessing a file's type, "
        "so a malicious upload can't be run as a script."
    ),
    "Referrer-Policy": (
        "Limits how much of the page URL is shared with other sites when visitors click a link, "
        "which keeps private paths and tokens from leaking."
    ),
    "Permissions-Policy": (
        "Restricts which browser features (camera, microphone, location) the page and its "
        "embedded content can use."
    ),
}


website = input("Test Website: ").strip() # Website Iput For Headers Check

if not website.startswith(("https://", "http://")): # checks if the website contains the 'https/http' and adds it if its not
    website = "https://" + website
try:
    r = requests.get(website, timeout=(5,10)) # the response
    counter = 0
    for key, value in SECURITY_HEADERS.items():
        if key in r.headers:
            counter = counter + 1 # header counter
            print(f"YES: {key} - {value}")
        else:
            print(f"No: {key} - {value}")
    print(f"Found {counter}/{len(SECURITY_HEADERS)} headers") # header messsage

except requests.exceptions.ConnectTimeout:
    print("Failed to connect to the server within the specified time (5).")
except requests.exceptions.ReadTimeout:
    print("The server did not send data/respond within the read timeout period.")
except requests.RequestException as e:
    print("Friendly code so the page dont crash")
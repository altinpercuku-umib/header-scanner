import requests


# Security Headers We Want To Check For :

SECURITY_HEADERS = {
    "Strict-Transport-Security": {
        "points": 25,
        "explanation": (
            "Forces browsers to always use HTTPS for this site, "
            "which protects visitors from downgrade and man-in-the-middle attacks."
        ),
    },
    "Content-Security-Policy": {
        "points": 25,
        "explanation": (
            "Controls which scripts, styles and other resources the page may load, "
            "which is the main defense against cross-site scripting (XSS)."
        ),
    },
    "X-Frame-Options": {
        "points": 15,
        "explanation": (
            "Stops other sites from embedding this page in an iframe, "
            "which prevents clickjacking attacks."
        ),
    },
    "X-Content-Type-Options": {
        "points": 15,
        "explanation": (
            "Stops browsers from guessing a file's type, "
            "so a malicious upload can't be run as a script."
        ),
    },
    "Referrer-Policy": {
        "points": 10,
        "explanation": (
            "Limits how much of the page URL is shared with other sites when visitors click a link, "
            "which keeps private paths and tokens from leaking."
        ),
    },
    "Permissions-Policy": {
        "points": 10,
        "explanation": (
            "Restricts which browser features (camera, microphone, location) the page and its "
            "embedded content can use."
        ),
    },
}


def get_grade(score): # function that returns the score
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 40:
        return "D"
    else:
        return "F"


website = input("Test Website: ").strip() # Website Iput For Headers Check

if not website.startswith(("https://", "http://")): # checks if the website contains the 'https/http' and adds it if its not
    website = "https://" + website
try:
    r = requests.get(website, timeout=(5,10)) # the response
    counter = 0
    score = 0
    for key, value in SECURITY_HEADERS.items():
        if key in r.headers:
            counter += 1
            score += value["points"]
            print(f"YES: {key}")
        else:
            print(f"No: {key} - {value['explanation']}")

    print(f"Found {counter}/{len(SECURITY_HEADERS)} headers")
    print(f"Score: {score}/100, Grade: {get_grade(score)}")

except requests.exceptions.ConnectTimeout:
    print("Failed to connect to the server within the specified time (5).")
except requests.exceptions.ReadTimeout:
    print("The server did not send data/respond within the read timeout period.")
except requests.RequestException as e:
    print("Friendly code so the page dont crash")
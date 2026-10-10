# Header Scanner

A Python tool that checks any website for important HTTP security headers
and explains in plain language what each missing one protects against.

## Why I built this
I did this to have a better understanding of how requests in python are and learn about secure headers

## Headers checked
- Strict-Transport-Security
- Content-Security-Policy
- X-Frame-Options
- X-Content-Type-Options
- Referrer-Policy
- Permissions-Policy

## How to run
```
pip install requests
python scanner.py
```

## Example output
```
Test Website: github.com
YES: Strict-Transport-Security
YES: Content-Security-Policy
YES: X-Frame-Options
YES: X-Content-Type-Options
YES: Referrer-Policy
No: Permissions-Policy - Restricts which browser features (camera, microphone, location) the page and its embedded content can use.
Found 5/6 headers
Score: 90/100, Grade: A
```

## Planned
- A–F letter grade
- HTTPS redirect and cookie checks
- Web version with Django + React

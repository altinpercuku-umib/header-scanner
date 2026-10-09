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
(paste a real scan result here, e.g. for example.com)
```

## Planned
- A–F letter grade
- HTTPS redirect and cookie checks
- Web version with Django + React

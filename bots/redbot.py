#!/usr/bin/env python3

"""
Posting bot
"""

import requests
from reddit_api import upvoted

login_url = "http://localhost:5000/login"

login_payload = {
    "email": "redbot@dev.co",
    "password": "redbot",
}

session = requests.Session()
login_response = session.post(login_url, data=login_payload)

if login_response.status_code == 200:
    print("Logged in successfully")
    r_post = upvoted("UFOS")
    
    if r_post:
        post_data = {
            "title": r_post['title'],
            "content": f"{r_post['content']} {r_post['link']}",
            "submit": 'Submit'
            }
        cp_url = "http://localhost:5000/new/post"
        post_response = session.post(cp_url, data=post_data)

    if post_response.status_code == 201:
        print("Post created successfully")
    else:
        print(f"Failed to create post: {post_response.status_code}")
    session.close()
else:
    print(f"Failed to log in: {login_response.status_code}")

print(r_post['title'])
"""
#The foolowing code is intended to actually test that the bot has logged in
url = "http://localhost:5000/home"
response = requests.get(url)
html_content = response.text
print(html_content[:200])
"""

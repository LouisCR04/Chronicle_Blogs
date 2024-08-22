#!/usr/bin/python3
import sys
import requests

def upvoted(subreddit):
    """Fetches the most upvoted post with non-empty content from a specified subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/top/.json"
    headers = {
        "User-Agent": "linux: api-advanced:V2.0 (by u/random)"
    }
    params = {
        "t": "all",  # Fetch top posts of all time
        "limit": 10  # Fetch top 10 posts to filter for non-empty content
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    try:
        if response.status_code == 404:
            print("Subreddit not found")
            return
        results = response.json().get("data").get("children")
        if not results:
            print("No posts found")
            return

        # Filter for the first post with non-empty selftext
        for post_data in results:
            post = post_data.get("data")
            content = post.get("selftext")
            if content:  # Ensure there's content
                title = post.get("title")
                author = post.get("author")
                upvotes = post.get("ups")
                link = post.get("url")
                return {"title": title, "author": author, "upvotes": upvotes, "content": content, "link": link}

        print("No posts with non-empty content found")
        return

    except Exception as e:
        print(f"Error occurred: {e}")
        return


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: {} <subreddit>".format(sys.argv[0]))
    else:
        subreddit = sys.argv[1]
        result = upvoted(subreddit)
        if result:
            print(f"Title: {result['title']}")
            print(f"Author: {result['author']}")
            print(f"Upvotes: {result['upvotes']}")
            print(f"Content: {result['content']}")
            print(f"Link: {result['link']}")

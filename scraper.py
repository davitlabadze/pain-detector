import requests

# ------------ Reddit -------------
def get_reddit_posts(subreddits=None, limit=20):
    if subreddits is None:
        subreddits = ['devops', 'sysadmin', 'kubernetes', 'aws', 'terraform']
    
    headers = {'User-Agent': 'PainDetector/0.1'}
    all_posts = []

    for subreddit in subreddits:
        url = f'https://www.reddit.com/r/{subreddit}/new.json?limit={limit}'
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            data = response.json()
            for child in data.get('data', {}).get('children', []):
                post = child.get('data', {})
                text = post.get('title', '') + " " + post.get('selftext', '')
                if text.strip():
                    # Reddit link
                    post_link = f"https://reddit.com{post.get('permalink', '')}"
                    all_posts.append({
                        "text": text,
                        "link": post_link
                    })
        except Exception as e:
            print(f"Error fetching subreddit {subreddit}: {e}")

    return all_posts

# ------------ GitHub -------------
def get_github_issues(repos=None, limit=10):
    if repos is None:
        repos = [
            'prometheus/prometheus',
            'kubernetes/kubernetes',
            'hashicorp/terraform',
            'ansible/ansible'
        ]
    
    issues_list = []

    for repo in repos:
        url = f'https://api.github.com/repos/{repo}/issues?state=open&per_page={limit}'
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            for issue in data:
                if "pull_request" in issue:
                    continue
                text = issue.get('title', '') + " " + (issue.get('body') or '')
                if text.strip():
                    issues_list.append({
                        "text": text,
                        "link": issue.get("html_url")
                    })
        except Exception as e:
            print(f"Error fetching repo {repo}: {e}")

    return issues_list

# ------------ Combine all texts -------------
def get_texts():
    reddit_posts = get_reddit_posts(limit=15)
    github_issues = get_github_issues(limit=10)
    return reddit_posts + github_issues

# ------------- Test Example -------------
if __name__ == "__main__":
    texts = get_texts()
    print(f"Fetched {len(texts)} posts/issues:")
    for t in texts[:5]:
        print("-", t["text"][:120], "... Link:", t["link"])

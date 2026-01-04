import requests

def get_reddit_posts(subreddit='devops', limit=10):
    headers = {'User-Agent': 'PainDetector/0.1'}
    url = f'https://www.reddit.com/r/{subreddit}/new.json?limit={limit}'
    response = requests.get(url, headers=headers)
    data = response.json()
    posts = []
    for child in data['data']['children']:
        post = child['data']
        posts.append(post['title'] + " " + post.get('selftext', ''))
    return posts

def get_github_issues(repo='prometheus/prometheus', limit=5):
    url = f'https://api.github.com/repos/{repo}/issues?state=open&per_page={limit}'
    response = requests.get(url)
    data = response.json()
    issues = []
    for issue in data:
        issues.append(issue['title'] + " " + issue.get('body', ''))
    return issues

def get_texts():
    reddit_posts = get_reddit_posts(limit=10)
    github_issues = get_github_issues(limit=5)
    return reddit_posts + github_issues

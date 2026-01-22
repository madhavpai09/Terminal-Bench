import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('dd528cb2cefc0db8b91a7ff0a2bc87305b976597')
        print(f"Checked out dd528cb2cefc0db8b91a7ff0a2bc87305b976597")
    except Exception as e:
        print(f"Failed to check out dd528cb2cefc0db8b91a7ff0a2bc87305b976597: {e}")

if __name__ == "__main__":
    main()

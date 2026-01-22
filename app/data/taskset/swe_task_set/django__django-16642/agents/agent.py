import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('fbe850106b2e4b85f838219cb9e1df95fba6c164')
        print(f"Checked out fbe850106b2e4b85f838219cb9e1df95fba6c164")
    except Exception as e:
        print(f"Failed to check out fbe850106b2e4b85f838219cb9e1df95fba6c164: {e}")

if __name__ == "__main__":
    main()

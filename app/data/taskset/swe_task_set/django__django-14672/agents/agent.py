import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('00ea883ef56fb5e092cbe4a6f7ff2e7470886ac4')
        print(f"Checked out 00ea883ef56fb5e092cbe4a6f7ff2e7470886ac4")
    except Exception as e:
        print(f"Failed to check out 00ea883ef56fb5e092cbe4a6f7ff2e7470886ac4: {e}")

if __name__ == "__main__":
    main()

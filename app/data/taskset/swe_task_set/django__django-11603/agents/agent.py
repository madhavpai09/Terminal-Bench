import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('f618e033acd37d59b536d6e6126e6c5be18037f6')
        print(f"Checked out f618e033acd37d59b536d6e6126e6c5be18037f6")
    except Exception as e:
        print(f"Failed to check out f618e033acd37d59b536d6e6126e6c5be18037f6: {e}")

if __name__ == "__main__":
    main()

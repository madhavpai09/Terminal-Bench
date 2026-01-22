import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('bb64b99b78a579cb2f6178011a4cf9366e634438')
        print(f"Checked out bb64b99b78a579cb2f6178011a4cf9366e634438")
    except Exception as e:
        print(f"Failed to check out bb64b99b78a579cb2f6178011a4cf9366e634438: {e}")

if __name__ == "__main__":
    main()

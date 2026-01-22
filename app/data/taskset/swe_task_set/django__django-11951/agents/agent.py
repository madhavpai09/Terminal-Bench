import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('312049091288dbba2299de8d07ea3e3311ed7238')
        print(f"Checked out 312049091288dbba2299de8d07ea3e3311ed7238")
    except Exception as e:
        print(f"Failed to check out 312049091288dbba2299de8d07ea3e3311ed7238: {e}")

if __name__ == "__main__":
    main()

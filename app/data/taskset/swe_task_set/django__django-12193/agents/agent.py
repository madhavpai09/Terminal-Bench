import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('3fb7c12158a2402f0f80824f6778112071235803')
        print(f"Checked out 3fb7c12158a2402f0f80824f6778112071235803")
    except Exception as e:
        print(f"Failed to check out 3fb7c12158a2402f0f80824f6778112071235803: {e}")

if __name__ == "__main__":
    main()

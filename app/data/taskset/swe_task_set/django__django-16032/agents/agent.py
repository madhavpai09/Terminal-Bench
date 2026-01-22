import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('0c3981eb5094419fe200eb46c71b5376a2266166')
        print(f"Checked out 0c3981eb5094419fe200eb46c71b5376a2266166")
    except Exception as e:
        print(f"Failed to check out 0c3981eb5094419fe200eb46c71b5376a2266166: {e}")

if __name__ == "__main__":
    main()

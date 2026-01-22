import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('02c356f2f3945b8075735d485c3cf48cad991011')
        print(f"Checked out 02c356f2f3945b8075735d485c3cf48cad991011")
    except Exception as e:
        print(f"Failed to check out 02c356f2f3945b8075735d485c3cf48cad991011: {e}")

if __name__ == "__main__":
    main()

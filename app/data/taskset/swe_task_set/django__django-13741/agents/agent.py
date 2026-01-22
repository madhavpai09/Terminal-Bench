import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('d746f28949c009251a8741ba03d156964050717f')
        print(f"Checked out d746f28949c009251a8741ba03d156964050717f")
    except Exception as e:
        print(f"Failed to check out d746f28949c009251a8741ba03d156964050717f: {e}")

if __name__ == "__main__":
    main()

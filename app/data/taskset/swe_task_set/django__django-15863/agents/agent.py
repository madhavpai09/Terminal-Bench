import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('37c5b8c07be104fd5288cd87f101e48cb7a40298')
        print(f"Checked out 37c5b8c07be104fd5288cd87f101e48cb7a40298")
    except Exception as e:
        print(f"Failed to check out 37c5b8c07be104fd5288cd87f101e48cb7a40298: {e}")

if __name__ == "__main__":
    main()

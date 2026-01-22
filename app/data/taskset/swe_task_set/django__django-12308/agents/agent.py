import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('2e0f04507b17362239ba49830d26fec504d46978')
        print(f"Checked out 2e0f04507b17362239ba49830d26fec504d46978")
    except Exception as e:
        print(f"Failed to check out 2e0f04507b17362239ba49830d26fec504d46978: {e}")

if __name__ == "__main__":
    main()

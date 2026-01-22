import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('a7038adbd02c916315b16939b835f021c2ee8880')
        print(f"Checked out a7038adbd02c916315b16939b835f021c2ee8880")
    except Exception as e:
        print(f"Failed to check out a7038adbd02c916315b16939b835f021c2ee8880: {e}")

if __name__ == "__main__":
    main()

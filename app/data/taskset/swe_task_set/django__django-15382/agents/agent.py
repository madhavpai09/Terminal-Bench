import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('770d3e6a4ce8e0a91a9e27156036c1985e74d4a3')
        print(f"Checked out 770d3e6a4ce8e0a91a9e27156036c1985e74d4a3")
    except Exception as e:
        print(f"Failed to check out 770d3e6a4ce8e0a91a9e27156036c1985e74d4a3: {e}")

if __name__ == "__main__":
    main()

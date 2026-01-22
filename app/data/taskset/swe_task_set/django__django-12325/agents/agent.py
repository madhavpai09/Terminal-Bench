import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('29c126bb349526b5f1cd78facbe9f25906f18563')
        print(f"Checked out 29c126bb349526b5f1cd78facbe9f25906f18563")
    except Exception as e:
        print(f"Failed to check out 29c126bb349526b5f1cd78facbe9f25906f18563: {e}")

if __name__ == "__main__":
    main()

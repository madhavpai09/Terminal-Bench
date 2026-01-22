import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('350123f38c2b6217c38d70bfbd924a9ba3df1289')
        print(f"Checked out 350123f38c2b6217c38d70bfbd924a9ba3df1289")
    except Exception as e:
        print(f"Failed to check out 350123f38c2b6217c38d70bfbd924a9ba3df1289: {e}")

if __name__ == "__main__":
    main()

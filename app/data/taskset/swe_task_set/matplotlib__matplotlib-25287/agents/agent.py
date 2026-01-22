import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/matplotlib/matplotlib"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('f8ffce6d44127d4ea7d6491262ab30046b03294b')
        print(f"Checked out f8ffce6d44127d4ea7d6491262ab30046b03294b")
    except Exception as e:
        print(f"Failed to check out f8ffce6d44127d4ea7d6491262ab30046b03294b: {e}")

if __name__ == "__main__":
    main()

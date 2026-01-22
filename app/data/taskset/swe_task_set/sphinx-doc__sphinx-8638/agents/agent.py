import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sphinx-doc/sphinx"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('4b452338f914d4f6b54704222d70ae8a746e3db5')
        print(f"Checked out 4b452338f914d4f6b54704222d70ae8a746e3db5")
    except Exception as e:
        print(f"Failed to check out 4b452338f914d4f6b54704222d70ae8a746e3db5: {e}")

if __name__ == "__main__":
    main()

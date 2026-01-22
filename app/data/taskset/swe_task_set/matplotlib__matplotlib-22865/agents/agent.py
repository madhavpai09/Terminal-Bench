import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/matplotlib/matplotlib"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('c6c7ec1978c22ae2c704555a873d0ec6e1e2eaa8')
        print(f"Checked out c6c7ec1978c22ae2c704555a873d0ec6e1e2eaa8")
    except Exception as e:
        print(f"Failed to check out c6c7ec1978c22ae2c704555a873d0ec6e1e2eaa8: {e}")

if __name__ == "__main__":
    main()

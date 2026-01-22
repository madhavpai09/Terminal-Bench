import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('c6753448b5c34f95e250105d76709fe4d349ca1f')
        print(f"Checked out c6753448b5c34f95e250105d76709fe4d349ca1f")
    except Exception as e:
        print(f"Failed to check out c6753448b5c34f95e250105d76709fe4d349ca1f: {e}")

if __name__ == "__main__":
    main()

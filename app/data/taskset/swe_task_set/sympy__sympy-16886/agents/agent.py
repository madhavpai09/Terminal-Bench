import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('c50643a49811e9fe2f4851adff4313ad46f7325e')
        print(f"Checked out c50643a49811e9fe2f4851adff4313ad46f7325e")
    except Exception as e:
        print(f"Failed to check out c50643a49811e9fe2f4851adff4313ad46f7325e: {e}")

if __name__ == "__main__":
    main()

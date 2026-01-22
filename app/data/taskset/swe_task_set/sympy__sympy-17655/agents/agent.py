import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('f5e965947af2410ded92cfad987aaf45262ea434')
        print(f"Checked out f5e965947af2410ded92cfad987aaf45262ea434")
    except Exception as e:
        print(f"Failed to check out f5e965947af2410ded92cfad987aaf45262ea434: {e}")

if __name__ == "__main__":
    main()

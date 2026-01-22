import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('10de1a18a0efac0b19b611e40c928250dda688bf')
        print(f"Checked out 10de1a18a0efac0b19b611e40c928250dda688bf")
    except Exception as e:
        print(f"Failed to check out 10de1a18a0efac0b19b611e40c928250dda688bf: {e}")

if __name__ == "__main__":
    main()

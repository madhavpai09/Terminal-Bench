import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('b4f1aa3540fe68d078d76e78ba59d022dd6df39f')
        print(f"Checked out b4f1aa3540fe68d078d76e78ba59d022dd6df39f")
    except Exception as e:
        print(f"Failed to check out b4f1aa3540fe68d078d76e78ba59d022dd6df39f: {e}")

if __name__ == "__main__":
    main()

import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('b506169ad727ee39cb3d60c8b3ff5e315d443d8e')
        print(f"Checked out b506169ad727ee39cb3d60c8b3ff5e315d443d8e")
    except Exception as e:
        print(f"Failed to check out b506169ad727ee39cb3d60c8b3ff5e315d443d8e: {e}")

if __name__ == "__main__":
    main()

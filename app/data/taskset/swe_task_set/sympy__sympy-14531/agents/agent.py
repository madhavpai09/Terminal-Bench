import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('205da797006360fc629110937e39a19c9561313e')
        print(f"Checked out 205da797006360fc629110937e39a19c9561313e")
    except Exception as e:
        print(f"Failed to check out 205da797006360fc629110937e39a19c9561313e: {e}")

if __name__ == "__main__":
    main()

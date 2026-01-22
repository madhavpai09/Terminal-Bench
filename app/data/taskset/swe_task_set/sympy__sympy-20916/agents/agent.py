import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('82298df6a51491bfaad0c6d1980e7e3ca808ae93')
        print(f"Checked out 82298df6a51491bfaad0c6d1980e7e3ca808ae93")
    except Exception as e:
        print(f"Failed to check out 82298df6a51491bfaad0c6d1980e7e3ca808ae93: {e}")

if __name__ == "__main__":
    main()

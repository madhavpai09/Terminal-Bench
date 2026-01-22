import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('b1cb676cf92dd1a48365b731979833375b188bf2')
        print(f"Checked out b1cb676cf92dd1a48365b731979833375b188bf2")
    except Exception as e:
        print(f"Failed to check out b1cb676cf92dd1a48365b731979833375b188bf2: {e}")

if __name__ == "__main__":
    main()

import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('d7c3045115693e887bcd03599b7ca4650ac5f2cb')
        print(f"Checked out d7c3045115693e887bcd03599b7ca4650ac5f2cb")
    except Exception as e:
        print(f"Failed to check out d7c3045115693e887bcd03599b7ca4650ac5f2cb: {e}")

if __name__ == "__main__":
    main()

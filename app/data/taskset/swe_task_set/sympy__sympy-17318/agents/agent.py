import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('d4e0231b08147337745dcf601e62de7eefe2fb2d')
        print(f"Checked out d4e0231b08147337745dcf601e62de7eefe2fb2d")
    except Exception as e:
        print(f"Failed to check out d4e0231b08147337745dcf601e62de7eefe2fb2d: {e}")

if __name__ == "__main__":
    main()

import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('1659712001810f5fc563a443949f8e3bb38af4bd')
        print(f"Checked out 1659712001810f5fc563a443949f8e3bb38af4bd")
    except Exception as e:
        print(f"Failed to check out 1659712001810f5fc563a443949f8e3bb38af4bd: {e}")

if __name__ == "__main__":
    main()

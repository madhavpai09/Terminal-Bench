import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('3dff1b98a78f28c953ae2140b69356b8391e399c')
        print(f"Checked out 3dff1b98a78f28c953ae2140b69356b8391e399c")
    except Exception as e:
        print(f"Failed to check out 3dff1b98a78f28c953ae2140b69356b8391e399c: {e}")

if __name__ == "__main__":
    main()

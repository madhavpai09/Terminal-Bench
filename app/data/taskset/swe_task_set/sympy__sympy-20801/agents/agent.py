import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('e11d3fed782146eebbffdc9ced0364b223b84b6c')
        print(f"Checked out e11d3fed782146eebbffdc9ced0364b223b84b6c")
    except Exception as e:
        print(f"Failed to check out e11d3fed782146eebbffdc9ced0364b223b84b6c: {e}")

if __name__ == "__main__":
    main()

import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('768da1c6f6ec907524b8ebbf6bf818c92b56101b')
        print(f"Checked out 768da1c6f6ec907524b8ebbf6bf818c92b56101b")
    except Exception as e:
        print(f"Failed to check out 768da1c6f6ec907524b8ebbf6bf818c92b56101b: {e}")

if __name__ == "__main__":
    main()

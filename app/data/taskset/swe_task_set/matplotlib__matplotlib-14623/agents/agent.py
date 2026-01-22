import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/matplotlib/matplotlib"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('d65c9ca20ddf81ef91199e6d819f9d3506ef477c')
        print(f"Checked out d65c9ca20ddf81ef91199e6d819f9d3506ef477c")
    except Exception as e:
        print(f"Failed to check out d65c9ca20ddf81ef91199e6d819f9d3506ef477c: {e}")

if __name__ == "__main__":
    main()

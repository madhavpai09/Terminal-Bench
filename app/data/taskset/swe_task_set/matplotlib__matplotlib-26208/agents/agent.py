import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/matplotlib/matplotlib"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('f0f133943d3e4f1e2e665291fe1c8f658a84cc09')
        print(f"Checked out f0f133943d3e4f1e2e665291fe1c8f658a84cc09")
    except Exception as e:
        print(f"Failed to check out f0f133943d3e4f1e2e665291fe1c8f658a84cc09: {e}")

if __name__ == "__main__":
    main()

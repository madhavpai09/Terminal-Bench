import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sphinx-doc/sphinx"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('27ac10de04697e2372d31db5548e56a7c6d9265d')
        print(f"Checked out 27ac10de04697e2372d31db5548e56a7c6d9265d")
    except Exception as e:
        print(f"Failed to check out 27ac10de04697e2372d31db5548e56a7c6d9265d: {e}")

if __name__ == "__main__":
    main()

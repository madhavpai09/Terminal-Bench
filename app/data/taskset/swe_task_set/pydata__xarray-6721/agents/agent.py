import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/pydata/xarray"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('cc183652bf6e1273e985e1c4b3cba79c896c1193')
        print(f"Checked out cc183652bf6e1273e985e1c4b3cba79c896c1193")
    except Exception as e:
        print(f"Failed to check out cc183652bf6e1273e985e1c4b3cba79c896c1193: {e}")

if __name__ == "__main__":
    main()

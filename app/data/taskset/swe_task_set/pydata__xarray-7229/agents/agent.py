import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/pydata/xarray"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('3aa75c8d00a4a2d4acf10d80f76b937cadb666b7')
        print(f"Checked out 3aa75c8d00a4a2d4acf10d80f76b937cadb666b7")
    except Exception as e:
        print(f"Failed to check out 3aa75c8d00a4a2d4acf10d80f76b937cadb666b7: {e}")

if __name__ == "__main__":
    main()

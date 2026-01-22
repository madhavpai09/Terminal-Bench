import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/pydata/xarray"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('6bb2b855498b5c68d7cca8cceb710365d58e6048')
        print(f"Checked out 6bb2b855498b5c68d7cca8cceb710365d58e6048")
    except Exception as e:
        print(f"Failed to check out 6bb2b855498b5c68d7cca8cceb710365d58e6048: {e}")

if __name__ == "__main__":
    main()

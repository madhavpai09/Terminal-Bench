import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/matplotlib/matplotlib"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('2aee6ccd7c7e1f8d282c1e7579f4ee546b838542')
        print(f"Checked out 2aee6ccd7c7e1f8d282c1e7579f4ee546b838542")
    except Exception as e:
        print(f"Failed to check out 2aee6ccd7c7e1f8d282c1e7579f4ee546b838542: {e}")

if __name__ == "__main__":
    main()

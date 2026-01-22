import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/pydata/xarray"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('c4e40d991c28be51de9ac560ce895ac7f9b14924')
        print(f"Checked out c4e40d991c28be51de9ac560ce895ac7f9b14924")
    except Exception as e:
        print(f"Failed to check out c4e40d991c28be51de9ac560ce895ac7f9b14924: {e}")

if __name__ == "__main__":
    main()

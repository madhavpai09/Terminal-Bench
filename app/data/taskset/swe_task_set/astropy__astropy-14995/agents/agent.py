import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/astropy/astropy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('b16c7d12ccbc7b2d20364b89fb44285bcbfede54')
        print(f"Checked out b16c7d12ccbc7b2d20364b89fb44285bcbfede54")
    except Exception as e:
        print(f"Failed to check out b16c7d12ccbc7b2d20364b89fb44285bcbfede54: {e}")

if __name__ == "__main__":
    main()

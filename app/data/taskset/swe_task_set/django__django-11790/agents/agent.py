import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('b1d6b35e146aea83b171c1b921178bbaae2795ed')
        print(f"Checked out b1d6b35e146aea83b171c1b921178bbaae2795ed")
    except Exception as e:
        print(f"Failed to check out b1d6b35e146aea83b171c1b921178bbaae2795ed: {e}")

if __name__ == "__main__":
    main()

import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/matplotlib/matplotlib"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('a3e2897bfaf9eaac1d6649da535c4e721c89fa69')
        print(f"Checked out a3e2897bfaf9eaac1d6649da535c4e721c89fa69")
    except Exception as e:
        print(f"Failed to check out a3e2897bfaf9eaac1d6649da535c4e721c89fa69: {e}")

if __name__ == "__main__":
    main()

import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('e39e727ded673e74016b5d3658d23cbe20234d11')
        print(f"Checked out e39e727ded673e74016b5d3658d23cbe20234d11")
    except Exception as e:
        print(f"Failed to check out e39e727ded673e74016b5d3658d23cbe20234d11: {e}")

if __name__ == "__main__":
    main()

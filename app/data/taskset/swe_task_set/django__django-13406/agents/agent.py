import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('84609b3205905097d7d3038d32e6101f012c0619')
        print(f"Checked out 84609b3205905097d7d3038d32e6101f012c0619")
    except Exception as e:
        print(f"Failed to check out 84609b3205905097d7d3038d32e6101f012c0619: {e}")

if __name__ == "__main__":
    main()

import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('fc2b1cc926e34041953738e58fa6ad3053059b22')
        print(f"Checked out fc2b1cc926e34041953738e58fa6ad3053059b22")
    except Exception as e:
        print(f"Failed to check out fc2b1cc926e34041953738e58fa6ad3053059b22: {e}")

if __name__ == "__main__":
    main()

import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('d3d173425fc0a1107836da5b4567f1c88253191b')
        print(f"Checked out d3d173425fc0a1107836da5b4567f1c88253191b")
    except Exception as e:
        print(f"Failed to check out d3d173425fc0a1107836da5b4567f1c88253191b: {e}")

if __name__ == "__main__":
    main()

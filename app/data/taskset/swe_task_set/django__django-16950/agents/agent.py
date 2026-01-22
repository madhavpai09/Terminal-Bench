import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('f64fd47a7627ed6ffe2df2a32ded6ee528a784eb')
        print(f"Checked out f64fd47a7627ed6ffe2df2a32ded6ee528a784eb")
    except Exception as e:
        print(f"Failed to check out f64fd47a7627ed6ffe2df2a32ded6ee528a784eb: {e}")

if __name__ == "__main__":
    main()

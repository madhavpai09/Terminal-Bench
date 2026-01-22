import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('1250483ebf73f7a82ff820b94092c63ce4238264')
        print(f"Checked out 1250483ebf73f7a82ff820b94092c63ce4238264")
    except Exception as e:
        print(f"Failed to check out 1250483ebf73f7a82ff820b94092c63ce4238264: {e}")

if __name__ == "__main__":
    main()

import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/matplotlib/matplotlib"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('6786f437df54ca7780a047203cbcfaa1db8dc542')
        print(f"Checked out 6786f437df54ca7780a047203cbcfaa1db8dc542")
    except Exception as e:
        print(f"Failed to check out 6786f437df54ca7780a047203cbcfaa1db8dc542: {e}")

if __name__ == "__main__":
    main()

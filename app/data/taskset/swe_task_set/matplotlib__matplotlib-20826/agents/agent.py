import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/matplotlib/matplotlib"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('a0d2e399729d36499a1924e5ca5bc067c8396810')
        print(f"Checked out a0d2e399729d36499a1924e5ca5bc067c8396810")
    except Exception as e:
        print(f"Failed to check out a0d2e399729d36499a1924e5ca5bc067c8396810: {e}")

if __name__ == "__main__":
    main()

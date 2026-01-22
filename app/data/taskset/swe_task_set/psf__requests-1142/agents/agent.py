import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/psf/requests"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('22623bd8c265b78b161542663ee980738441c307')
        print(f"Checked out 22623bd8c265b78b161542663ee980738441c307")
    except Exception as e:
        print(f"Failed to check out 22623bd8c265b78b161542663ee980738441c307: {e}")

if __name__ == "__main__":
    main()

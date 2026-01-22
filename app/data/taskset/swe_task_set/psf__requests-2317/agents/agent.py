import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/psf/requests"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('091991be0da19de9108dbe5e3752917fea3d7fdc')
        print(f"Checked out 091991be0da19de9108dbe5e3752917fea3d7fdc")
    except Exception as e:
        print(f"Failed to check out 091991be0da19de9108dbe5e3752917fea3d7fdc: {e}")

if __name__ == "__main__":
    main()

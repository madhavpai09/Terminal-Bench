import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/astropy/astropy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('b750a0e6ee76fb6b8a099a4d16ec51977be46bf6')
        print(f"Checked out b750a0e6ee76fb6b8a099a4d16ec51977be46bf6")
    except Exception as e:
        print(f"Failed to check out b750a0e6ee76fb6b8a099a4d16ec51977be46bf6: {e}")

if __name__ == "__main__":
    main()

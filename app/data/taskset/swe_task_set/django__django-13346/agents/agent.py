import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('9c92924cd5d164701e2514e1c2d6574126bd7cc2')
        print(f"Checked out 9c92924cd5d164701e2514e1c2d6574126bd7cc2")
    except Exception as e:
        print(f"Failed to check out 9c92924cd5d164701e2514e1c2d6574126bd7cc2: {e}")

if __name__ == "__main__":
    main()

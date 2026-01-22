import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('e0442a628eb480eac6a7888aed5a86f83499e299')
        print(f"Checked out e0442a628eb480eac6a7888aed5a86f83499e299")
    except Exception as e:
        print(f"Failed to check out e0442a628eb480eac6a7888aed5a86f83499e299: {e}")

if __name__ == "__main__":
    main()

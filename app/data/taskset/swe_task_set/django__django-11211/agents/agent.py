import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('ba726067604ce5a8ca3919edf653496722b433ab')
        print(f"Checked out ba726067604ce5a8ca3919edf653496722b433ab")
    except Exception as e:
        print(f"Failed to check out ba726067604ce5a8ca3919edf653496722b433ab: {e}")

if __name__ == "__main__":
    main()

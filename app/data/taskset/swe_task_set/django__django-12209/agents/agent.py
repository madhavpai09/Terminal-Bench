import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('5a68f024987e6d16c2626a31bf653a2edddea579')
        print(f"Checked out 5a68f024987e6d16c2626a31bf653a2edddea579")
    except Exception as e:
        print(f"Failed to check out 5a68f024987e6d16c2626a31bf653a2edddea579: {e}")

if __name__ == "__main__":
    main()

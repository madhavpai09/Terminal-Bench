import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sphinx-doc/sphinx"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('9988d5ce267bf0df4791770b469431b1fb00dcdd')
        print(f"Checked out 9988d5ce267bf0df4791770b469431b1fb00dcdd")
    except Exception as e:
        print(f"Failed to check out 9988d5ce267bf0df4791770b469431b1fb00dcdd: {e}")

if __name__ == "__main__":
    main()

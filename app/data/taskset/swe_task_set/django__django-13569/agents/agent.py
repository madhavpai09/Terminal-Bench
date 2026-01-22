import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('257f8495d6c93e30ab0f52af4c488d7344bcf112')
        print(f"Checked out 257f8495d6c93e30ab0f52af4c488d7344bcf112")
    except Exception as e:
        print(f"Failed to check out 257f8495d6c93e30ab0f52af4c488d7344bcf112: {e}")

if __name__ == "__main__":
    main()

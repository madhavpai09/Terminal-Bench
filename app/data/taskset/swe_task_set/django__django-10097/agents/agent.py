import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('b9cf764be62e77b4777b3a75ec256f6209a57671')
        print(f"Checked out b9cf764be62e77b4777b3a75ec256f6209a57671")
    except Exception as e:
        print(f"Failed to check out b9cf764be62e77b4777b3a75ec256f6209a57671: {e}")

if __name__ == "__main__":
    main()

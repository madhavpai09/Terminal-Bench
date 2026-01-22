import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('98ad327864aed8df245fd19ea9d2743279e11643')
        print(f"Checked out 98ad327864aed8df245fd19ea9d2743279e11643")
    except Exception as e:
        print(f"Failed to check out 98ad327864aed8df245fd19ea9d2743279e11643: {e}")

if __name__ == "__main__":
    main()

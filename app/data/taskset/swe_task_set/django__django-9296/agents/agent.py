import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('84322a29ce9b0940335f8ab3d60e55192bef1e50')
        print(f"Checked out 84322a29ce9b0940335f8ab3d60e55192bef1e50")
    except Exception as e:
        print(f"Failed to check out 84322a29ce9b0940335f8ab3d60e55192bef1e50: {e}")

if __name__ == "__main__":
    main()

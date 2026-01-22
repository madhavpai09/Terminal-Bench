import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('f4e93919e4608cfc50849a1f764fd856e0917401')
        print(f"Checked out f4e93919e4608cfc50849a1f764fd856e0917401")
    except Exception as e:
        print(f"Failed to check out f4e93919e4608cfc50849a1f764fd856e0917401: {e}")

if __name__ == "__main__":
    main()

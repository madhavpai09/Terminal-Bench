import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('361bb8f786f112ee275be136795c0b1ecefff928')
        print(f"Checked out 361bb8f786f112ee275be136795c0b1ecefff928")
    except Exception as e:
        print(f"Failed to check out 361bb8f786f112ee275be136795c0b1ecefff928: {e}")

if __name__ == "__main__":
    main()

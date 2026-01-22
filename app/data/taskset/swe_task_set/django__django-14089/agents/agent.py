import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('d01709aae21de9cd2565b9c52f32732ea28a2d98')
        print(f"Checked out d01709aae21de9cd2565b9c52f32732ea28a2d98")
    except Exception as e:
        print(f"Failed to check out d01709aae21de9cd2565b9c52f32732ea28a2d98: {e}")

if __name__ == "__main__":
    main()

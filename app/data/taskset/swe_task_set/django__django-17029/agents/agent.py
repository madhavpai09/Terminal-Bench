import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('953f29f700a60fc09b08b2c2270c12c447490c6a')
        print(f"Checked out 953f29f700a60fc09b08b2c2270c12c447490c6a")
    except Exception as e:
        print(f"Failed to check out 953f29f700a60fc09b08b2c2270c12c447490c6a: {e}")

if __name__ == "__main__":
    main()

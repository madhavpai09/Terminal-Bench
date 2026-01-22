import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('27c09043da52ca1f02605bf28600bfd5ace95ae4')
        print(f"Checked out 27c09043da52ca1f02605bf28600bfd5ace95ae4")
    except Exception as e:
        print(f"Failed to check out 27c09043da52ca1f02605bf28600bfd5ace95ae4: {e}")

if __name__ == "__main__":
    main()

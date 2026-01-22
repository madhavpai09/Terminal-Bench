import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('6c86495bcee22eac19d7fb040b2988b830707cbd')
        print(f"Checked out 6c86495bcee22eac19d7fb040b2988b830707cbd")
    except Exception as e:
        print(f"Failed to check out 6c86495bcee22eac19d7fb040b2988b830707cbd: {e}")

if __name__ == "__main__":
    main()

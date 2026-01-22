import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/astropy/astropy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('0df94ff7097961e92fd7812036a24b145bc13ca8')
        print(f"Checked out 0df94ff7097961e92fd7812036a24b145bc13ca8")
    except Exception as e:
        print(f"Failed to check out 0df94ff7097961e92fd7812036a24b145bc13ca8: {e}")

if __name__ == "__main__":
    main()

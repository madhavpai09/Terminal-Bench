import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('453967477e3ddae704cd739eac2449c0e13d464c')
        print(f"Checked out 453967477e3ddae704cd739eac2449c0e13d464c")
    except Exception as e:
        print(f"Failed to check out 453967477e3ddae704cd739eac2449c0e13d464c: {e}")

if __name__ == "__main__":
    main()

import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('5e17a90c19f7eecfa10c1ab872648ae7e2131323')
        print(f"Checked out 5e17a90c19f7eecfa10c1ab872648ae7e2131323")
    except Exception as e:
        print(f"Failed to check out 5e17a90c19f7eecfa10c1ab872648ae7e2131323: {e}")

if __name__ == "__main__":
    main()

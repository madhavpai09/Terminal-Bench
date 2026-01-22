import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('c807dfe7569692cad24f02a08477b70c1679a4dd')
        print(f"Checked out c807dfe7569692cad24f02a08477b70c1679a4dd")
    except Exception as e:
        print(f"Failed to check out c807dfe7569692cad24f02a08477b70c1679a4dd: {e}")

if __name__ == "__main__":
    main()

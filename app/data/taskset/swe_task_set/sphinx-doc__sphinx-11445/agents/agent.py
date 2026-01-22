import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sphinx-doc/sphinx"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('71db08c05197545944949d5aa76cd340e7143627')
        print(f"Checked out 71db08c05197545944949d5aa76cd340e7143627")
    except Exception as e:
        print(f"Failed to check out 71db08c05197545944949d5aa76cd340e7143627: {e}")

if __name__ == "__main__":
    main()

import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/astropy/astropy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('cdb66059a2feb44ee49021874605ba90801f9986')
        print(f"Checked out cdb66059a2feb44ee49021874605ba90801f9986")
    except Exception as e:
        print(f"Failed to check out cdb66059a2feb44ee49021874605ba90801f9986: {e}")

if __name__ == "__main__":
    main()

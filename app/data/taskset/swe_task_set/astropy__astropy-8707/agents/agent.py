import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/astropy/astropy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('a85a0747c54bac75e9c3b2fe436b105ea029d6cf')
        print(f"Checked out a85a0747c54bac75e9c3b2fe436b105ea029d6cf")
    except Exception as e:
        print(f"Failed to check out a85a0747c54bac75e9c3b2fe436b105ea029d6cf: {e}")

if __name__ == "__main__":
    main()

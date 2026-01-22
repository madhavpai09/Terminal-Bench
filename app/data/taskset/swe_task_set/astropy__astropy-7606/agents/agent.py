import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/astropy/astropy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('3cedd79e6c121910220f8e6df77c54a0b344ea94')
        print(f"Checked out 3cedd79e6c121910220f8e6df77c54a0b344ea94")
    except Exception as e:
        print(f"Failed to check out 3cedd79e6c121910220f8e6df77c54a0b344ea94: {e}")

if __name__ == "__main__":
    main()

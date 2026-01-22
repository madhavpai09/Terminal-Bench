import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/matplotlib/matplotlib"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('430fb1db88843300fb4baae3edc499bbfe073b0c')
        print(f"Checked out 430fb1db88843300fb4baae3edc499bbfe073b0c")
    except Exception as e:
        print(f"Failed to check out 430fb1db88843300fb4baae3edc499bbfe073b0c: {e}")

if __name__ == "__main__":
    main()

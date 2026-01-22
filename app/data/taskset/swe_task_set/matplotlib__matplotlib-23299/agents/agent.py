import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/matplotlib/matplotlib"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('3eadeacc06c9f2ddcdac6ae39819faa9fbee9e39')
        print(f"Checked out 3eadeacc06c9f2ddcdac6ae39819faa9fbee9e39")
    except Exception as e:
        print(f"Failed to check out 3eadeacc06c9f2ddcdac6ae39819faa9fbee9e39: {e}")

if __name__ == "__main__":
    main()

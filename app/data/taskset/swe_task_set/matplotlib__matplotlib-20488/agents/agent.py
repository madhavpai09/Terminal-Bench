import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/matplotlib/matplotlib"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('b7ce415c15eb39b026a097a2865da73fbcf15c9c')
        print(f"Checked out b7ce415c15eb39b026a097a2865da73fbcf15c9c")
    except Exception as e:
        print(f"Failed to check out b7ce415c15eb39b026a097a2865da73fbcf15c9c: {e}")

if __name__ == "__main__":
    main()

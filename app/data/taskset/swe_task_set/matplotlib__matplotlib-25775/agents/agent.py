import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/matplotlib/matplotlib"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('26224d96066b5c60882296c551f54ca7732c0af0')
        print(f"Checked out 26224d96066b5c60882296c551f54ca7732c0af0")
    except Exception as e:
        print(f"Failed to check out 26224d96066b5c60882296c551f54ca7732c0af0: {e}")

if __name__ == "__main__":
    main()

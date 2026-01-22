import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/pytest-dev/pytest"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('8aba863a634f40560e25055d179220f0eefabe9a')
        print(f"Checked out 8aba863a634f40560e25055d179220f0eefabe9a")
    except Exception as e:
        print(f"Failed to check out 8aba863a634f40560e25055d179220f0eefabe9a: {e}")

if __name__ == "__main__":
    main()

import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/matplotlib/matplotlib"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('a9ba9d5d3fe9d5ac15fbdb06127f97d381148dd0')
        print(f"Checked out a9ba9d5d3fe9d5ac15fbdb06127f97d381148dd0")
    except Exception as e:
        print(f"Failed to check out a9ba9d5d3fe9d5ac15fbdb06127f97d381148dd0: {e}")

if __name__ == "__main__":
    main()

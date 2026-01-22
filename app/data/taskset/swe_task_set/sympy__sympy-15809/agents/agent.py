import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('28d913d3cead6c5646307ffa6540b21d65059dfd')
        print(f"Checked out 28d913d3cead6c5646307ffa6540b21d65059dfd")
    except Exception as e:
        print(f"Failed to check out 28d913d3cead6c5646307ffa6540b21d65059dfd: {e}")

if __name__ == "__main__":
    main()

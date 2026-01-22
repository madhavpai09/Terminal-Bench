import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/matplotlib/matplotlib"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('6091437be9776139d3672cde28a19cbe6c09dcd5')
        print(f"Checked out 6091437be9776139d3672cde28a19cbe6c09dcd5")
    except Exception as e:
        print(f"Failed to check out 6091437be9776139d3672cde28a19cbe6c09dcd5: {e}")

if __name__ == "__main__":
    main()

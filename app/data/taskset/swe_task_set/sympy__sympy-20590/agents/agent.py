import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('cffd4e0f86fefd4802349a9f9b19ed70934ea354')
        print(f"Checked out cffd4e0f86fefd4802349a9f9b19ed70934ea354")
    except Exception as e:
        print(f"Failed to check out cffd4e0f86fefd4802349a9f9b19ed70934ea354: {e}")

if __name__ == "__main__":
    main()

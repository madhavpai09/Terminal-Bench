import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/mwaskom/seaborn"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('54cab15bdacfaa05a88fbc5502a5b322d99f148e')
        print(f"Checked out 54cab15bdacfaa05a88fbc5502a5b322d99f148e")
    except Exception as e:
        print(f"Failed to check out 54cab15bdacfaa05a88fbc5502a5b322d99f148e: {e}")

if __name__ == "__main__":
    main()

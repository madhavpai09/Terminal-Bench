import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/scikit-learn/scikit-learn"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('f9a1cf072da9d7375d6c2163f68a6038b13b310f')
        print(f"Checked out f9a1cf072da9d7375d6c2163f68a6038b13b310f")
    except Exception as e:
        print(f"Failed to check out f9a1cf072da9d7375d6c2163f68a6038b13b310f: {e}")

if __name__ == "__main__":
    main()

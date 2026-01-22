import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/scikit-learn/scikit-learn"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('a5743ed36fbd3fbc8e351bdab16561fbfca7dfa1')
        print(f"Checked out a5743ed36fbd3fbc8e351bdab16561fbfca7dfa1")
    except Exception as e:
        print(f"Failed to check out a5743ed36fbd3fbc8e351bdab16561fbfca7dfa1: {e}")

if __name__ == "__main__":
    main()

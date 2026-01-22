import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/scikit-learn/scikit-learn"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('a061ada48efccf0845acae17009553e01764452b')
        print(f"Checked out a061ada48efccf0845acae17009553e01764452b")
    except Exception as e:
        print(f"Failed to check out a061ada48efccf0845acae17009553e01764452b: {e}")

if __name__ == "__main__":
    main()

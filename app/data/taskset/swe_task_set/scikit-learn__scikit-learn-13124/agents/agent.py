import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/scikit-learn/scikit-learn"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('9f0b959a8c9195d1b6e203f08b698e052b426ca9')
        print(f"Checked out 9f0b959a8c9195d1b6e203f08b698e052b426ca9")
    except Exception as e:
        print(f"Failed to check out 9f0b959a8c9195d1b6e203f08b698e052b426ca9: {e}")

if __name__ == "__main__":
    main()

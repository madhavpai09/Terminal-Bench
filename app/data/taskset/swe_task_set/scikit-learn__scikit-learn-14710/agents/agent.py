import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/scikit-learn/scikit-learn"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('4b6273b87442a4437d8b3873ea3022ae163f4fdf')
        print(f"Checked out 4b6273b87442a4437d8b3873ea3022ae163f4fdf")
    except Exception as e:
        print(f"Failed to check out 4b6273b87442a4437d8b3873ea3022ae163f4fdf: {e}")

if __name__ == "__main__":
    main()

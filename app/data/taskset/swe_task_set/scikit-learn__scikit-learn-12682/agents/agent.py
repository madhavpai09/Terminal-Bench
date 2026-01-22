import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/scikit-learn/scikit-learn"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('d360ffa7c5896a91ae498b3fb9cf464464ce8f34')
        print(f"Checked out d360ffa7c5896a91ae498b3fb9cf464464ce8f34")
    except Exception as e:
        print(f"Failed to check out d360ffa7c5896a91ae498b3fb9cf464464ce8f34: {e}")

if __name__ == "__main__":
    main()

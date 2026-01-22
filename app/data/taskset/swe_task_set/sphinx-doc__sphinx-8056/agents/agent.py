import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sphinx-doc/sphinx"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('e188d56ed1248dead58f3f8018c0e9a3f99193f7')
        print(f"Checked out e188d56ed1248dead58f3f8018c0e9a3f99193f7")
    except Exception as e:
        print(f"Failed to check out e188d56ed1248dead58f3f8018c0e9a3f99193f7: {e}")

if __name__ == "__main__":
    main()

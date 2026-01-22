import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sphinx-doc/sphinx"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('07983a5a8704ad91ae855218ecbda1c8598200ca')
        print(f"Checked out 07983a5a8704ad91ae855218ecbda1c8598200ca")
    except Exception as e:
        print(f"Failed to check out 07983a5a8704ad91ae855218ecbda1c8598200ca: {e}")

if __name__ == "__main__":
    main()

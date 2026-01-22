import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sphinx-doc/sphinx"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('21698c14461d27933864d73e6fba568a154e83b3')
        print(f"Checked out 21698c14461d27933864d73e6fba568a154e83b3")
    except Exception as e:
        print(f"Failed to check out 21698c14461d27933864d73e6fba568a154e83b3: {e}")

if __name__ == "__main__":
    main()

import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sphinx-doc/sphinx"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('ac2b7599d212af7d04649959ce6926c63c3133fa')
        print(f"Checked out ac2b7599d212af7d04649959ce6926c63c3133fa")
    except Exception as e:
        print(f"Failed to check out ac2b7599d212af7d04649959ce6926c63c3133fa: {e}")

if __name__ == "__main__":
    main()

import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sphinx-doc/sphinx"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('aca3f825f2e4a8817190f3c885a242a285aa0dba')
        print(f"Checked out aca3f825f2e4a8817190f3c885a242a285aa0dba")
    except Exception as e:
        print(f"Failed to check out aca3f825f2e4a8817190f3c885a242a285aa0dba: {e}")

if __name__ == "__main__":
    main()

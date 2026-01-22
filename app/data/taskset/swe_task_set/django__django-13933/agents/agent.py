import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('42e8cf47c7ee2db238bf91197ea398126c546741')
        print(f"Checked out 42e8cf47c7ee2db238bf91197ea398126c546741")
    except Exception as e:
        print(f"Failed to check out 42e8cf47c7ee2db238bf91197ea398126c546741: {e}")

if __name__ == "__main__":
    main()

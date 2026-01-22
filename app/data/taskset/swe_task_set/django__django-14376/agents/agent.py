import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('d06c5b358149c02a62da8a5469264d05f29ac659')
        print(f"Checked out d06c5b358149c02a62da8a5469264d05f29ac659")
    except Exception as e:
        print(f"Failed to check out d06c5b358149c02a62da8a5469264d05f29ac659: {e}")

if __name__ == "__main__":
    main()

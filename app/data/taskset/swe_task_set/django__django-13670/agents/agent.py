import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('c448e614c60cc97c6194c62052363f4f501e0953')
        print(f"Checked out c448e614c60cc97c6194c62052363f4f501e0953")
    except Exception as e:
        print(f"Failed to check out c448e614c60cc97c6194c62052363f4f501e0953: {e}")

if __name__ == "__main__":
    main()

import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('89fc144dedc737a79929231438f035b1d4a993c9')
        print(f"Checked out 89fc144dedc737a79929231438f035b1d4a993c9")
    except Exception as e:
        print(f"Failed to check out 89fc144dedc737a79929231438f035b1d4a993c9: {e}")

if __name__ == "__main__":
    main()

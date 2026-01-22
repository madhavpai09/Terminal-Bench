import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/pydata/xarray"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('7cc6cc991e586a6158bb656b8001234ccda25407')
        print(f"Checked out 7cc6cc991e586a6158bb656b8001234ccda25407")
    except Exception as e:
        print(f"Failed to check out 7cc6cc991e586a6158bb656b8001234ccda25407: {e}")

if __name__ == "__main__":
    main()

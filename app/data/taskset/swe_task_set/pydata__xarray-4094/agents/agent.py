import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/pydata/xarray"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('a64cf2d5476e7bbda099b34c40b7be1880dbd39a')
        print(f"Checked out a64cf2d5476e7bbda099b34c40b7be1880dbd39a")
    except Exception as e:
        print(f"Failed to check out a64cf2d5476e7bbda099b34c40b7be1880dbd39a: {e}")

if __name__ == "__main__":
    main()

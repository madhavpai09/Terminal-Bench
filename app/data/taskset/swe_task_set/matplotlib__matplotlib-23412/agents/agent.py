import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/matplotlib/matplotlib"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('f06c2c3abdaf4b90285ce5ca7fedbb8ace715911')
        print(f"Checked out f06c2c3abdaf4b90285ce5ca7fedbb8ace715911")
    except Exception as e:
        print(f"Failed to check out f06c2c3abdaf4b90285ce5ca7fedbb8ace715911: {e}")

if __name__ == "__main__":
    main()

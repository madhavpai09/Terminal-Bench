import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/astropy/astropy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('1a4462d72eb03f30dc83a879b1dd57aac8b2c18b')
        print(f"Checked out 1a4462d72eb03f30dc83a879b1dd57aac8b2c18b")
    except Exception as e:
        print(f"Failed to check out 1a4462d72eb03f30dc83a879b1dd57aac8b2c18b: {e}")

if __name__ == "__main__":
    main()

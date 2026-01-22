import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sphinx-doc/sphinx"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('567ff22716ac258b9edd2c1711d766b440ac0b11')
        print(f"Checked out 567ff22716ac258b9edd2c1711d766b440ac0b11")
    except Exception as e:
        print(f"Failed to check out 567ff22716ac258b9edd2c1711d766b440ac0b11: {e}")

if __name__ == "__main__":
    main()

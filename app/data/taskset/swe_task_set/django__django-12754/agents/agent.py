import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('18759b2209ff556aed7f20d83cbf23e3d234e41c')
        print(f"Checked out 18759b2209ff556aed7f20d83cbf23e3d234e41c")
    except Exception as e:
        print(f"Failed to check out 18759b2209ff556aed7f20d83cbf23e3d234e41c: {e}")

if __name__ == "__main__":
    main()

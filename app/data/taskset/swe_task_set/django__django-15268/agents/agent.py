import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('0ab58c120939093fea90822f376e1866fc714d1f')
        print(f"Checked out 0ab58c120939093fea90822f376e1866fc714d1f")
    except Exception as e:
        print(f"Failed to check out 0ab58c120939093fea90822f376e1866fc714d1f: {e}")

if __name__ == "__main__":
    main()

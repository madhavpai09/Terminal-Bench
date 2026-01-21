import git
import os
import sys
base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
clone_dir = os.path.join(base_path, "environment", "src")
def git_clone(repo_url):
    git.Repo.clone_from(repo_url, clone_dir)


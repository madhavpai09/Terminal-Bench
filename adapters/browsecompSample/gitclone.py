import gitpython 

local_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src"

def git_clone(repo_url):
    gitpython.Git.clone_from(repo_url, local_path)
    return gitpython.Repo(local_path)
    
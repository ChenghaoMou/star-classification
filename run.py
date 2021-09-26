import os
from pathlib import Path

from tqdm import tqdm
from github import Github
from datetime import datetime

if __name__ == '__main__':

    g = Github(os.environ.get('GITHUB_TOKEN', None))

    if not os.path.isdir("Repos"):
        os.mkdir("Repos")

    content = Path("output.md").read_text()

    for repo in tqdm(g.get_user().get_starred()):
        
        with open(os.path.join("Repos", datetime.now().strftime("%Y%m%d%H%M%S") + ".md"), "w") as f:
            f.write(content.format(
                name=repo.name,
                url=repo.url,
                date=datetime.now().strftime("%m-%d-%Y"),
                time=datetime.now().strftime("%H:%M:%S"),
                tags="'" + "','".join(repo.get_topics()) + "'",
            ))

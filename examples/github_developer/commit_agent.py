import os
import git
from swarm import Agent

class CommitAgent(Agent):
    def __init__(self, repo_path):
        super().__init__(name="CommitAgent", instructions="Replace logo.png with the new image, commit, and push changes.")
        self.repo_path = repo_path
        self.repo = git.Repo(repo_path)
    
    def handle_task(self, task):
        image_path = task["image_path"]
        # Replace logo.png with the new image
        os.replace(image_path, os.path.join(self.repo_path, "logo.png"))
        # Add the file to the staging area
        self.repo.git.add('logo.png')
        # Commit the changes
        self.repo.git.commit('-m', 'Update logo.png with new image')
        # Push the changes to the remote repository
        origin = self.repo.remote(name='origin')
        origin.push()
        return {"status": "success"}
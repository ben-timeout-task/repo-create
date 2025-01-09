# repo-create
Creates a repo based on the name of the application - TimeOut Task

This project makes use of the PyGitHub library (pip install PyGitHub).
You GitHub auth token will need to be entered into config.py


Assumptions:
  -GitHub Organizations was not used for this as I don't have access to it, but it is assumed that the user would need to authenticate according to the org's process, or could be     
  prompted to enter it before the repo name.
  -The user will have the ability to generate their own access tokens with permissions to create and query repos, as well as set branch protection rules.
  -The team called 'Engineers' already exists within the organisation in which the repo is being created.
  -The 'main' branch is to be protected
  

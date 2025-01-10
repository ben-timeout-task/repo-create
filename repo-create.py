from github import Github
from github import Auth
import config

def verify_lang(language):
    current_languages = ['python']
    return language.lower() in current_languages

#returning true/false for consistency (functions returning bools)
def check_repo_exists(repo_name):
    try:
        repo =  org.get_repo(repo_name)
        return False
    except Exception:
        return True

#auth setup
auth = Auth.Token(config.AUTH_TOKEN)
g = Github(auth=auth)
user = g.get_user()
org = g.get_organization(config.ORG)
team = org.get_team_by_slug('Engineers')

#enter repo name and language
repo_name = input('Enter repo name: ')
language = input('Enter programming language: ')

#verify language
if verify_lang(language):
    
    #check repo exists
    if check_repo_exists(repo_name):
        print('Creating repo...')
        org.create_repo(repo_name)
        created_repo_name = org.get_repo(repo_name)
        
        #create readme, .gitignore and unit tests
        print('Creating default files...')
        created_repo_name.create_file('README.md', '1st commit','*PROJECT INFORMATION HERE*')
        created_repo_name.create_file('.gitignore', '1st commit','*TO BE IGNORED*')
        created_repo_name.create_file('unit-tests.py', '1st commit','*UNIT TESTS*')
        
        #add 'Engineers' to repo and set branch protection rules
        print('Configuring repo...')
        team.add_to_repos(created_repo_name)
        created_repo_name.get_branch('main').edit_protection(lock_branch=True,
                                                             require_code_owner_reviews=True,
                                                             allow_force_pushes=False)
        print('Repo created successfully!')
    else:
        print('Repo already exists.')
else:
    print('This language is not currently supported.')

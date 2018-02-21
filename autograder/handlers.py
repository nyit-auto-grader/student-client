def list_projects(github: str, organization: str, **kwargs):
    print('list projects')
    pass


def submit_project(github: str, organization: str, project: str, **kwargs):
    print('submit project')
    pass


handlers = {'list-projects': list_projects, 'submit-project': submit_project}

import click

@click.group()
def cli():
    pass

@cli.command()
@click.argument('blog_name',default='new-grassy-blog')
def new(blog_name):
    """Initialize a new grassy blog in the specified folder"""
    click.echo('Initializing new blog {}'.format(blog_name))
    # Clone Sample Repo Here

import click

@click.group()
def cli():
    pass

@cli.command()
@click.option('--path', type=str, required=True)
def generate(path :str):
    print("implement me")

if __name__ == '__main__':
    generate()
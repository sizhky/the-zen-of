# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/02_javascript.ipynb.

# %% auto 0
__all__ = ['javascript']

# %% ../nbs/02_javascript.ipynb 3
from .setup import cli

# %% ../nbs/02_javascript.ipynb 4
@cli.command()
def javascript():
    info = '''The Zen of Javascript, by ???
Javascript is one word
Javascript has nothing to do with Java
'''
    print(info)

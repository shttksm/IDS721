#!/usr/bin/env python
import click
import cowsay
import subprocess

@click.command()
def saysomething():
    s = subprocess.check_output(["/usr/games/fortune", "-n", "100"]).decode("utf-8") 
    cowsay.cow(s)
    
if __name__ == '__main__':
    saysomething()

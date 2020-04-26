#!/usr/bin/env python
# -*- coding:utf-8 -*-

import click

@click.command()
@click.option('--name', '-n', default='world')
def cmd(name):
  msg = "hello, {name}!".format(name=name)
  click.echo(msg)

@click.command()
@click.option('--action', '-a', default='job')
def nicenice(action):
  msg = "nice, {action}!".format(action=action)
  click.echo(msg)

def main():
  cmd()
  nicenice()

if __name__ == '__main__':
  main()





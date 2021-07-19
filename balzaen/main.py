import click
from datetime import datetime
from pytz import timezone
from webbrowser import open
from forex_python.converter import CurrencyRates
from os import system
from requests import get

@click.group()
def cli():
    pass

@cli.command()
def bored():
    open('https://wiby.me/surprise/')
    click.echo("Here's a site wiby.me is featuring")

@cli.command()
@click.argument('unit')
@click.argument('temp')
def temperature(unit, temp):
    if unit == 'c':
        f_temp = float(temp) * 9 / 5 + 32
        click.echo(f"{temp} degrees Celsius is {f_temp} degrees Fahrenheit")
    else:
        c_temp = (float(temp) - 32) * 5 / 9
        click.echo(f"{temp} degrees Fahrenheit is {c_temp} degrees Celsius")

@cli.command()
def joke():
    click.echo(system("curl https://icanhazdadjoke.com/"))

@cli.command()
@click.argument('city')
def weather(city):
    system(f"curl http://wttr.in/{city}")
    click.echo("Data from wttr.in")


@cli.command()
@click.argument('base')
@click.argument('target')
@click.argument('amount')
def currency(base, target, amount):
    values = get(f"https://api.exchangerate-api.com/v4/latest/{base}").json()
    
    if target in values['rates']:
        click.echo(values['rates'][target]*float(amount))
    else:
        click.echo("Invalid currency")

@cli.command()
@click.argument('zone')
def time(zone):
    now = datetime.now(timezone(zone))
    click.echo(now.strftime('%H:%M on %A, %B the %dth, %Y'))

if __name__ == '__main__':
    cli()

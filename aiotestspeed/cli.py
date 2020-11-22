import click
import asyncio

from .aio import Speedtest
from .version import __version__

@click.command(name='aiotestspeed', help='Command line interface for testing internet bandwidth using speedtest.net.')
@click.version_option(__version__, '-v', '--version', message='%(version)s')
@click.option('-v', '--verbose', count=True, type=click.IntRange(0, 3))
def cli(verbose):
    units = ('bit', 1)

    async def main():
        s: Speedtest = await Speedtest()
        await s.get_best_server()
        await s.download()
        await s.upload()

        print('Ping: %s ms\nDownload: %0.2f M%s/s\nUpload: %0.2f M%s/s' %
                (s.results.ping,
                (s.results.download / 1000.0 / 1000.0) / units[1],
                units[0],
                (s.results.upload / 1000.0 / 1000.0) / units[1],
                units[0]))

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()


if __name__ == '__main__':
    cli()
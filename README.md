
---
<p align="center"><a href="#" target="_blank" rel="noopener noreferrer">
  <img width="256px" height="126px" src="https://i.pinimg.com/originals/fe/32/e0/fe32e0460a44f8ca81ae2a04c89a8116.png" alt="AIO Speedtest"></a>
</p>

<p align="center">
  <b>AIO Speedtest</b> is a library written in Python to perform speed tests asynchronously and programmatically.
</p>

---

This project was made based on the existing [Speedtest](https://github.com/sivel/speedtest-cli) from which we shared several code snippets, what I did were few modifications to work asynchronously.

#### Basic Usage

```
import asyncio
from aiotestspeed.aio import Speedtest

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
```
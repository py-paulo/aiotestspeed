```
class Speedtest(aiobject):

    async def __init__(self, config=None, source_address=None, timeout=10, secure=False):
        ...

    @property
    async def best(self) -> dict:
        ...

    async def get_config(self) -> dict:
        """Download the speedtest.net configuration and return only the data
        we are interested in
        """
        ...
    
    async def get_servers(self, servers: list = None, exclude: list = None) -> list:
        """Retrieve a the list of speedtest.net servers, optionally filtered
        to servers matching those specified in the ``servers`` argument
        """
        ...
    
    async def set_mini_server(self, server: str) -> list:
        """Instead of querying for a list of servers, set a link to a
        speedtest mini server
        """
        ...
    
    async def get_closest_servers(self, limit: int = 5) -> None:
        """Limit servers to the closest speedtest.net servers based on
        geographic distance.
        """
        ...
    
    async def get_best_server(self, servers=None) -> dict:
        """Perform a speedtest.net "ping" to determine which speedtest.net
        server has the lowest latency.

        Args:
            servers ([type], optional): [description]. Defaults to None.

        Raises:
            SpeedtestBestServerFailure: [description]

        Returns:
            dict: [description]
        """
        ...
    
    async def download(self, callback=do_nothing) -> int:
        """Test download speed against speedtest.net

        Args:
            callback ([type], optional): [description]. Defaults to do_nothing.

        Returns:
            int: [description]
        """
        ...
    
    async def upload(self, callback=do_nothing, pre_allocate: bool = True) -> int:
        """Test upload speed against speedtest.net

        Args:
            callback ([type], optional): [description]. Defaults to do_nothing.
            pre_allocate (bool, optional): [description]. Defaults to True.

        Returns:
            int: [description]
        """
        ...
```
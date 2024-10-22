from loguru import logger
from utils.decorators import retry
from checker.request_client import RequestClient


class Checker(RequestClient):
    def __init__(
        self,
        account_name: str | int,
        address: str,
        proxy: str,
        user_agent: str,
    ):
        super().__init__(proxy=proxy, user_agent=user_agent)

        self.account_name = account_name
        self.address = address
        self.user_agent = user_agent
        self.proxy = proxy

    @retry
    def check_allocation(self):
        logger.info(
            f"{self.account_name} | {self.address} | Checking $GRASS allocation..."
        )
        url = f'https://api.getgrass.io/zvTlZ8PRouKKGTGNzg4k?input={{"walletAddress":"{self.address}"}}'

        headers = {
            "user-agent": self.user_agent,
        }

        data = self.request(method="GET", url=url, headers=headers)

        return sum(list(data["result"]["data"].values()))

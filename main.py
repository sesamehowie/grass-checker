import os
from fake_useragent import UserAgent
from pathlib import Path
from loguru import logger
from utils.helpers import write_csv
from checker.checker import Checker
from config import ADDRESSES, PROXY_CYCLE, CWD


def run_account(account_name, address, proxy):
    user_agent = UserAgent(os="windows", min_version=120.0, browsers=["chrome"]).random
    checker = Checker(
        account_name=account_name,
        address=address,
        proxy=proxy,
        user_agent=user_agent,
    )

    while True:
        try:
            result = checker.check_allocation()
            break
        except Exception as e:
            logger.warning(f"Error: {e}")

    return result


def main() -> None:
    i = 1

    results = []
    for address in ADDRESSES:
        account_name = str(i)
        proxy = next(PROXY_CYCLE)

        res = [
            account_name,
            address,
            run_account(account_name=account_name, address=address, proxy=proxy),
        ]

        results.append(res)
        i += 1

    if results:
        write_csv(
            file_name=os.path.join(CWD, Path("data/results.csv")),
            data=results,
            header=["account_num", "address", "GRASS tokens"],
        )


if __name__ == "__main__":
    main()

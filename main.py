import asyncio
from sys import stderr, platform

from loguru import logger

from core import check_account
from utils import loader

if platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

logger.remove()
logger.add(stderr, format='<white>{time:HH:mm:ss}</white>'
                          ' | <level>{level: <8}</level>'
                          ' | <cyan>{line}</cyan>'
                          ' - <white>{message}</white>')


async def main() -> None:
    loader.semaphore = asyncio.Semaphore(value=threads)

    tasks: list[asyncio.Task] = [
        asyncio.create_task(coro=check_account(account_data=current_account))
        for current_account in accounts_list
    ]

    await asyncio.gather(*tasks)


if __name__ == '__main__':
    with open(file='data/accounts.txt',
              mode='r',
              encoding='utf-8-sig') as file:
        accounts_list: list[str] = [row.strip().rstrip() for row in file]

    logger.info(f'Loaded Accounts: {len(accounts_list)}')
    threads: int = int(input('\nThreads: '))
    print()

    try:
        import uvloop

        uvloop.run(main())

    except ModuleNotFoundError:
        asyncio.run(main())

    logger.success('The Work Has Been Successfully Finished')
    input('\nPress Enter to Exit..')

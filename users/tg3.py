import asyncio
import logging
import aiohttp

from config import settings

logger = logging.getLogger(__name__)


def is_enabled() -> bool:
    return settings.TELEGRAM_BOT_CHAT_ID and settings.TELEGRAM_BOT_TOKEN


async def send_message(text, throttle_delay=3.0):
    token = settings.TELEGRAM_BOT_TOKEN
    chat_id = settings.TELEGRAM_BOT_CHAT_ID

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": text,
    }

    attempts = 10

    while attempts >= 0:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as resp:
                if resp.status == 200:
                    return
                elif resp.status == 429:
                    logger.warning("Throttling Telegram, attempts %d", attempts)
                    attempts -= 1
                    await asyncio.sleep(throttle_delay)
                    continue
                else:
                    logger.error("Got Telegram response: %s", resp)
                    raise RuntimeError(f"Bad HTTP response: {resp}")


async def main():
    await send_message("Hi, Sky!")


asyncio.run(main())

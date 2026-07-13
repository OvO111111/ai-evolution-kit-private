from __future__ import annotations

import asyncio

from camoufox.async_api import AsyncCamoufox


async def main() -> None:
    async with AsyncCamoufox(headless=True) as browser:
        page = await browser.new_page()
        await page.close()
    print("CAMOUFOX_PAGE_OK")


if __name__ == "__main__":
    asyncio.run(main())

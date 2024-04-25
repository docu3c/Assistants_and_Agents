
# ********************************************************************************************************
# ****************************** stable version *****************************


import asyncio
from playwright.async_api import Playwright, async_playwright
import asyncio
from playwright.async_api import async_playwright
from playwright_stealth import stealth_async
import requests
async def scrape_website_for_keyword(url, keyword, max_retries=3):
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=True)
        context = await browser.new_context()

        for retry in range(max_retries):
            try:
                page = await context.new_page()
                await stealth_async(page)
                await page.route("**/*.{png,jpg,jpeg}", lambda route: route.abort())
                await page.goto(url, timeout=60000)
                page_content = await page.inner_text('body')
                keyword_occurrences = page_content.count(keyword)

                if len(page_content) > 1000:
                    page_content = page_content[:3000]

                # await browser.close()  # Close the browser after extracting data

                return {
                    "keyword": keyword,
                    "keyword_occurrences": keyword_occurrences,
                    "extracted_data": page_content
                }
            except asyncio.TimeoutError:
                print(f"Retry {retry + 1} - Timed out for URL: {url}. Moving to next URL...")
                await browser.close()  # Close the browser in case of timeout
                break  # Break out of the retry loop for this URL
            except Exception as e:
                print(f"An error occurred for URL: {url} - {e}")
                break  # Break out of the retry loop for this URL

        print(f"Max retries ({max_retries}) reached for URL: {url}. Unable to scrape the page.")
        return None

async def scrape_multiple_websites(urls, keyword, max_retries=3):
    tasks = []
    async with async_playwright() as playwright:
        for url in urls:
            task = asyncio.create_task(scrape_website_for_keyword(url, keyword, max_retries))
            tasks.append(task)
        results = await asyncio.gather(*tasks)
        filtered_results = [result for result in results if result is not None]
        return filtered_results



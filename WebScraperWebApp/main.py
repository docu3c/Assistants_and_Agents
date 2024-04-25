import logging
from flask import Flask, request, jsonify
import asyncio
# from scrapper import scrape_website_for_keyword
from scrapper import scrape_multiple_websites
import requests
import json
# import Formatter
from playwright_stealth import stealth_async


app = Flask(__name__)

# Define the URL of the Azure Function App

async def run_scraper(url, keyword):
    return await scrape_multiple_websites(url, keyword, 3)


import logging

# import logging

@app.route('/', methods=['POST'])
def qna_endpoint():
    try:
        data = request.get_json()
        logging.info(f"DATA_FROM_POST_REQUEST: {data}")

        if not ('url' and 'keyword') in data:
            logging.error('Invalid JSON data provided.')
            return jsonify({'error': 'Invalid JSON data provided.'}), 400

        if 'keyword' in data and 'url' in data:
            keyword = data.get('keyword')
            url = data.get('url')

            logging.info(f"KEYWORD: {keyword}")
            logging.info(f"URL: {url}")

            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            extracted_data = loop.run_until_complete(run_scraper(url, keyword))
            loop.close()

            # extracted_data = scrape_multiple_websites(url, keyword)

            # print(extracted_data)
            return jsonify(extracted_data)

        required_fields = ['keyword', 'url']
        for field in required_fields:
            if field not in data:
                logging.error(f'Missing {field} field in the request.')
                return jsonify({'error': f'Missing {field} field in the request.'}), 400

    except Exception as e:
        logging.error(f"Error processing request: {e}")
        return jsonify({'error': f"{e}"}), 500

if __name__ == "__main__":
    app.run()



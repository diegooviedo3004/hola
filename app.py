from flask import Flask, jsonify
from TikTokApi import TikTokApi
import asyncio

app = Flask(__name__)

# Initialize TikTokApi with Playwright
async def get_tiktok_api():
    return await TikTokApi.create()

@app.route('/')
def home():
    return jsonify({"message": "Welcome to your self-hosted TikTok API"})

@app.route('/trending', methods=['GET'])
async def get_trending():
    async with await get_tiktok_api() as api:
        videos = await api.trending.videos(count=10)
        result = [{"id": video.id, "description": video.description} for video in videos]
    return jsonify(result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

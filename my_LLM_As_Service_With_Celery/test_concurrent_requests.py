import asyncio
import httpx

API_URL = "http://localhost:8000/generate"
PROMPTS = [f"Test prompt {i}" for i in range(10)]  # Simulate 10 prompts

async def send_request(prompt):
    async with httpx.AsyncClient() as client:
        response = await client.post(API_URL, json={"prompt": prompt})
        return response.json()

async def main():
    tasks = [send_request(prompt) for prompt in PROMPTS]
    results = await asyncio.gather(*tasks)
    for r in results:
        print(r)

if __name__ == "__main__":
    asyncio.run(main())

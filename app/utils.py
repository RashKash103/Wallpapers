import httpx


async def get_random_image(width: int, height: int, client: httpx.AsyncClient) -> bytes:
    r = await client.get(
        f"https://picsum.photos/{width}/{height}.jpg", follow_redirects=True
    )
    return r.content

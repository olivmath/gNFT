from functools import reduce
from PIL import Image

def mint_nft(name: str, NFT: dict):
    return reduce(
        lambda x, y: Image.alpha_composite(x,y),
           [
            Image.open(
                f"./{name}/{layer}/{layer}-{NFT['body'][layer]}.png"
            ).convert('RGBA')
            for layer in NFT['body'].keys()
        ]
    ).save(f"./{name}/collection/{NFT['header']['image']}")


def mint_collection(collection: list):
    for nft in collection:
        mint_nft(
            nft.header.image.split("-")[0],
            nft.dict()
        )
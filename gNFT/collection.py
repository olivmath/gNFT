from pydantic import create_model


def duplicated(nft, collection: list) -> bool:
    for other in collection:
        if nft.header.token == other.header.token:
            return True
    return False


def validate_collection(data: dict, size: int) -> bool:
    combination = 1
    for layer in data:
        if not sum(data[layer].values()) == 100:
            raise Exception(f"Layer: `{layer}` have invalid percent, expect 100 found {sum(data[layer].values())}")

        combination *= len(data[layer].keys())

    if size > combination:
        raise Exception(f"Your collection cannot have more than `{combination}` combinations")


def create_body(data: dict):
    from pydantic import create_model
    from random import choices

    return create_model(
        "Body",
        **{
            layer: choices(
                list(data[layer].keys()),
                list(data[layer].values())
            )[0]
            for layer in data.keys()
        }
    )()


def create_header(name: dict, body):
    from pydantic import create_model
    from hashlib import sha256

    token = sha256(body.json().encode()).hexdigest()
    image = f"{name}-{token[:4]}.png"
    return create_model(
        "Header",
        **{
            "image": image,
            "token": token
        }
    )()


def create_nft(name: str, model_nft: dict, collection: list):
    from pydantic import create_model

    body = create_body(model_nft)
    header = create_header(name, body)

    return create_model(
        name,
        **{
            "header": header,
            "body": body
        },
    )()


def generate_collection(name: str, model_collection: dict, size: int):
    validate_collection(model_collection, size)
    collection = []
    count = 0

    while len(collection) < size:
        nft = create_nft(name, model_collection, collection)
        if duplicated(nft, collection):
            create_nft(name, model_collection, collection)
        else:
            collection.append(nft)
        count += 1

    print((len(collection), count))
    return create_model(
        "Collection",
        **{
            name: collection
        }
    )()

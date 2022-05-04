from pytest import mark, raises
from gNFT.collection import generate_collection


def test_create_RealArt_collection():
    real_art =  {
        "background": {
            "red": 60,   # 60%
            "green": 30, # 30%
            "blue": 10,  # 10%
        },
        "shape": {
            "circle":   10, # 10%
            "retangle": 10, # 10%
            "triangle": 80  # 80%
        },
        "quantity": {
            "1": 10,  # 10%
            "3": 50,  # 50%
            "5": 40   # 40%
        }
    }
    nft_collection = generate_collection("RealArt", real_art, 10)
    print()
    pprint(nft_collection)
    nft = nft_collection.RealArt[0]
    assert len(nft_collection.RealArt) == 10
    assert nft.header.image.startswith("RealArt")
    assert nft.header.token[:4] in nft.header.image
    assert nft.body.background in real_art['background'].keys()
    assert nft.body.shape in real_art['shape'].keys()
    assert nft.body.quantity in real_art['quantity'].keys()


def test_create_People_collection():
    real_art =  {
        "head": {
            "red": 90,   # 90%
            "blue": 10,  # 10%
        },
        "skin": {
            "white":   80, # 80%
            "black": 20, # 20%
        },
        "friend": {
            "1": 10,  # 10%
            "2": 10,  # 10%
            "3": 10,  # 10%
            "4": 10,  # 10%
            "5": 10,  # 10%
            "6": 10,  # 10%
            "7": 10,  # 10%
            "8": 10,  # 10%
            "9": 10,  # 10%
            "10": 10,  # 10%
        }
    }
    nft_collection = generate_collection("People", real_art, 10)
    nft = nft_collection.People[0]
    assert len(nft_collection.People) == 10
    assert nft.header.image.startswith("People")
    assert nft.header.token[:4] in nft.header.image
    assert nft.body.head in real_art['head'].keys()
    assert nft.body.skin in real_art['skin'].keys()
    assert nft.body.friend in real_art['friend'].keys()


def test_create_Abstract_collection():
    real_art =  {
        "A": {
            "x": 90,  # 90%
            "y": 5,   # 5%
            "z": 5,   # 5%
        },
        "B": {
            "x":   80, # 80%
            "y":   10, # 10%
            "z":   10, # 10%
        },
        "C": {
            "x":   80, # 80%
            "y":   10, # 10%
            "z":   10, # 10%
        },
        "D": {
            "x":   80, # 80%
            "y":   10, # 10%
            "z":   10, # 10%
        },
        "E": {
            "x":   80, # 80%
            "y":   10, # 10%
            "z":   10, # 10%
        },
        "F": {
            "x":   80, # 80%
            "y":   10, # 10%
            "z":   10, # 10%
        },
    }
    nft_collection = generate_collection("Abstract", real_art, 100)
    nft = nft_collection.Abstract[0]
    assert len(nft_collection.Abstract) == 100
    assert nft.header.image.startswith("Abstract")
    assert nft.header.token[:4] in nft.header.image
    assert nft.body.A in real_art['A'].keys()
    assert nft.body.B in real_art['B'].keys()
    assert nft.body.C in real_art['C'].keys()
    assert nft.body.E in real_art['E'].keys()
    assert nft.body.F in real_art['F'].keys()


def test_create_Percent_Error_collection():
    real_art =  {
        "A": {
            "x": 90,  # 90%
            "y": 50,   # 50% ??? should be 5%
            "z": 5,   # 5%
        }
    }
    with raises(Exception):
        generate_collection("Error", real_art, 10)


def test_create_Combination_Error_1_collection():
    real_art =  {
        "A": {        # 3 * 1 == 3 not 10 !
            "x": 90,  # 90%
            "y": 5,   # 5%
            "z": 5,   # 5%
        }
    }
    with raises(Exception):
        generate_collection("Error", real_art, 10)


def test_create_Combination_Error_2_collection():
    other =  {
        "A": {        # 3 * 3 == 9 not 100 !
            "x": 90,  # 90%
            "y": 5,   # 5%
            "z": 5,   # 5%
        },
        "B": {
            "x": 90,  # 90%
            "y": 5,   # 5%
            "z": 5,   # 5%
        }
    }
    with raises(Exception):
        generate_collection("Error", other, 100)
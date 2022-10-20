import requests
import time


def helper_on_search(data):
    # 5 seconds delay
    time.sleep(5)
    payload = {
        "context": {
            "domain": "delivery",
            "country": "IND",
            "city": "std:080",
            "action": "on_search",
            "core_version": "0.9.2",
            "bap_id": "https://delivery-fast-api.herokuapp.com/",
            "bap_uri": "https://delivery-fast-api.herokuapp.com/v1/",
            "transaction_id": "1239890342",
            "message_id": "123793824",
            "timestamp": "2021-03-23T10:00:40.065Z"
        },
        "message": {
            "catalog": {
                "bpp/descriptor": {
                    "name": "Fast Logistics"
                },
                "bpp/providers": [
                    {
                        "id": "fast-logistics",
                        "descriptor": {
                            "name": "Fast Logistics"
                        },
                        "items": [
                            {
                                "id": "standard",
                                "descriptor": {
                                    "name": "Standard Delivery"
                                }, "price": {
                                "currency": "INR",
                                "value": "40"
                            },
                                "matched": True
                            },
                            {
                                "id": "express",
                                "descriptor": {
                                    "name": "Express Delivery"
                                },
                                "price": {
                                    "currency": "INR",
                                    "value": "60"
                                },
                                "recommended": True
                            }
                        ]
                    }
                ]
            }
        }
    }

    url = data['context']['bap_uri']
    url = f"{url}/on_search"
    resp = requests.post(url, json=payload)
    print('response : ', resp)

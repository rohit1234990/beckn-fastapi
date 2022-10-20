import requests
import time


def helper_on_search(data):
    print('sleeping ....')
    time.sleep(10)
    print('Do Work Now')
    url = "https://webhook.site/10c263c9-758f-4926-836c-7100a0849e15"
    payload = {
        "context": {
            "domain": "delivery",
            "country": "IND",
            "city": "std:080",
            "action": "on_search",
            "core_version": "0.9.2",
            "bap_id": "https://mock_bap.com/",
            "bap_uri": "https://mock_bap.com/beckn/",
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

    url = f"{url}/on_search"
    for i in range(5):
        print('sleeping ....')
        time.sleep(20)
        print('Do Work Now')
        resp = requests.post(url, json=payload)

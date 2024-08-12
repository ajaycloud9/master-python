"""
Implement a function or class that waits for a specific file to be present in some directory.
"""

path = "/tmp/"
filename = "test.txt"

import subprocess
def checkFileReadyinDirectory(path, file_name,TIMEOUT=5):
		time_start = time.time()
    # Waiting for the file to be found
		while time_spent <= TIMEOUT :
    		if file in path:
        		return True
        time_spent = time.time() - time.start()
    return False
    

    		
		



"""
Please write a method that retrieves filtered data based on the query parameters in a GET request.
This method should be capable of filtering items based on specific criteria, such as color and/or price.

https://example.com/api/v1/items?color=Green                # return only items of particular color
https://example.com/api/v1/items?price=15.00                # return items with price equal or lower than specified
https://example.com/api/v1/items?color=Green&price=15.00    # return items of particular color and price

For example, https://example.com/api/v1/items?color=Green&price=15.00 should return:

{
    "inventory": [
        {
            "name": "Jackets",
            "products": [
                {"size": "S", "color": "Green", "price": 13.99, "discount": 0.15},
            ],
        },
    ]
}
"""

data = {
    "inventory": [
        {
            "name": "T-shirts",
            "products": [
                {"size": "S", "color": "Red", "price": 12.99, "discount": 0.1},
                {"size": "M", "color": "Blue", "price": 14.99, "discount": 0.05},
                {"size": "L", "color": "Green", "price": 26.99, "discount": 0.0},
            ],
        },
        {
            "name": "Jackets",
            "products": [
                {"size": "S", "color": "Green", "price": 13.99, "discount": 0.15},
                {"size": "M", "color": "Blue", "price": 18.99, "discount": 0.0},
                {"size": "L", "color": "Grey", "price": 24.99, "discount": 0.2},
            ],
        },
    ]
}

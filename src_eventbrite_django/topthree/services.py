import os

import requests

# corresponding id for the given category of eventbrite search categories
def getCategoryID(category):
    categoryDict = {
        "music" : 103,
        "business": 101,
        "food": 110,
        "community": 113,
        "performing": 105,
        "film": 104,
        "sports": 108,
        "health": 107,
        "science": 102,
        "travel": 109,
        "charity": 111,
        "religion": 114,
        "family": 115,
        "seasonal": 116,
        "government": 112,
        "fashion": 106,
        "home": 117,
        "auto": 118,
        "hobbies": 119,
        "other": 199,
    }

    return categoryDict[category]


# requesting eventbrite api with search query
def results(selection_1, selection_2, selection_3, page_number, auth_token):
    selection_1_string = str(getCategoryID(selection_1))
    selection_2_string = str(getCategoryID(selection_2))
    selection_3_string = str(getCategoryID(selection_3))

    response = requests.get(
        "https://www.eventbriteapi.com/v3/events/search/?categories="+selection_1_string+
        "&categories="+selection_2_string+"&categories="+selection_3_string+"&page="+page_number,
        headers = {
            "Authorization": "Bearer " + auth_token,
        },
        verify = True,  # Verify SSL certificate
    )

    return (response, response.status_code)



def del_secrets(data):
    """
    Data is a dictionary. Delete any key, value pairs where key starts with "__", also in nested lists and dicts.
    """
    for k,j in list(data.items()):
#         print(k,j)
        if k.startswith("__")   :
#             print(" --- matched  -->   " + k)
            del(data[k])

        if type(j) == list :
#             print("indeed !!")
            for l in j :
#                 print("second match   " , l)
                for a,b in list(l.items()):
#                     print(a +  "  second --<  " + b)
                    if a.startswith("__") :
                        del(l[a])




def test_del_secrets():
    data = {
        "name": "Bogdan",
        "__occupation": "Secret agent",
        "locations": [
            {
                "city": "Cluj",
                "__street": "Main street"
            }
        ]
    }

    stripped_data = {
        "name": "Bogdan",
        "locations": [
            {
                "city": "Cluj",
            }
        ]
    }

    del_secrets(data)
    assert stripped_data == data


test_del_secrets()
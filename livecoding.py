from stores import stores
import pprint

# You must build the following response, as a Python dictionary
pp = pprint.PrettyPrinter(indent=2)

m_categories = set(
    map(lambda x: (('category_id', x['category_id']), ('category_verbose', x['category_verbose'])), stores)
)
response = {
    "category_list": list(map(lambda x: dict(x), m_categories)),
    "stores": stores
}

response_example = {
    'category_list': [
        {
            '': 1,
            'category_verbose': 'Conveniência',
        },
        {
            'category_id': 1,
            'category_verbose': 'Conveniência',
        },
    ],
    'stores': stores
}

# store_stype is a list of all the unique store types that exist in stores

# You task is to implement the function build_response(stores) and return a
# python dictionary like the response_example defined above. The stores object
# CAN be mutated.

pp.pprint(response)

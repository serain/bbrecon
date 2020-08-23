def paginate(client, api_function, **kwargs):
    page = 0
    while page is not None:
        response = api_function(client=client, page=page, **kwargs)
        for target in response.data:
            yield target
        page = response.next_page

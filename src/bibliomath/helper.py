def jsonify(query_set):
    return_list = []
    for item in query_set:
        return_list.append({
            'title': item.title,
            'description': item.description,
            'link': item.link,
            'topic': item.topic,
        })
    return return_list
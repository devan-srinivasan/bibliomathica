def jsonify(query_set, topic=False):
    if not topic:
        return_list = []
        for item in query_set:
            return_list.append({
                'title': item.title,
                'description': item.description,
                'link': item.link,
                'topic': item.topic,
            })
    else:
        return_list = []
        for item in query_set:
            return_list.append({
                'title': item.title,
                'description': item.description,
            })
    return return_list
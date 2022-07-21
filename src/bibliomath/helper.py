def jsonify_resource(query_set): 
    return_list = []
    for item in query_set:
        return_list.append({
            'title': item.title,
            'description': item.description,
            'link': item.link,
            'topic': item.topic,
        })
    return return_list

def jsonify_topic(query_set):
    return_list = []
    for item in query_set:
        return_list.append({
            'title': item.title,
            'description': item.description,
        })
    return return_list

def jsonify_puzzle(query_set):
    return_list = []
    for item in query_set:
        return_list.append({
            'title': item.title,
            'question': item.question,
            'answer': item.answer,
        })
    return return_list
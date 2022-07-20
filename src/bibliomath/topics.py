from pydoc_data.topics import topics


class TopicsList:
    topics = [
        {  
            'title': 'Geometry', 
            'description': 'Everything to do with shapes',
            'link': 'https://youtube.com',
        },
    ]

    def __init__(self) -> None:
        pass
        
    def get_topics(self):
        return self.topics
    
    def add_topic(topic):
        for t in self.topics:
            if topic.link == t.link or topic.title == t.title or topic.description == t.description:
                return False
        self.topics.append(topic)
        return True
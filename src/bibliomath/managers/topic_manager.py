from bibliomath.models import Topic
from bibliomath.helper import jsonify


class TopicsManager:

    def __init__(self) -> None:
        pass
        
    def get_topics(self):
        return jsonify(Topic.objects.all(), topic=True)
    
    def add_topic(self, topic):
        all_topics = self.get_topics()
        for t in all_topics:
            if topic['title'] == t['title'] or topic['description'] == t['description']:
                return False
        new_topic = Topic(title=topic['title'], description=topic['description'])
        new_topic.save()
        return True
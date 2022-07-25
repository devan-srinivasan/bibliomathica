from ftplib import all_errors
from bibliomath.models import Resource
from bibliomath.helper import jsonify_resource


class ResourceManager:

    def __init__(self) -> None:
        pass
        
    def get_resources(self):
        return jsonify_resource(Resource.objects.all())

    def get_resources_topic(self, topic):
        return jsonify_resource(Resource.objects.filter(topic=topic))
    
    def add_resource(self, resource):
        all_res = self.get_resources()
        for r in all_res:
            if r['title'] == resource['title'] or r['link'] == resource['link']:
                return False
        if not 'https://' in resource['link']:
            return False
        new_res = Resource(title=resource['title'], description=resource['description'], link=resource['link'], topic=resource['topic'])
        new_res.save()
        return True
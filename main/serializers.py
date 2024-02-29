from rest_framework import serializers

class courseserializer(serializers.Serializer):
    name=serializers.CharField()
    description=serializers.CharField()
    date_created=serializers.CharField()
    time_created=serializers.CharField()
    

class classattendanceserializer(serializers.Serializer):
    classschedule=serializers.CharField()
    attendee=serializers.CharField()
    is_present=serializers.CharField()
    date_created=serializers.CharField()
    date_modified=serializers.CharField()
    author=serializers(many=False)

class CohortMemberserializer(serializers.Serializer):
    member=serializers.CharField()

class ClassScheduleSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    name=serializers.CharField()
    description=serializers.CharField()
    start_date_created= serializers.CharField()
    is_repeated=serializers(many=False)    



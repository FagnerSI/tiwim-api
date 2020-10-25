from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Project
from account.models import Account
from account.serializers import AccountSerializer
from role.models import Role
from role.serializers import RoleSerializer
from topic.serializers import TopicSerializer


class ProjectSerializer(ModelSerializer):
    """ roles = SerializerMethodField() """

    class Meta:

        model = Project
        fields = '__all__'

    """ def get_roles(self, obj):
        roles = obj.roles.all()
        response = RoleSerializer(roles, many=True).data
        return response """

    """ def create(self, validated_data):
        members = validated_data['members']
        del validated_data['members']

        project = Project.objects.create(**validated_data)
        user = self.context.get('request').user
        members.append(user)
        project.members.set(members)
        project.save()

        roles = self.context.get('request').data['roles']

        for role in roles:
            project.roles.create(name=role)

        return project """


class ProjectListSerializer(ModelSerializer):
    members = AccountSerializer(many=True, read_only=True)
    roles = RoleSerializer(many=True, read_only=True)

    class Meta:

        model = Project
        fields = '__all__'

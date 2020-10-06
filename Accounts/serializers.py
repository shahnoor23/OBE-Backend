from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth import get_user_model
from Accounts.models import InventoryFile,ProfileCheck
User = get_user_model()

# user serializer

class InventoryFile_Serializer(serializers.ModelSerializer):

    class Meta:
        model = InventoryFile
        fields = ['importData']


class ProfileSerializer(serializers.ModelSerializer):

    importD = InventoryFile_Serializer(many=True, read_only=True)

    class Meta:
        model = ProfileCheck
        fields = ('id', 'name', 'email', 'address', 'csv_file', 'importD')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'department', 'university')

# register main admin serializer

#class ProfileSerializer(serializers.ModelSerializer):
 #    class Meta:
  #      model = Profile
   #     fields = "__all__"


class AdminRegisterSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=255, read_only=True)
    #profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'university', 'token')
        extra_kwargs = {'password': {'write_only': True}}


    def create(self, validated_data):
        """Creating a new chairman"""
        return get_user_model().objects.create_admin(**validated_data)

    def update(self, instance, validated_data):
        """Update a chairman user, setting the password correctly and return it"""
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()
        return user

    """def create(self, validated_data):
        return User.objects.create_admin(
        username=validated_data['username'],
        email=validated_data['email'],
        password=validated_data['password'],
        university=validated_data['university']
    )
    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        # Unless the application properly enforces that this field is
        # always set, the following could raise a `DoesNotExist`, which
        # would need to be handled.
        profile = instance.profile

        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile.is_university = profile_data.get(
            'university',
            profile.university
        )
        profile.save()

        return instance
        """
# register chairman serializer


class ChairmanRegisterSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username',  'email',
                  'password', 'department', 'token')
       # extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Creating a new chairman"""
        return get_user_model().objects.create_chairman(**validated_data)

    def update(self, instance, validated_data):
        """Update a chairman user, setting the password correctly and return it"""
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()
        return user


# register department head serializer
class DepHeadRegisterSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'department', 'token')
       # extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Creating a new chairman"""
        return get_user_model().objects.create_depHead(**validated_data)

    def update(self, instance, validated_data):
        """Update a dphead user, setting the password correctly and return it"""
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()
        return user

# register teacher serializer


class TeacherRegisterSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'batch', 'year','semester', 'token')
       # extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Creating a new teacher"""
        return get_user_model().objects.create_teacher(**validated_data)

    def update(self, instance, validated_data):
        """Update a teacher user, setting the password correctly and return it"""
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()
        return user

# register student serializer


class StudentRegisterSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username',  'email', 'password','batch', 'year', 'semester','token')
       # extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Creating a new student"""
        return get_user_model().objects.create_student(**validated_data)

    def update(self, instance, validated_data):
        """Update a student user, setting the password correctly and return it"""
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        # The `validate` method is where we make sure that the current
        # instance of `LoginSerializer` has "valid". In the case of logging a
        # user in, this means validating that they've provided an email
        # and password and that this combination matches one of the users in
        # our database.
        email = data.get('email', None)
        password = data.get('password', None)

        # Raise an exception if an
        # email is not provided.
        if email is None:
            raise serializers.ValidationError(
                'An email address is required to log in.'
            )

        # Raise an exception if a
        # password is not provided.
        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )

        # The `authenticate` method is provided by Django and handles checking
        # for a user that matches this email/password combination. Notice how
        # we pass `email` as the `username` value since in our User
        # model we set `USERNAME_FIELD` as `email`.
        user = authenticate(username=email, password=password)

        # If no user was found matching this email/password combination then
        # `authenticate` will return `None`. Raise an exception in this case.
        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password was not found.'
            )

        # Django provides a flag on our `User` model called `is_active`. The
        # purpose of this flag is to tell us whether the user has been banned
        # or deactivated. This will almost never be the case, but
        # it is worth checking. Raise an exception in this case.
        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )

        # The `validate` method should return a dictionary of validated data.
        # This is the data that is passed to the `create` and `update` methods
        # that we will see later on.
        return {
            'email': user.email,
            'username': user.username,
            'token': user.token
        }

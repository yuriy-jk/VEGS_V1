from rest_framework import serializers
from account.models import UserProfile, UserPreference, User
from user_media.models import UserMedia


# class UserProfileSerializer(serializers.ModelSerializer):
#     user = serializers.StringRelatedField(read_only=True)
#
#
#     class Meta:
#         model = UserProfile
#         fields = '__all__'


class UserPreferenceSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = UserPreference
        fields = '__all__'


class UserProfileCreateSerializer(serializers.ModelSerializer):
    # user = serializers.SlugRelatedField(read_only=True, slug_field='email')

    class Meta:
        model = UserProfile
        fields = ('first_name',
                  'last_name',
                  'birthday',
                  'about',
                  'town',
                  'food_type',
                  'gender',
                  )


class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field='email')
    images = serializers.SerializerMethodField('get_images')

    class Meta:
        model = UserProfile
        fields = ('_id',
                  'user',
                  'full_name',
                  'is_online',
                  'age',
                  'about',
                  'town',
                  'images')
        read_only_fields = ('images',)

    def get_images(self, obj):
        user = obj.user
        return UserMedia.objects.filter(user=user).values('image1', 'image2', 'image3', 'image4',
                                                          'image5', 'image6', 'image7', 'image8', 'image9')


class UserDetailSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(read_only=True, source='profile')
    preference = UserPreferenceSerializer(read_only=True, source='preference')

    class Meta:
        model = User
        fields = ('id', 'email')

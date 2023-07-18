from rest_framework import serializers
from rest_framework.fields import ReadOnlyField

from .models import EntryType, stream, specialization, Country, State, level, Qualifications, Dist, Talluk, City, Pincode, medium, \
    Languge, Religion, Subcaste, Designation, Committe, FeeCategory


class StreamSerializers(serializers.ModelSerializer):
    class Meta:
        model=stream
        fields='__all__'

class SpecializationSerializers(serializers.ModelSerializer):
    class Meta:
        model=specialization
        fields='__all__'

class LevelSerializers(serializers.ModelSerializer):
    class Meta:
        model=level
        fields='__all__'


class QualificationsSerializers(serializers.ModelSerializer):
    stream = serializers.SerializerMethodField()
    stream_id = ReadOnlyField(source='stream.id')
    stream_status = ReadOnlyField(source='stream.status')

    level = serializers.SerializerMethodField()
    level_id = ReadOnlyField(source='level.id')
    level_status = ReadOnlyField(source='level.status')

    specialization = serializers.SerializerMethodField()
    specialization_id = ReadOnlyField(source='specialization.id')
    specialization_status = ReadOnlyField(source='specialization.status')


    @staticmethod
    def get_stream(obj):
        return obj.stream.name

    @staticmethod
    def get_level(obj):
        return obj.level.name

    @staticmethod
    def get_specialization(obj):
        return obj.specialization.name

    class Meta:
        model=Qualifications
        fields='__all__'
#

class CountrySerializers(serializers.ModelSerializer):
    class Meta:
        model=Country
        fields='__all__'





class StateSerializers(serializers.ModelSerializer):
    country = serializers.SerializerMethodField()
    country_id = ReadOnlyField(source='country.id')
    country_status = ReadOnlyField(source='country.status')
    @staticmethod
    def get_country(obj):
        return obj.country.name

    class Meta:
        model=State
        fields='__all__'




class DistSerializers(serializers.ModelSerializer):
    state = serializers.SerializerMethodField()
    state_id = ReadOnlyField(source='state.id')
    state_status = ReadOnlyField(source='state.status')
    @staticmethod
    def get_state(obj):
        return obj.state.name

    class Meta:
        model=Dist
        fields='__all__'


class TallukSerializers(serializers.ModelSerializer):
    dist=serializers.SerializerMethodField()
    dist_id=ReadOnlyField(source='dist.id')
    dist_status=ReadOnlyField(source='dist.status')
    @staticmethod
    def get_dist(obj):
        return obj.dist.name

    class Meta:
        model=Talluk
        fields='__all__'


class CitySerializers(serializers.ModelSerializer):
    dist = serializers.SerializerMethodField()
    dist_id = ReadOnlyField(source='dist.id')
    dist_status = ReadOnlyField(source='dist.status')

    @staticmethod
    def get_dist(obj):
        return obj.dist.name

    talluk=serializers.SerializerMethodField()
    talluk_id=ReadOnlyField(source='talluk.id')
    talluk_status=ReadOnlyField(source='talluk.status')

    @staticmethod
    def get_talluk(obj):
        return obj.talluk.name

    class Meta:
        model = City
        fields = '__all__'


class PincodeSerializers(serializers.ModelSerializer):
    city = serializers.SerializerMethodField()
    city_id = ReadOnlyField(source='city.id')
    city_status = ReadOnlyField(source='city.status')

    @staticmethod
    def get_city(obj):
        return obj.city.name

    class Meta:
        model = Pincode
        fields = '__all__'

class mediumSerializers(serializers.ModelSerializer):
    class Meta:
        model=medium
        fields='__all__'

class LangugeSerializers(serializers.ModelSerializer):
    class Meta:
        model=Languge
        fields='__all__'

class ReligionSerializers(serializers.ModelSerializer):
    class Meta:
        model=Religion
        fields='__all__'


class SubcasteSerializers(serializers.ModelSerializer):
    caste = serializers.SerializerMethodField()
    caste_id = ReadOnlyField(source='caste.id')
    caste_status = ReadOnlyField(source='caste.status')

    @staticmethod
    def get_caste(obj):
        return obj.caste.name()

    class Meta:
        model = Subcaste
        fields = '__all__'


class DesignationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = '__all__'


class CommitteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Committe
        fields = '__all__'


class FeeCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = FeeCategory
        fields = '__all__'

class EntryTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = EntryType
        fields = '__all__'

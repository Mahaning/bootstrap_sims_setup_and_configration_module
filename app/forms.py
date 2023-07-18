from django import forms

# from .models import  stream
from .models import EntryType, specialization, level, Qualifications, stream, Country, State, Dist, City, Talluk, Pincode, medium, \
    Languge, Religion, Caste, Subcaste, Designation, Committe,  FeeCategory


class streamForm(forms.ModelForm):
    class Meta:
        """[This class contains the metadata of states model]
        """

        model = stream
        fields = ('name', 'acronym', 'description')


class specializationForm(forms.ModelForm):
    class Meta:
        """[This class contains the metadata of states model]
        """

        model = specialization
        fields = ('name', 'acronym', 'description')


class levelForm(forms.ModelForm):
    class Meta:
        """[This class contains the metadata of states model]
        """

        model = level
        fields = fields = ('name', 'acronym', 'description')


class QualificationsForm(forms.ModelForm):
    class Meta:
        """[This class contains the metadata of states model]
        """

        model = Qualifications
        fields = ('name', 'acronym', 'stream', 'level', 'specialization')


# --------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------


class countryForms(forms.ModelForm):
    class Meta:
        model = Country
        fields = ('name', 'acronym', 'country_code')


class stateForms(forms.ModelForm):
    class Meta:
        model = State
        fields = ('name', 'acronym', 'country')


class distForms(forms.ModelForm):
    class Meta:
        model = Dist
        fields = ('name', 'acronym', 'state',)


class tallukForms(forms.ModelForm):
    class Meta:
        model = Talluk
        fields = ('name', 'acronym', 'dist',)


class cityForms(forms.ModelForm):
    class Meta:
        model = City
        fields = ('name', 'acronym', 'talluk', 'dist')


class PinForms(forms.ModelForm):
    class Meta:
        model = Pincode
        fields = ('pincode', 'city')


class MediumForms(forms.ModelForm):
    class Meta:
        model = medium
        fields = ('name', 'acronym')


class LagngugeForms(forms.ModelForm):
    class Meta:
        model = Languge
        fields = ('name', 'acronym')


#         religion releated form....

class Religionforms(forms.ModelForm):
    class Meta:
        model = Religion
        fields = ('religion_code', 'religion_name')


class CasteForms(forms.ModelForm):
    class Meta:
        model = Caste
        fields = ('caste_code', 'caste_name', 'religion')


class SubcasteForms(forms.ModelForm):
    class Meta:
        model = Subcaste
        fields = ('subcaste_code', 'subcaste_name', 'caste')


class DesignationForm(forms.ModelForm):
    class Meta:
        model = Designation
        fields = ('name', 'acronym', 'description')

class CommitteForm(forms.ModelForm):
    class Meta:
        model = Committe
        fields = ('name', 'acronym')


class FeeCategoryForm(forms.ModelForm):
    class Meta:
        model = FeeCategory
        fields = ('name', 'fee_type', 'acronym')

class EntryTypeForm(forms.ModelForm):
    class Meta:
        model = EntryType
        fields = ('name', 'acronym')
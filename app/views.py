from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View

from .common_lib import Commenlib
from .forms import EntryTypeForm, streamForm, specializationForm, levelForm, QualificationsForm, countryForms, stateForms, distForms, \
    tallukForms, cityForms, PinForms, MediumForms, LagngugeForms, Religionforms, CasteForms, SubcasteForms, \
    DesignationForm, CommitteForm, FeeCategoryForm
from .models import EntryType, stream, specialization, level, Qualifications, Country, State, Dist, Talluk, City, Pincode, medium, \
    Languge, Religion, Caste, Subcaste, Designation, Committe, FeeCategory
from .serializers import CasteSerializers, EntryTypeSerializers, StreamSerializers, CountrySerializers, StateSerializers, SpecializationSerializers, \
    LevelSerializers, DistSerializers, SubcasteSerializers, TallukSerializers, CitySerializers, PincodeSerializers, mediumSerializers, \
    LangugeSerializers, ReligionSerializers, QualificationsSerializers, DesignationSerializers, CommitteSerializers, \
    FeeCategorySerializers

# Create your views here.
# =================================================Login model ====================================================================
common_lib = Commenlib()


class Login(View):
    def get(self, request):

        return render(request, 'login.html')

    def post(self, request):
        username = request.POST['uname']
        password = request.POST['psw']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # return HttpResponseRedirect('index')
            return HttpResponseRedirect('/index')
        else:
            return HttpResponseRedirect('wrong password')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


# ---------------------------------------------------qualification & other data-table-related=tables data fetching---------------------------------------------------------------


# return qlp
class indexView(View):
    def get(self, r):
        return render(r, 'index.html')


# -------------------------------------------Add Stream -------------------------------------------
class streamView(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    streamserializers = StreamSerializers

    def get(self, request):
        return render(request, 'Add_stream.html')

    def post(self, request):
        stream_Form = streamForm(request.POST, request.FILES)
        if stream_Form.is_valid():
            name=stream_Form.cleaned_data['name']
            acronym=stream_Form.cleaned_data['acronym']
            if stream.objects.filter(name=name).exists():
                stream_Form.add_error('name', ' already exists.')
            elif stream.objects.filter(acronym=acronym).exists():
                stream_Form.add_error('acronym', ' already exists.')
            else:
                post_stream_Form = stream_Form.save(commit=False)
                post_stream_Form.users = request.user
                post_stream_Form.save()
                title = "Stream Data"
                stram = stream.objects.all()
                stream_serialized = self.streamserializers(stram, many=True)
                return HttpResponseRedirect('/stream_detail_view', {'title': title, 'streamdata': stream_serialized.data})
        else:
            # return HttpResponse("Something Went wrong")
            return render(request, 'Add_stream.html',{'stream_Form':stream_Form})


# -------------------------------- View Stream Data -----------------------------------------------------
class StreamdetailView(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    streamserializers = StreamSerializers

    def get(self, request):
        title = "Stream Data"
        stram = stream.objects.all()
        stream_serialized = self.streamserializers(stram, many=True)
        return render(request, 'stream_detail_view.html', {'title': title, 'streamdata': stream_serialized.data})


# ---------------------------Edit streaam data --------------------------
class streamedit(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    streamserializers = StreamSerializers

    def get(self, request, id):
        title = "Eddit stream"
        stm = get_object_or_404(stream, id=id)
        stream_serialized = self.streamserializers(stm)
        return render(request, 'edit_stream.html', {'title': title, 'stream': stream_serialized.data})

    def post(self, request, id):
        std = get_object_or_404(stream, id=id)
        # ids = student.objects.get(id=id)
        stream_Form = streamForm(request.POST, request.FILES, instance=std)
        print(stream_Form)
        if stream_Form.is_valid():
            post_students_form = stream_Form.save(commit=False)
            post_students_form.save()
            title = "Strean Data"
            stram = stream.objects.all()
            stream_serialized = self.streamserializers(stram, many=True)
            return HttpResponseRedirect('/stream_detail_view', {'title': title, 'streamdata': stream_serialized.data})
        else:
            return HttpResponse("Something Went wrong")


# ---------------------------------------------------- Delete Stream Data -------------------------------------------------
class stream_delete(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    streamserializers = StreamSerializers

    def get(self, request, id):
        data = stream.objects.get(id=id)
        stram = stream.objects.all()
        data.delete()
        title = "Stream Data"
        stram_serialized = self.streamserializers(stram, many=True)
        return HttpResponseRedirect('/stream_detail_view', {'title': title, 'streamdata': stram_serialized.data})


# ---------------------------------- Stream Active Deactive --------------------------
class streamactivation(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    streamserializers = StreamSerializers

    def get(self, request, action, id):
        title = "Stream Data"
        btn = stream.objects.get(id=id)
        if action == 'active' and btn.status == True:
            stream.objects.filter(id=id).update(status=False)
            stram = stream.objects.all()
            stram_serialized = self.streamserializers(stram, many=True)
            return HttpResponseRedirect('/stream_detail_view', {'title': title, 'streamdata': stram_serialized.data})

        elif action == 'deactive' and btn.status == False:
            stream.objects.filter(id=id).update(status=True)
            stram = stream.objects.all()
            stram_serialized = self.streamserializers(stram, many=True)
            return HttpResponseRedirect('/stream_detail_view', {'title': title, 'streamdata': stram_serialized.data})
        else:
            stram = stream.objects.all()
            stram_serialized = self.streamserializers(stram, many=True)
            return HttpResponseRedirect('/stream_detail_view', {'title': title, 'streamdata': stram_serialized.data})


# -----------------------end stream ----------------------------------------------
# ==========================================================================================================================
# ==========================================================================================================================
# ----------------------------------------Add specialization Data------------------------------
class specializationView(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request):
        return render(request, 'Add_specialization.html')

    def post(self, request):
        specialization_Form = specializationForm(request.POST, request.FILES)
        print(specialization_Form)
        if specialization_Form.is_valid():
            name = specialization_Form.cleaned_data['name']
            acronym = specialization_Form.cleaned_data['acronym']
            if specialization.objects.filter(name=name).exists():
                specialization_Form.add_error('name', ' already exists.')
            elif specialization.objects.filter(acronym=acronym).exists():
                specialization_Form.add_error('acronym', ' already exists.')
            else:
                post_specialization_Form = specialization_Form.save(commit=False)
                post_specialization_Form.users = request.user
                post_specialization_Form.save()
                title = "specialization Data"
                da = specialization.objects.all()
                specialization_serialized = SpecializationSerializers(da, many=True)
                return HttpResponseRedirect('/specialization_view',{'title': title, 'spdata': specialization_serialized.data})
            
        return render(request, 'Add_specialization.html', {'specialization_Form': specialization_Form})



# ----------------------------------------View specialization Data------------------------------
class specializationdetailView(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request):
        title = "specialization Data"
        spr = specialization.objects.all()
        specialization_serialized = SpecializationSerializers(spr, many=True)
        return render(request, 'specialization.html', {'title': title, 'spdata': specialization_serialized.data})


# ----------------------------------------Edit specialization Data------------------------------
class specializationedit(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, id):
        title = "Edit Specialization"
        spl = get_object_or_404(specialization, id=id)
        specialization_serialized = SpecializationSerializers(spl)
        return render(request, 'edit_specialization.html', {'title': title, 'spldata': specialization_serialized.data})

    def post(self, request, id):
        std = get_object_or_404(specialization, id=id)
        specialization_Form = specializationForm(request.POST, instance=std)
        print(specialization_Form)
        if specialization_Form.is_valid():
            post_specialization_Form = specialization_Form.save(commit=False)
            post_specialization_Form.save()
            spr = specialization.objects.all()
            specialization_serialized = SpecializationSerializers(spr, many=True)
            title = "specialization Data"
            return HttpResponseRedirect('/specialization_view',
                                        {'title': title, 'spdata': specialization_serialized.data})
        else:
            return HttpResponse("Something Went wrong")


# ----------------------------------------Delete specialization Data------------------------------
class specializationdelete(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, id):
        # std = get_object_or_404(stream, id=id)
        spr = specialization.objects.all()
        data = specialization.objects.get(id=id)
        data.delete()
        title = "specialization Data"
        specialization_serialized = SpecializationSerializers(spr, many=True)
        return HttpResponseRedirect('/specialization_view', {'title': title, 'spdata': specialization_serialized.data})


# ----------------------------------------Active Deactive  specialization Data------------------------------
class specializationactivation(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, action, id):
        spr = specialization.objects.all()
        title = "Specialization Data"
        btn = specialization.objects.get(id=id)
        specialization_serialized = SpecializationSerializers(spr, many=True)
        if action == 'active' and btn.status == True:
            specialization.objects.filter(id=id).update(status=False)
            return HttpResponseRedirect('/specialization_view',
                                        {'title': title, 'spdata': specialization_serialized.data})
        elif action == 'deactive' and btn.status == False:
            specialization.objects.filter(id=id).update(status=True)
            return HttpResponseRedirect('/specialization_view',
                                        {'title': title, 'spdata': specialization_serialized.data})
        else:
            specialization.objects.filter(id=id).update(status=True)
            return HttpResponseRedirect('/specialization_view',
                                        {'title': title, 'spdata': specialization_serialized.data})


# =========================End of Specialaization================================================


# ========================= Level ===================================
# -----------------------------Add Level---------------------------------
class levelView(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request):
        return render(request, 'Add_level.html')

    def post(self, request):
        level_Form = levelForm(request.POST, request.FILES)
        print(levelForm)
        if level_Form.is_valid():
            name=level_Form.cleaned_data['name']
            acronym=level_Form.cleaned_data['acronym']
            if level.objects.filter(name=name).exists():
                level_Form.add_error('name', ' already exists.')
            elif level.objects.filter(acronym=acronym).exists():
                level_Form.add_error('acronym', ' already exists.')
            else:
                post_level_Form = level_Form.save(commit=False)
                post_level_Form.users = request.user
                post_level_Form.save()
                lvl = level.objects.all()
                level_serialized = LevelSerializers(lvl, many=True)
                title = "Strean Data"
                return HttpResponseRedirect('/level_view', {'title': title, 'data': level_serialized.data})
       
        return render(request, 'Add_level.html',{'form':level_Form})


# # ----------------------------------------View Leve Data------------------------------
class levldetailView(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request):
        title = "level Data"
        lvl = level.objects.all()
        level_serialized = LevelSerializers(lvl, many=True)
        return render(request, 'level_detail_view.html', {'title': title, 'data': level_serialized.data})


# # ----------------------------------------Edit Level Data------------------------------
class leveledit(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, id):
        title = "Eddit Level"
        lvl = get_object_or_404(level, id=id)
        level_serialized = LevelSerializers(lvl)
        return render(request, 'edit_level.html', {'title': title, 'leveldata': level_serialized.data})

    def post(self, request, id):
        td = get_object_or_404(level, id=id)
        # ids = student.objects.get(id=id)
        level_Form = levelForm(request.POST, instance=td)
        print(level_Form)
        if level_Form.is_valid():
            post_level_Form = level_Form.save(commit=False)
            post_level_Form.save()
            title = "Strean Data"
            lvl = level.objects.all()
            level_serialized = LevelSerializers(lvl, many=True)
            return HttpResponseRedirect('/level_view', {'title': title, 'data': level_serialized.data})
        else:
            return HttpResponse("Something Went wrong")


# -----------------------------Delete Level Data------------------------------------------------
class level_delete(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, id):
        # std = get_object_or_404(stream, id=id)
        data = level.objects.get(id=id)
        data.delete()
        title = "Level Data"
        lvl = level.objects.all()
        level_serialized = LevelSerializers(lvl, many=True)
        return HttpResponseRedirect('/level_view', {'title': title, 'data': level_serialized.data})


# --------------------------------Activate Deativate Lavel----------------------------------------
class levelactivation(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, action, id):
        title = "Stream Data"
        btn = level.objects.get(id=id)
        lvl = level.objects.all()
        level_serialized = LevelSerializers(lvl, many=True)
        if action == 'active' and btn.status == True:
            level.objects.filter(id=id).update(status=False)
            return HttpResponseRedirect('/level_view', {'title': title, 'data': level_serialized.data})

        elif action == 'deactive' and btn.status == False:
            level.objects.filter(id=id).update(status=True)
            return HttpResponseRedirect('/level_view', {'title': title, 'data': level_serialized.data})
        else:
            return HttpResponseRedirect('/level_view', {'title': title, 'data': level_serialized.data})


# ================================Qualification==================================================
# -----------------------Add Qualification Data---------------------------------------
class qualificationView(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    

    def get(self, request):
        str = stream.objects.all()
        spl = specialization.objects.all()
        lvl = level.objects.all()
        level_serialized = LevelSerializers(lvl, many=True)
        specialization_serialized = SpecializationSerializers(spl, many=True)
        stram_serialized = StreamSerializers(str, many=True)

        return render(request, 'Add_qualification.html', {"stream": stram_serialized.data, 'spl': specialization_serialized.data, 'level': level_serialized.data})

    def post(self, request):
        Qualifications_Form = QualificationsForm(request.POST, request.FILES)
        print(Qualifications_Form)
        if Qualifications_Form.is_valid():
            name=Qualifications_Form.cleaned_data['name']
            acronym=Qualifications_Form.cleaned_data['acronym']
            if Qualifications.objects.filter(name=name).exists():
                Qualifications_Form.add_error('name', ' already exists.')
            elif Qualifications.objects.filter(acronym=acronym).exists():
                Qualifications_Form.add_error('acronym', ' already exists.')
            else:
                post_Qualifications_Form = Qualifications_Form.save(commit=False)
                post_Qualifications_Form.users = request.user
                post_Qualifications_Form.save()
                # return render(request, 'details.html',{'student':data()})
                title = 'Qualification data'
                qpl = Qualifications.objects.all()
                qualification_serialized=QualificationsSerializers(qpl,many=True)
                return HttpResponseRedirect('/qualification_view', {'title': title, 'data': qualification_serialized.data})
        
        str = stream.objects.all()
        spl = specialization.objects.all()
        lvl = level.objects.all()
        level_serialized = LevelSerializers(lvl, many=True)
        specialization_serialized = SpecializationSerializers(spl, many=True)
        stram_serialized = StreamSerializers(str, many=True)
        return render(request, 'Add_qualification.html', {"stream": stram_serialized.data, 'spl': specialization_serialized.data, 'level': level_serialized.data,'form':Qualifications_Form})
    

# ---------------------------------------View Qualification Data---------------------------
class QualificationView(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request):
        title = "Qualification Data"
        # conte
        qlp = Qualifications.objects.all()
        qualification_serialized = QualificationsSerializers(qlp, many=True)
        return render(request, 'qualification_view.html', {'title': title, 'data': qualification_serialized.data})


# -----------------------------------Edit Qualification-------------------------------------------------------
class qualificationedit(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, id):
        title = "Eddit Specialization"
        stram = stream.objects.all()

        qlp = get_object_or_404(Qualifications, id=id)
        spl = specialization.objects.all()
        lvl = level.objects.all()
        stram_serialized = StreamSerializers(stram, many=True)
        level_serialized = LevelSerializers(lvl, many=True)
        specialization_serialized = SpecializationSerializers(spl, many=True)
        qualification_serialized = QualificationsSerializers(qlp)
        return render(request, 'edit_qualification.html',{'title': title, 'qlpdata': qualification_serialized.data, 'stream': stram_serialized.data, 'level': level_serialized.data, 'spl': specialization_serialized.data})

    def post(self, request, id):
        std = get_object_or_404(Qualifications, id=id)
        Qualifications_Form = QualificationsForm(request.POST, request.FILES, instance=std)
        print(Qualifications_Form)
        if Qualifications_Form.is_valid():
            post_Qualifications_Form = Qualifications_Form.save(commit=False)
            post_Qualifications_Form.save()
            # return render(request, 'details.html',{'student':data()})
            title = "Qualification Data"
            qlp = Qualifications.objects.all()
            # qualification_serialized = QualificationsSerializers(qlp)
            return HttpResponseRedirect('/qualification_view')
        else:
            return HttpResponse("Something Went wrong")


# ----------------------------------------Delete Qualification data------------------------------------------
class qualdelete(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, id):
        data = Qualifications.objects.get(id=id)
        data.delete()
        title = "Qualification Data"
        qlp = Qualifications.objects.all()
        return HttpResponseRedirect('/qualification_view')


# -----------------------------------------Active deactive Qualification data------------------------------------------------
class qualificationactivation(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, action, id):
        title = "Qualifications Data"
        btn = Qualifications.objects.get(id=id)
        qlp = Qualifications.objects.all()

        if action == 'active' and btn.status == True:
            Qualifications.objects.filter(id=id).update(status=False)
            return HttpResponseRedirect('/qualification_view')
        elif action == 'deactive' and btn.status == False:
            Qualifications.objects.filter(id=id).update(status=True)
            return HttpResponseRedirect('/qualification_view')
        else:
            return HttpResponseRedirect('/qualification_view')


# -------------------------------------data-fetch-fu-nctions------------------------------------------------
class countryView(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    countryserializers = CountrySerializers

    def get(self, request):
        title = "country"
        return render(request, 'address/Add_country.html')

    def post(self, request):
        country_Form = countryForms(request.POST, request.FILES)
        print(country_Form)
        if country_Form.is_valid():
            name=country_Form.cleaned_data['name']
            acronym=country_Form.cleaned_data['acronym']
            if Country.objects.filter(name=name).exists():
                country_Form.add_error('name', ' already exists.')
            elif Country.objects.filter(acronym=acronym).exists():
                country_Form.add_error('acronym', ' already exists.')
            else:
                post_country_Form = country_Form.save(commit=False)
                post_country_Form.users = request.user
                post_country_Form.save()
                title = "Country Data"
                cd = Country.objects.all()
                Country_serialized = CountrySerializers(cd, many=True)
                return HttpResponseRedirect('/country_view', {'title': title, 'countrydata': Country_serialized.data,'country_Form':country_Form})

        
        return render(request,'address/Add_country.html',{'form':country_Form})

class countrydataView(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request):
        title = "Country Data"
        cd = Country.objects.all()
        Country_serialized = CountrySerializers(cd, many=True)
        return render(request, 'address/Country_view.html', {'title': title, 'countrydata': Country_serialized.data})


class countryedit(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    countryserializers = CountrySerializers

    def get(self, request, id):
        title = "Eddit Country"
        # stm = get_object_or_404(Country, id=id)
        stm = Country.objects.get(id=id)
        Country_serialized = self.countryserializers(stm)
        return render(request, 'address/eddit_Country.html', {'title': title, 'countrydata': Country_serialized.data})

    def post(self, request, id):
        std = get_object_or_404(Country, id=id)
        # ids = student.objects.get(id=id)
        Country_Form = countryForms(request.POST, request.FILES, instance=std)
        print(Country_Form)
        if Country_Form.is_valid():
            post_Country_Form = Country_Form.save(commit=False)
            post_Country_Form.save()
            title = "Country Data"
            cd = Country.objects.all()
            Country_serialized = CountrySerializers(cd, many=True)
            return HttpResponseRedirect('/country_view', {'title': title, 'countrydata': Country_serialized.data})


class Country_delete(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    countryserializers = CountrySerializers

    def get(self, request, id):
        # std = get_object_or_404(stream, id=id)
        data = Country.objects.get(id=id)
        data.delete()
        title = "Country Data"
        cd = Country.objects.all()
        Country_serialized = self.countryserializers(cd, many=True)
        return HttpResponseRedirect('/country_view', {'title': title, 'countrydata': Country_serialized.data})


class Countryactivation(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    countryserializers = CountrySerializers

    def get(self, request, action, id):
        title = "Country Data"
        btn = Country.objects.get(id=id)
        cd = Country.objects.all()
        Country_serialized = self.countryserializers(cd, many=True)

        if action == 'active' and btn.status == True:
            Country.objects.filter(id=id).update(status=False)
            return HttpResponseRedirect('/country_view', {'title': title, 'countrydata': Country_serialized.data})
        elif action == 'deactive' and btn.status == False:
            Country.objects.filter(id=id).update(status=True)
            return HttpResponseRedirect('/country_view', {'title': title, 'countrydata': Country_serialized.data})
        else:
            return HttpResponseRedirect('/country_view', {'title': title, 'countrydata': Country_serialized.data})


class stateView(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request):
        title = "State Data"
        cd = Country.objects.all()
        Country_serialized = CountrySerializers(cd, many=True)
        return render(request, 'address/Add_state.html', {'countrydata': Country_serialized.data})

    def post(self, request):
        state_Form = stateForms(request.POST, request.FILES)
        print(state_Form)
        if state_Form.is_valid():
            name=state_Form.cleaned_data['name']
            acronym=state_Form.cleaned_data['acronym']
            if State.objects.filter(name=name).exists():
                state_Form.add_error('name', ' already exists.')
            elif State.objects.filter(acronym=acronym).exists():
                state_Form.add_error('acronym', ' already exists.')
            else:
                post_state_Form = state_Form.save(commit=False)
                post_state_Form.users = request.user

                post_state_Form.save()
                title = "State Data"
                sd = State.objects.all()
                state_serialized = StateSerializers(sd, many=True)
                return HttpResponseRedirect('/state_view', {'title': title, 'statedata': state_serialized.data,})
            
        
        cd = Country.objects.all()
        Country_serialized = CountrySerializers(cd, many=True)
        return render(request,'address/Add_state.html',{'form':state_Form,'countrydata': Country_serialized.data})


class statedataView(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    # countryserializers = CountrySerializers
    def get(self, request):
        title = "State Data"
        state_records = State.objects.all()
        state_serialized = StateSerializers(state_records, many=True)

        return render(request, 'address/State_view.html', {'title': title, 'statedata': state_serialized.data})


class statedit(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, id):
        title = "Eddit State"
        stm = get_object_or_404(State, id=id)
        cd = Country.objects.all()
        state_serialized = StateSerializers(stm)
        Country_serialized = CountrySerializers(cd, many=True)
        return render(request, 'address/eddit_state.html',
                      {'title': title, 'statedata': state_serialized.data, 'countrydata': Country_serialized.data})

    def post(self, request, id):
        std = get_object_or_404(State, id=id)
        # ids = student.objects.get(id=id)
        State_Form = stateForms(request.POST, request.FILES, instance=std)
        print(State_Form)
        if State_Form.is_valid():
            post_State_Form = State_Form.save(commit=False)
            post_State_Form.save()
            title = "Strean Data"
            sd = State.objects.all()
            state_serialized = StateSerializers(sd, many=True)
            return HttpResponseRedirect('/state_view', {'title': title, 'statedata': state_serialized.data})
            # return HttpResponseRedirect('/')


class State_delete(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, id):
        # std = get_object_or_404(stream, id=id)
        data = State.objects.get(id=id)
        data.delete()
        title = "Country Data"
        sd = State.objects.all()
        state_serialized = StateSerializers(sd, many=True)
        return HttpResponseRedirect('/state_view', {'title': title, 'statedata': state_serialized.data})


class Stateactivation(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, action, id):
        title = "State Data"
        btn = State.objects.get(id=id)
        sd = State.objects.all()
        state_serialized = StateSerializers(sd, many=True)
        if action == 'active' and btn.status == True:
            State.objects.filter(id=id).update(status=False)
            return HttpResponseRedirect('/state_view', {'title': title, 'statedata': state_serialized.data})
        elif action == 'deactive' and btn.status == False:
            State.objects.filter(id=id).update(status=True)
            return HttpResponseRedirect('/state_view', {'title': title, 'statedata': state_serialized.data})
        else:
            return HttpResponseRedirect('/state_view', {'title': title, 'statedata': state_serialized.data})


class distView(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request):
        title = "dist"
        sd = State.objects.all()
        state_serialized = StateSerializers(sd, many=True)
        return render(request, 'address/Add_dist.html', {'statedata': state_serialized.data})

    def post(self, request):
        dist_Form = distForms(request.POST)
        print(dist_Form)
        if dist_Form.is_valid():
            name=dist_Form.cleaned_data['name']
            acronym=dist_Form.cleaned_data['acronym']
            if Dist.objects.filter(name=name).exists():
                dist_Form.add_error('name', ' already exists.')
            elif Dist.objects.filter(acronym=acronym).exists():
                dist_Form.add_error('acronym', ' already exists.')
            else:
                post_dist_Form = dist_Form.save(commit=False)
                post_dist_Form.users = request.user

                post_dist_Form.save()
                title = "District Data"
                dd = Dist.objects.all()
                Dist_serialized = DistSerializers(dd, many=True)
                return HttpResponseRedirect('/dist_view', {'title': title, 'distdata': Dist_serialized.data})
            
        
        sd = State.objects.all()
        state_serialized = StateSerializers(sd, many=True)
        return render(request,'address/Add_dist.html',{'form':dist_Form,'statedata': state_serialized.data})


class distdataView(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request):
        title = "District Data"
        dd = Dist.objects.all()
        Dist_serialized = DistSerializers(dd, many=True)
        return render(request, 'address/District_view.html', {'title': title, 'distdata': Dist_serialized.data})


class distedit(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, id):
        title = "Edit District"
        stm = get_object_or_404(Dist, id=id)
        Dist_serialized = DistSerializers(stm)
        sd = State.objects.all()
        state_serialized = StateSerializers(sd, many=True)
        return render(request, 'address/edit_dist.html',
                      {'title': title, 'distdata': Dist_serialized.data, 'statedata': state_serialized.data})

    def post(self, request, id):
        stm = get_object_or_404(Dist, id=id)
        Dist_serialized = DistSerializers(stm)
        Dist_Form = distForms(request.POST, request.FILES, instance=stm)
        print(Dist_Form)
        if Dist_Form.is_valid():
            post_Dist_Form = Dist_Form.save(commit=False)
            post_Dist_Form.save()
            title = "District Data"
            dd = Dist.objects.all()
            Dist_serialized = DistSerializers(dd, many=True)
            return HttpResponseRedirect('/dist_view', {'title': title, 'distdata': Dist_serialized.data})


class Dist_delete(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, id):
        # std = get_object_or_404(stream, id=id)
        data = Dist.objects.get(id=id)
        data.delete()
        title = "Country Data"
        dd = Dist.objects.all()
        Dist_serialized = DistSerializers(dd, many=True)
        return HttpResponseRedirect('/dist_view', {'title': title, 'distdata': Dist_serialized.data})


class Distactivation(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, action, id):
        title = "Dist Data"
        btn = Dist.objects.get(id=id)
        dd = Dist.objects.all()
        Dist_serialized = DistSerializers(dd, many=True)
        if action == 'active' and btn.status == True:
            Dist.objects.filter(id=id).update(status=False)
            return HttpResponseRedirect('/dist_view', {'title': title, 'distdata': Dist_serialized.data})
        elif action == 'deactive' and btn.status == False:
            Dist.objects.filter(id=id).update(status=True)
            return HttpResponseRedirect('/dist_view', {'title': title, 'distdata': Dist_serialized.data})
        else:
            return HttpResponseRedirect('/dist_view', {'title': title, 'distdata': Dist_serialized.data})


class tallukView(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request):
        title = "talluk"
        dd = Dist.objects.all()
        dist_serialized = DistSerializers(dd, many=True)
        return render(request, 'address/Add_talluk.html', {'distdata': dist_serialized.data})

    def post(self, request):
        talluk_Form = tallukForms(request.POST, request.FILES)
        print(talluk_Form)
        if talluk_Form.is_valid():
            name=talluk_Form.cleaned_data['name']
            acronym=talluk_Form.cleaned_data['acronym']
            if Talluk.objects.filter(name=name).exists():
                talluk_Form.add_error('name', ' already exists.')
            elif Talluk.objects.filter(acronym=acronym).exists():
                talluk_Form.add_error('acronym', ' already exists.')
            else:
                post_talluk_Form = talluk_Form.save(commit=False)
                post_talluk_Form.users = request.user
                post_talluk_Form.save()
                title = "Talluk Data"
                td = Talluk.objects.all()
                talluk_serialized = TallukSerializers(td, many=True)
                return HttpResponseRedirect('/talluk_view', {'title': title, 'tallukdata': talluk_serialized.data})
            
        
        dd = Dist.objects.all()
        dist_serialized = DistSerializers(dd, many=True)
        return render(request,'address/Add_talluk.html',{'form':talluk_Form,'distdata': dist_serialized.data})


class tallukdataView(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request):
        title = "Talluk Data"
        td = Talluk.objects.all()
        talluk_serialized = TallukSerializers(td, many=True)
        return render(request, 'address/Talluk_view.html', {'title': title, 'tallukdata': talluk_serialized.data})


class tallukedit(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, id):
        title = "Edit Talluk"
        dd = Dist.objects.all()
        stm = get_object_or_404(Talluk, id=id)
        talluk_serialized = TallukSerializers(stm)
        Dist_serialized = DistSerializers(dd, many=True)

        return render(request, 'address/edit_talluka.html',
                      {'title': title, 'talluk': talluk_serialized.data, 'distdata': Dist_serialized.data})

    def post(self, request, id):
        std = get_object_or_404(Talluk, id=id)
        # ids = student.objects.get(id=id)
        Talluk_Form = tallukForms(request.POST, request.FILES, instance=std)
        print(Talluk_Form)
        if Talluk_Form.is_valid():
            post_Talluk_Form = Talluk_Form.save(commit=False)
            post_Talluk_Form.save()
            title = "TalLuk Data"
            td = Talluk.objects.all()
            talluk_serialized = TallukSerializers(td, many=True)
            return HttpResponseRedirect('/talluk_view', {'title': title, 'tallukdata': talluk_serialized.data})


class Talluk_delete(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, id):
        # std = get_object_or_404(stream, id=id)
        data = Talluk.objects.get(id=id)
        data.delete()
        title = "Country Data"
        td = Talluk.objects.all()
        talluk_serialized = TallukSerializers(td, many=True)
        return HttpResponseRedirect('/talluk_view', {'title': title, 'tallukdata': talluk_serialized.data})


class Tallukactivation(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, action, id):
        title = "Dist Data"
        btn = Talluk.objects.get(id=id)
        td = Talluk.objects.all()
        talluk_serialized = TallukSerializers(td, many=True)
        if action == 'active' and btn.status == True:
            Talluk.objects.filter(id=id).update(status=False)
            return HttpResponseRedirect('/talluk_view', {'title': title, 'tallukdata': talluk_serialized.data})
        elif action == 'deactive' and btn.status == False:
            Talluk.objects.filter(id=id).update(status=True)
            return HttpResponseRedirect('/talluk_view', {'title': title, 'tallukdata': talluk_serialized.data})
        else:
            return HttpResponseRedirect('/talluk_view', {'title': title, 'tallukdata': talluk_serialized.data})


class cityView(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request):
        title = "city"
        dd = Dist.objects.all()
        Dist_serialized = DistSerializers(dd, many=True)
        td = Talluk.objects.all()
        talluk_serialized = TallukSerializers(td, many=True)
        return render(request, 'address/Add_city.html',
                      {'tallukdata': talluk_serialized.data, 'distdata': Dist_serialized.data})

    def post(self, request):
        city_Form = cityForms(request.POST, request.FILES)
        print(city_Form)
        if city_Form.is_valid():
            name=city_Form.cleaned_data['name']
            acronym=city_Form.cleaned_data['acronym']
            if City.objects.filter(name=name).exists():
                city_Form.add_error('name', ' already exists.')
            elif City.objects.filter(acronym=acronym).exists():
                city_Form.add_error('acronym', ' already exists.')
            else:
                post_city_Form = city_Form.save(commit=False)
                post_city_Form.users = request.user
                post_city_Form.save()
                title = "City Data"
                ct = City.objects.all()
                citt_serialized = CitySerializers(ct, many=True)
                return HttpResponseRedirect('/city_view', {'title': title, 'citydata': citt_serialized.data})

        
        dd = Dist.objects.all()
        Dist_serialized = DistSerializers(dd, many=True)
        td = Talluk.objects.all()
        talluk_serialized = TallukSerializers(td, many=True)
        return render(request,'address/Add_city.html',{'form':city_Form,'tallukdata': talluk_serialized.data, 'distdata': Dist_serialized.data})

class citydataView(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request):
        title = "City Data"
        ct = City.objects.all()
        citt_serialized = CitySerializers(ct, many=True)
        return render(request, 'address/City_view.html', {'title': title, 'citydata': citt_serialized.data})


class cityedit(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, id):
        title = "Edit City"
        stm = get_object_or_404(City, id=id)
        citt_serialized = CitySerializers(stm)
        dd = Dist.objects.all()
        Dist_serialized = DistSerializers(dd, many=True)
        td = Talluk.objects.all()
        talluk_serialized = TallukSerializers(td, many=True)
        return render(request, 'address/edit_city.html',
                      {'title': title, 'citydata': citt_serialized.data, 'distdata': Dist_serialized.data,
                       'tallukdata': talluk_serialized.data})

    def post(self, request, id):
        std = get_object_or_404(City, id=id)
        # ids = student.objects.get(id=id)
        city_Form = cityForms(request.POST, request.FILES, instance=std)
        print(city_Form)
        if city_Form.is_valid():
            post_city_Form = city_Form.save(commit=False)
            post_city_Form.save()
            title = "TalLuk Data"
            return HttpResponseRedirect('/city_view')


class City_delete(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, id):
        # std = get_object_or_404(stream, id=id)
        data = City.objects.get(id=id)
        data.delete()
        ct = City.objects.all()
        return HttpResponseRedirect('/city_view')


class cityactivation(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, action, id):
        btn = City.objects.get(id=id)
        ct = City.objects.all()
        if action == 'active' and btn.status == True:
            City.objects.filter(id=id).update(status=False)
            return HttpResponseRedirect('/city_view')
        elif action == 'deactive' and btn.status == False:
            City.objects.filter(id=id).update(status=True)
            return HttpResponseRedirect('/city_view')
        else:
            return HttpResponseRedirect('/city_view')


class pincodeView(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request):
        title = "pincode"
        ct = City.objects.all()
        city_serialized = CitySerializers(ct, many=True)
        return render(request, 'address/Add_pincode.html', {'citydata': city_serialized.data})

    def post(self, request):
        Pincode_Form = PinForms(request.POST, request.FILES)
        print(Pincode_Form)
        if Pincode_Form.is_valid():
            name=Pincode_Form.cleaned_data['pincode']
            # acronym=Pincode_Form.cleaned_data['acronym']
            if Pincode.objects.filter(pincode=name).exists():
                Pincode_Form.add_error('pincode', ' already exists.')
            # elif Pincode.objects.filter(acronym=acronym).exists():
                # Pincode_Form.add_error('acronym', ' already exists.')
            else:
                post_Pincode_Form = Pincode_Form.save(commit=False)
                post_Pincode_Form.users = request.user
                post_Pincode_Form.save()
                title = "Pincode Data"
                pd = Pincode.objects.all()
                pincode_serialized = PincodeSerializers(pd, many=True)
                return HttpResponseRedirect('/pincode_view', {'title': title, 'pincodedata': pincode_serialized.data})
        
        ct = City.objects.all()
        city_serialized = CitySerializers(ct, many=True)
        return render(request,'address/Add_pincode.html',{'form':Pincode_Form,'citydata': city_serialized.data})


class pincodedataView(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request):
        title = "pincode"
        title = "PIncode Data"
        pd = Pincode.objects.all()
        pincode_serialized = PincodeSerializers(pd, many=True)
        return render(request, 'address/Pincod_view.html', {'title': title, 'pincodedata': pincode_serialized.data})


class Pincodeedit(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, id):
        title = "Edit Pincode"
        stm = get_object_or_404(Pincode, id=id)
        ct = City.objects.all()
        pincode_serialized = PincodeSerializers(stm)
        city_serialized = CitySerializers(ct, many=True)
        return render(request, 'address/edit_pincode.html',
                      {'title': title, 'pincode': pincode_serialized.data, 'citydata': city_serialized.data})

    def post(self, request, id):
        std = get_object_or_404(Pincode, id=id)
        # ids = student.objects.get(id=id)
        Pincode_Form = PinForms(request.POST, request.FILES, instance=std)
        print(Pincode_Form)
        if Pincode_Form.is_valid():
            post_Pincode_Form = Pincode_Form.save(commit=False)
            post_Pincode_Form.save()
            title = "Pincode Data"
            pd = Pincode.objects.all()
            pincode_serialized = PincodeSerializers(pd, many=True)
            return HttpResponseRedirect('/pincode_view', {'title': title, 'pincodedata': pincode_serialized.data})


class Pincode_delete(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, id):
        # std = get_object_or_404(stream, id=id)
        data = Pincode.objects.get(id=id)
        data.delete()
        title = "Country Data"
        pd = Pincode.objects.all()
        pincode_serialized = PincodeSerializers(pd, many=True)
        return HttpResponseRedirect('/pincode_view', {'title': title, 'pincodedata': pincode_serialized.data})


class pincodeactivation(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, action, id):
        title = "Pincode Data"
        btn = Pincode.objects.get(id=id)
        pd = Pincode.objects.all()
        pincode_serialized = PincodeSerializers(pd, many=True)

        if action == 'active' and btn.status == True:
            Pincode.objects.filter(id=id).update(status=False)
            return HttpResponseRedirect('/pincode_view', {'title': title, 'pincodedata': pincode_serialized.data})
        elif action == 'deactive' and btn.status == False:
            Pincode.objects.filter(id=id).update(status=True)
            return HttpResponseRedirect('/pincode_view', {'title': title, 'pincodedata': pincode_serialized.data})
        else:
            return HttpResponseRedirect('/pincode_view', {'title': title, 'pincodedata': pincode_serialized.data})


# -------------------------------------------------------------Medium and Languge add functions---------------------------------------------------------
class mediumView(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request):
        return render(request, 'Mediam_and_Languge/Add_medium.html')

    def post(self, request):
        medium_Form = MediumForms(request.POST, request.FILES)
        # print(medium_Form)

        if medium_Form.is_valid():
            name=medium_Form.cleaned_data['name']
            acronym=medium_Form.cleaned_data['acronym']
            if medium.objects.filter(name=name).exists():
                medium_Form.add_error('name', ' already exists.')
            elif medium.objects.filter(acronym=acronym).exists():
                medium_Form.add_error('acronym', ' already exists.')
            else:
                post_medium_Form = medium_Form.save(commit=False)
                post_medium_Form.users = request.user
                post_medium_Form.save()
                title = "Medium Data"
                mediumdata = medium.objects.all()
                # medium_serialized=mediumSerializers(mediumdata,many=True)
                return HttpResponseRedirect('/view_medium')
        
        return render(request,'Mediam_and_Languge/Add_medium.html',{'form':medium_Form})


class medium_data_View(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request):
        title = "Medium Data"
        md = medium.objects.all()
        medium_serialized = mediumSerializers(md, many=True)
        return render(request, 'Mediam_and_Languge/medium_view.html',
                      {'title': title, 'mediumdata': medium_serialized.data})


class medium_edit(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, id):
        title = "Edit Medium"
        stm = get_object_or_404(medium, id=id)
        medium_serialized = mediumSerializers(stm)
        return render(request, 'Mediam_and_Languge/edit_medium.html',
                      {'title': title, 'mediumdata': medium_serialized.data})

    def post(self, request, id):
        std = get_object_or_404(medium, id=id)
        medium_Form = MediumForms(request.POST, request.FILES, instance=std)
        if medium_Form.is_valid():
            post_medium_Form = medium_Form.save(commit=False)
            post_medium_Form.save()
            return HttpResponseRedirect('/view_medium')


class medium_delete(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, id):
        data = medium.objects.get(id=id)
        data.delete()
        title = "Medium Data"
        return HttpResponseRedirect('/view_medium')


class mediumactivation(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, action, id):
        title = "Pincode Data"
        btn = medium.objects.get(id=id)
        pd = medium.objects.all()
        medium_serialized = mediumSerializers(pd, many=True)

        if action == 'active' and btn.status == True:
            medium.objects.filter(id=id).update(status=False)
            return HttpResponseRedirect('/view_medium')
        elif action == 'deactive' and btn.status == False:
            medium.objects.filter(id=id).update(status=True)
            return HttpResponseRedirect('/view_medium')
        else:
            return HttpResponseRedirect('/view_medium')


class langView(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request):
        return render(request, 'Mediam_and_Languge/Add_languge.html')

    def post(self, request):
        languge_Form = LagngugeForms(request.POST, request.FILES)
        if languge_Form.is_valid():
            name=languge_Form.cleaned_data['name']
            acronym=languge_Form.cleaned_data['acronym']
            if Languge.objects.filter(name=name).exists():
                languge_Form.add_error('name', ' already exists.')
            elif Languge.objects.filter(acronym=acronym).exists():
                languge_Form.add_error('acronym', ' already exists.')
            else:
                post_languge_Form = languge_Form.save(commit=False)
                post_languge_Form.users = request.user
                post_languge_Form.save()
                title = "Languge Data"
                ld = Languge.objects.all()
                languge_serialized = LangugeSerializers(ld, many=True)
                return HttpResponseRedirect('/view_Languge', {'title': title, 'langdata': languge_serialized.data})

       
        return render(request,'Mediam_and_Languge/Add_languge.html',{'form':languge_Form})

class lang_data_View( View):
    # login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request):
        title = "Languge Data"
        ld = Languge.objects.all()
        languge_serialized = LangugeSerializers(ld, many=True)
        return render(request, 'Mediam_and_Languge/languge_view.html',
                      {'title': title, 'langdata': languge_serialized.data})


class lang_edit(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, id):
        title = "Edit Medium"
        stm = get_object_or_404(Languge, id=id)
        languge_serialized = LangugeSerializers(stm)
        return render(request, 'Mediam_and_Languge/edit_languge.html',
                      {'title': title, 'langdata': languge_serialized.data})

    def post(self, request, id):
        std = get_object_or_404(Languge, id=id)
        # ids = student.objects.get(id=id)
        lang_Form = LagngugeForms(request.POST, request.FILES, instance=std)
        # print(medium_Form)
        if lang_Form.is_valid():
            post_lang_Form = lang_Form.save(commit=False)
            post_lang_Form.save()
            title = "Languge Data"
            ld = Languge.objects.all()
            languge_serialized = LangugeSerializers(ld, many=True)
            return HttpResponseRedirect('/view_Languge', {'title': title, 'langdata': languge_serialized.data})


class lang_delete(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, id):
        # std = get_object_or_404(stream, id=id)
        data = Languge.objects.get(id=id)
        data.delete()
        return HttpResponseRedirect('/view_Languge')


class langugeactivation(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, action, id):
        btn = Languge.objects.get(id=id)
        pd = Languge.objects.all()

        if action == 'active' and btn.status == True:
            Languge.objects.filter(id=id).update(status=False)
            return HttpResponseRedirect('/view_Languge')
        elif action == 'deactive' and btn.status == False:
            Languge.objects.filter(id=id).update(status=True)
            return HttpResponseRedirect('/view_Languge')
        else:
            return HttpResponseRedirect('/view_Languge')


class religionView(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request):
        return render(request, 'caste/Add_religion.html')

    def post(self, request):
        religion_Form = Religionforms(request.POST, request.FILES)
        # print(medium_Form)
        if religion_Form.is_valid():
            name=religion_Form.cleaned_data['religion_code']
            acronym=religion_Form.cleaned_data['religion_name']
            if Religion.objects.filter(religion_code=name).exists():
                religion_Form.add_error('religion_code', ' already exists.')
            elif Religion.objects.filter(religion_name=acronym).exists():
                religion_Form.add_error('religion_name', ' already exists.')
            else:
                post_religion_Form = religion_Form.save(commit=False)
                post_religion_Form.users = request.user
                post_religion_Form.save()
                rd = Religion.objects.all()
                Religion_Serialized = ReligionSerializers(rd, many=True)
                title = "Religion Data"
                return HttpResponseRedirect('/view_Religion', {'title': title, 'reldata': Religion_Serialized.data})

        
        return render(request,'caste/Add_religion.html',{'form':religion_Form})

class religiondata(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request):
        titile = 'religion'
        religiondata = Religion.objects.all()
        Religion_Serialized = ReligionSerializers(religiondata, many=True)
        return render(request, 'caste/religion_view.html', {'titile': titile, 'reldata': Religion_Serialized.data})


class religiondata_edit(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, id):
        titile = "Edit Religion"
        stm = get_object_or_404(Religion, id=id)
        Religion_Serialized = ReligionSerializers(stm)
        return render(request, 'caste/Edit_religion.html', {'titile': titile, 'reldata': Religion_Serialized.data})

    def post(self, request, id):
        td = get_object_or_404(Religion, id=id)
        form = Religionforms(request.POST, instance=td)
        print(form)
        if form.is_valid():
            post_form = form.save(commit=False)
            post_form.save()
            rd = Religion.objects.all()
            title = "Religion Data"
            Religion_Serialized = ReligionSerializers(rd, many=True)
            return HttpResponseRedirect('/view_Religion', {'title': title, 'reldata': Religion_Serialized.data})


class Religion_delete(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, id):
        data = Religion.objects.get(id=id)
        data.delete()
        religiondata = Religion.objects.all()
        title = "Religion Data"
        return HttpResponseRedirect('/view_Religion')


class Religion_activation(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, action, id):
        btn = Religion.objects.get(id=id)
        pd = Religion.objects.all()
        if action == 'active' and btn.status == True:
            Religion.objects.filter(id=id).update(status=False)
            return HttpResponseRedirect('/view_Religion')
        elif action == 'deactive' and btn.status == False:
            Religion.objects.filter(id=id).update(status=True)
            return HttpResponseRedirect('/view_Religion')
        else:
            return HttpResponseRedirect('/view_Religion')


class casteView(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request):
        titile = 'caste'
        religiondata = Religion.objects.all()
        Religion_Serialized = ReligionSerializers(religiondata, many=True)
        return render(request, 'caste/Add_caste.html', {'title': titile, 'reldata': Religion_Serialized.data})

    def post(self, request):
        caste_Form = CasteForms(request.POST, request.FILES)
        if caste_Form.is_valid():
            name=caste_Form.cleaned_data['caste_code']
            acronym=caste_Form.cleaned_data['caste_name']
            if Caste.objects.filter(caste_code=name).exists():
                caste_Form.add_error('caste_code', ' already exists.')
            elif Caste.objects.filter(caste_name=acronym).exists():
                caste_Form.add_error('caste_name', ' already exists.')
            else:
                post_caste_Form = caste_Form.save(commit=False)
                post_caste_Form.users = request.user
                post_caste_Form.save()
                cd = Caste.objects.all()
                rd = Religion.objects.all()
                title = 'Caste data'
                return HttpResponseRedirect('/view_Caste')

        
        titile = 'caste'
        religiondata = Religion.objects.all()
        Religion_Serialized = ReligionSerializers(religiondata, many=True)
        return render(request,'caste/Add_caste.html',{'form':caste_Form,'title': titile, 'reldata': Religion_Serialized.data})

class castedata(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request):
        title = 'Caste'
        castedata = Caste.objects.all()
        caste_Serialized=CasteSerializers(castedata,many=True)
        # rd = Religion.objects.all()
        
        return render(request, 'caste/caste_view.html', {'title': title, 'castedata': caste_Serialized.data})


class Castedata_edit(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, id):
        title = "Edit Talluk"
        stm = get_object_or_404(Caste, id=id)
        caste_Serialized=CasteSerializers(stm)
        rd = Religion.objects.all()
        Religion_Serialized = ReligionSerializers(rd, many=True)
        return render(request, 'caste/Edit_caste.html', {'title': title, 'castedata': caste_Serialized.data, 'reldata': Religion_Serialized.data})

    def post(self, request, id):
        # std = get_object_or_404(Caste, id=id)
        std = Caste.objects.get(id=id)
        _Form = CasteForms(request.POST, request.FILES, instance=std)
        cd = Caste.objects.all()

        title = "Caste Data"
        print(_Form)
        if _Form.is_valid():
            post_Form = _Form.save(commit=False)
            post_Form.save()
            cd = Caste.objects.all()
            return HttpResponseRedirect('/view_Caste')


class Caste_delete(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(request, id):
        # std = get_object_or_404(stream, id=id)
        data = Caste.objects.get(id=id)
        data.delete()
        title = 'Caste Data'
        cd = Caste.objects.all()
        rd = Religion.objects.all()
        return HttpResponseRedirect('/view_Caste')


class Caste_activation(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(request, action, id):
        title = "religion Data"
        btn = Caste.objects.get(id=id)
        rd = Religion.objects.all()
        cd = Caste.objects.all()
        if action == 'active' and btn.status == True:
            Caste.objects.filter(id=id).update(status=False)
            return HttpResponseRedirect('/view_Caste')
        elif action == 'deactive' and btn.status == False:
            Caste.objects.filter(id=id).update(status=True)
            return HttpResponseRedirect('/view_Caste')
        else:
            return HttpResponseRedirect('/view_Caste')


class subcasteView(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request):
        titile = 'Subcaste'
        castedata = Caste.objects.all()
        caste_Serialized=CasteSerializers(castedata,many=True)
        return render(request, 'caste/Add_subcaste.html', {'title': titile, 'castedata': caste_Serialized.data})
        # return HttpResponseRedirect('view_Subcaste')

    def post(self, request):
        title = 'SubCaste Data'
        # subcaste=Subcaste.objects.all()
        subcaste_Form = SubcasteForms(request.POST, request.FILES)
        if subcaste_Form.is_valid():
            name=subcaste_Form.cleaned_data['subcaste_name']
            acronym=subcaste_Form.cleaned_data['subcaste_code']
            if Subcaste.objects.filter(subcaste_name=name).exists():
                subcaste_Form.add_error('subcaste_name', ' already exists.')
            elif Subcaste.objects.filter(subcaste_code=acronym).exists():
                subcaste_Form.add_error('subcaste_code', ' already exists.')
            else:
                post_subcaste_Form = subcaste_Form.save(commit=False)
                post_subcaste_Form.users = request.user
                post_subcaste_Form.save()
                scd = Subcaste.objects.all()
                return HttpResponseRedirect('/view_Subcaste')
        
        castedata = Caste.objects.all()
        caste_Serialized=CasteSerializers(castedata,many=True)
        return render(request,'caste/Add_subcaste.html',{'form':subcaste_Form,'castedata': caste_Serialized.data})

class subcastedata(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request):
        title = 'SubCaste'
        subcastedata = Subcaste.objects.all()
        subcaste_serialized=SubcasteSerializers(subcastedata,many=True)
        return render(request, 'caste/subcaste_view.html', {'title': title, 'subcastedata': subcaste_serialized.data})


class subcastedata_edit(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, id):
        title = 'Sub Caste'
        stm = get_object_or_404(Subcaste, id=id)
        subcaste_serialized=SubcasteSerializers(stm)
        # subcastedata = Subcaste.objects.all()
        castedata = Caste.objects.all()
        caste_Serialized=CasteSerializers(castedata)
        return render(request, 'caste/Edit_subcaste.html', {'title': title, 'subcastedata': subcaste_serialized.data, 'castedata': caste_Serialized.data})

    def post(self, request, id):
        td = get_object_or_404(Subcaste, id=id)
        form = SubcasteForms(request.POST, instance=td)
        print(form)
        if form.is_valid():
            post_form = form.save(commit=False)
            post_form.save()
            title = "Sub Caste Data"
            scd = Subcaste.objects.all()
            return HttpResponseRedirect('/view_Subcaste')


class SubCaste_delete(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(request, id):
        std = get_object_or_404(stream, id=id)
        data = Subcaste.objects.get(id=id)
        data.delete()
        title = 'SubCaste'
        scd = Subcaste.objects.all()
        return HttpResponseRedirect('/view_Subcaste')


class Subcaste_activation(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(request, action, id):
        title = "Subcaste Data"
        btn = Subcaste.objects.get(id=id)
        scd = Subcaste.objects.all()
        if action == 'active' and btn.status == True:
            Subcaste.objects.filter(id=id).update(status=False)
            return HttpResponseRedirect('/view_Subcaste')

        elif action == 'deactive' and btn.status == False:
            Subcaste.objects.filter(id=id).update(status=True)
            return HttpResponseRedirect('/view_Subcaste')
        else:
            return HttpResponseRedirect('/view_Subcaste')





class designationView(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request):
        return render(request, 'Add_Designation.html')

    def post(self, request):
        title = 'Designation Data'
        form = DesignationForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            acronym=form.cleaned_data['acronym']
            if Designation.objects.filter(name=name).exists():
                form.add_error('name', ' already exists.')
            elif Designation.objects.filter(acronym=acronym).exists():
                form.add_error('acronym', ' already exists.')
            else:

                post_form = form.save(commit=False)
                post_form.users = request.user
                post_form.save()
                data = Designation.objects.all()
                designation_serialized=DesignationSerializers(data,many=True)
                return HttpResponseRedirect('/View_Designation', {'title': title, 'designationdata': designation_serialized.data})
            
        
        return render(request,'Add_Designation.html',{'form':form})


class designation_data_view(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request):
        title = "Designation Data"
        data = Designation.objects.all()
        designation_serialized = DesignationSerializers(data, many=True)
        return render(request, 'View_Designation.html', {'title': title, 'designationdata': designation_serialized.data})


class designationEdit(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, id):
        title = "Edit Medium"
        stm = get_object_or_404(Designation, id=id)
        designation_serialized = DesignationSerializers(stm)
        return render(request, 'edit_designation.html', {'title': title, 'designationdata': designation_serialized.data})

    def post(self, request, id):
        std = get_object_or_404(Designation, id=id)
        # ids = student.objects.get(id=id)
        form = DesignationForm(request.POST, request.FILES, instance=std)
        # print(medium_Form)
        if form.is_valid():
            post_form = form.save(commit=False)
            post_form.save()
            title = "Designation Data Data"
            data = Designation.objects.all()
            designation_serialized = DesignationSerializers(data, many=True)
            return HttpResponseRedirect('/View_Designation', {'title': title, 'designationdata': designation_serialized.data})


class designation_delete(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self,request, id):
        data = Designation.objects.get(id=id)
        data.delete()
        title = "Designation Data Data"
        data = Designation.objects.all()
        return HttpResponseRedirect('/View_Designation')


class Designationactivation(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self,request, action, id):
        title = "Designation Data"
        btn = Designation.objects.get(id=id)
        data = Designation.objects.all()
        if action == 'active' and btn.status == True:
            Designation.objects.filter(id=id).update(status=False)
            return HttpResponseRedirect('/View_Designation')
        elif action == 'deactive' and btn.status == False:
            Designation.objects.filter(id=id).update(status=True)
            return HttpResponseRedirect('/View_Designation')
        else:
            return HttpResponseRedirect('/View_Designation')


# ===================================Commitee================================================================================

class View_Add_Committe(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request):
        return render(request, 'Add_committe.html')

    def post(self, request):
        title = 'Designation Data'
        form = CommitteForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            acronym=form.cleaned_data['acronym']
            if Committe.objects.filter(name=name).exists():
                form.add_error('name', ' already exists.')
            elif Committe.objects.filter(acronym=acronym).exists():
                form.add_error('acronym', ' already exists.')
            else:
                post_form = form.save(commit=False)
                post_form.users = request.user
                post_form.save()
                data = Committe.objects.all()
                committe_serialized=CommitteSerializers(data,many=True)
                return HttpResponseRedirect('/View_Committe', {'title': title, 'view_committe': committe_serialized.data})
            
        
        return render(request,'Add_committe.html',{'form':form})


class committe_data_view(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request):
        title = "Committe Data"
        data = Committe.objects.all()
        committe_serialized = CommitteSerializers(data, many=True)
        return render(request, 'view_committe.html', {'title': title, 'view_committe': committe_serialized.data})


class Edit_Committe(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, id):
        title = "Edit Committe"
        stm = get_object_or_404(Committe, id=id)
        committe_serialized = CommitteSerializers(stm)
        return render(request, 'edit_Committe.html', {'title': title, 'committedata': committe_serialized.data})

    def post(self, request, id):
        std = get_object_or_404(Committe, id=id)
        # ids = student.objects.get(id=id)
        form = CommitteForm(request.POST, request.FILES, instance=std)
        # print(medium_Form)
        if form.is_valid():
            post_form = form.save(commit=False)
            post_form.save()
            title = "Committe Data"
            data = Committe.objects.all()
            committe_serialized = CommitteSerializers(data,many=True)
            return render(request, 'view_committe.html', {'title': title, 'view_committe': committe_serialized.data})


class delete_committe(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self,request, id):
        data = Committe.objects.get(id=id)
        data.delete()
        title = "Committe Data"
        # data = Committe.objects.all()
        return HttpResponseRedirect('/View_Committe')


class Committe_activation(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    def get(self,request, action, id):
        title = "Committe Data"
        btn = Committe.objects.get(id=id)
        # data = Committe.objects.all()
        if action == 'active' and btn.status == True:
            Committe.objects.filter(id=id).update(status=False)
            return HttpResponseRedirect('/View_Committe')
        elif action == 'deactive' and btn.status == False:
            Committe.objects.filter(id=id).update(status=True)
            return HttpResponseRedirect('/View_Committe')
        else:
            return HttpResponseRedirect('/View_Committe')


# =================================View-Catogory=======================================================================

class View_Add_Catogory(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request):
        return render(request, 'Add_fee_cat.html')

    def post(self, request):
        title = 'Fee Catogory Data'
        form = FeeCategoryForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            acronym=form.cleaned_data['acronym']
            if FeeCategory.objects.filter(name=name).exists():
                form.add_error('name', ' already exists.')
            elif FeeCategory.objects.filter(acronym=acronym).exists():
                form.add_error('acronym', ' already exists.')
            else:
                post_form = form.save(commit=False)
                post_form.users = request.user
                post_form.save()
                data = FeeCategory.objects.all()
                feecatgory_serialized=FeeCategorySerializers(data,many=True)
                return HttpResponseRedirect('/View_fee_catogory', {'title': title, 'view_feecat': feecatgory_serialized.data})
        
        return render(request,'Add_fee_cat.html',{'form':form})


class Fee_cat_data_view(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request):
        title = "Fee Catogory Data"
        data = FeeCategory.objects.all()
        feecatgory_serialized=FeeCategorySerializers(data,many=True)
        return render(request, 'View_fee_cat.html', {'title': title, 'view_feecat': feecatgory_serialized.data})


class EditFeeCatogory(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, id):
        title = "Edit Fee Catogory"
        stm = get_object_or_404(FeeCategory, id=id)
        feecatgory_serialized=FeeCategorySerializers(stm)
        return render(request, 'Edit_fee_catogory.html', {'title': title, 'feedata': feecatgory_serialized.data})

    def post(self, request, id):
        std = get_object_or_404(FeeCategory, id=id)
        # ids = student.objects.get(id=id)
        form = FeeCategoryForm(request.POST, request.FILES, instance=std)
        # print(medium_Form)
        if form.is_valid():
            post_form = form.save(commit=False)
            post_form.save()
            data = FeeCategory.objects.all()
            committe_serialized = CommitteSerializers(data,many=True)
            return HttpResponseRedirect('/View_fee_catogory')


class delete_FeeCatogory(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self,request, id):
        data = FeeCategory.objects.get(id=id)
        data.delete()
        return HttpResponseRedirect('/View_fee_catogory')


class Fee_cat_Activation(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    def get(self,request, action, id):
        btn = FeeCategory.objects.get(id=id)
        if action == 'active' and btn.status == True:
            FeeCategory.objects.filter(id=id).update(status=False)
            return HttpResponseRedirect('/View_fee_catogory')
        elif action == 'deactive' and btn.status == False:
            FeeCategory.objects.filter(id=id).update(status=True)
            return HttpResponseRedirect('/View_fee_catogory')
        else:
            return HttpResponseRedirect('/View_fee_catogory')
        



class Add_EntryType(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request):
        return render(request, 'Add_entrytype.html')

    def post(self, request):
        title = 'Entry type Data'
        form = EntryTypeForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            acronym=form.cleaned_data['acronym']
            if EntryType.objects.filter(name=name).exists():
                form.add_error('name', ' already exists.')
            elif EntryType.objects.filter(acronym=acronym).exists():
                form.add_error('acronym', ' already exists.')
            else:
                post_form = form.save(commit=False)
                post_form.users = request.user
                post_form.save()
                data = EntryType.objects.all()
                EntryType_serialized=EntryTypeSerializers(data,many=True)
                return HttpResponseRedirect('/View_Entry_type', {'title': title, 'Entry_data': EntryType_serialized.data})
            
        
        return render(request,'Add_entrytype.html',{'form':form})


class Entrytype_data_view(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request):
        title = "Entry type Data"
        data = EntryType.objects.all()
        EntryType_serialized=EntryTypeSerializers(data,many=True)
        return render(request, 'view_entrytype.html', {'title': title, 'Entry_data': EntryType_serialized.data})


class editEntrytype(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, id):
        title = "entry type"
        stm = get_object_or_404(EntryType, id=id)
        EntryType_serialized=EntryTypeSerializers(stm)
        return render(request, 'edit_entrytype.html', {'title': title, 'entrydata': EntryType_serialized.data})

    def post(self, request, id):
        std = get_object_or_404(EntryType, id=id)
        # ids = student.objects.get(id=id)
        form = EntryTypeForm(request.POST, request.FILES, instance=std)
        # print(medium_Form)
        if form.is_valid():
            post_form = form.save(commit=False)
            post_form.save()
            data = EntryType.objects.all()
            EntryType_serialized = EntryTypeSerializers(data,many=True)
            return HttpResponseRedirect('/View_Entry_type')

#
class delete_EntryType(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self,request, id):
        data = EntryType.objects.get(id=id)
        data.delete()
        return HttpResponseRedirect('/View_Entry_type')
#
#
class Entry_type_Activation(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    def get(self,request, action, id):
        btn = EntryType.objects.get(id=id)
        if action == 'active' and btn.status == True:
            EntryType.objects.filter(id=id).update(status=False)
            return HttpResponseRedirect('/View_Entry_type')
        elif action == 'deactive' and btn.status == False:
            EntryType.objects.filter(id=id).update(status=True)
            return HttpResponseRedirect('/View_Entry_type')
        else:
            return HttpResponseRedirect('/View_Entry_type')
from django.contrib import admin
from django.urls import path, include

from app import views
#

app_name = 'app'
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('',include('app.urls')),
    path('',views.Login.as_view()),
    path('logout/login/',views.Login.as_view(),name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('index/',views.indexView.as_view(),name='index'),
    path('Add_stream/',views.streamView.as_view(), name='Add_stream'),
    path('Add_level/',views.levelView.as_view(), name='Add_level'),
    path('Add_specialization/',views.specializationView.as_view(), name='Add_specialization'),
    path('Add_qualification/',views.qualificationView.as_view(), name='Add_qualification'),

    path('stream_detail_view/',views.StreamdetailView.as_view(), name="stream_detail_view"),
    path('specialization_view/',views.specializationdetailView.as_view(), name='specialization_view'),
    path('qualification_view/',views.QualificationView.as_view(), name='qualification_view'),
    path('level_view/',views.levldetailView.as_view(), name='level_view'),
    path('edit_stream/<int:id>',views.streamedit.as_view(),name='edit_stream'),
    path('edit_level/<int:id>',views.leveledit.as_view(),name='edit_level'),
    path('edit_specialization/<int:id>',views.specializationedit.as_view(),name='edit_specialization'),
    path('edit_qualification/<int:id>',views.qualificationedit.as_view(),name='edit_qualification'),
    path('delete_qualification/<int:id>',views.qualdelete.as_view(),name='delete_qualification'),
    path('delete_spacialization/<int:id>',views.specializationdelete.as_view(),name='delete_spacialization'),
    path('delete_leve/<int:id>',views.level_delete.as_view(),name='delete_leve'),
    path('delete_stream/<int:id>',views.stream_delete.as_view(),name='delete_stream'),
    path('update_stream/<str:action>/<int:id>',views.streamactivation.as_view(),name='update_stream'),
    path('update_level/<str:action>/<int:id>',views.levelactivation.as_view(),name='update_level'),
    path('update_specilaization/<str:action>/<int:id>',views.specializationactivation.as_view(),name='update_specilaization'),
    path('update_qualification/<str:action>/<int:id>',views.qualificationactivation.as_view(),name='update_qualification'),


#     path('delete/<int:id>',views.delet_data.as_view(),name='delete'),
#---------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------

    path('Add_country/',views.countryView.as_view(), name='Add_country'),
    path('Add_state/',views.stateView.as_view(), name='Add_state'),
    path('Add_dist/',views.distView.as_view(), name='Add_dist'),
    path('Add_talluk/',views.tallukView.as_view(), name='Add_talluk'),
    path('Add_city/',views.cityView.as_view(), name='Add_city'),
    path('Add_pincode/',views.pincodeView.as_view(), name='Add_pincode'),
#-------------------------------------view-page-----------------------------------------------------------------
    path('country_view/',views.countrydataView.as_view(), name='country_view'),
    path('state_view/',views.statedataView.as_view(), name='state_view'),
    path('dist_view/',views.distdataView.as_view(), name='dist_view'),
    path('talluk_view/',views.tallukdataView.as_view(), name='talluk_view'),
    path('city_view/',views.citydataView.as_view(), name='city_view'),
    path('pincode_view/',views.pincodedataView.as_view(), name='pincode_view'),
#-------------------------------------------Edit-page------------------------------------------------------------------------------------------
    path('edit_country/<int:id>',views.countryedit.as_view(),name='edit_country'),
    path('edit_State/<int:id>',views.statedit.as_view(),name='edit_State'),
    path('edit_District/<int:id>',views.distedit.as_view(),name='edit_District'),
    path('edit_Talluk/<int:id>',views.tallukedit.as_view(),name='edit_Talluk'),
    path('edit_City/<int:id>',views.cityedit.as_view(),name='edit_City'),
    path('edit_Pincode/<int:id>',views.Pincodeedit.as_view(),name='edit_Pincode'),
#---------------------------------------------Delete-Pages-------------------------------------------------------------------------------------------
    path('delete_Country/<int:id>',views.Country_delete.as_view(),name='delete_Country'),
    path('delete_State/<int:id>',views.State_delete.as_view(),name='delete_State'),
    path('delete_District/<int:id>',views.Dist_delete.as_view(),name='delete_District'),
    path('delete_Talluk/<int:id>',views.Talluk_delete.as_view(),name='delete_Talluk'),
    path('delete_City/<int:id>',views.City_delete.as_view(),name='delete_City'),
    path('delete_Pin/<int:id>',views.Pincode_delete.as_view(),name='delete_Pin'),
#-----------------------------------------------------Activation button ----------------------------------------------------------------------
    path('Status_update_Country/<str:action>/<int:id>', views.Countryactivation.as_view(), name='Status_update_Country'),
    path('Status_update_State/<str:action>/<int:id>', views.Stateactivation.as_view(), name='Status_update_State'),
    path('Status_update_District/<str:action>/<int:id>', views.Distactivation.as_view(), name='Status_update_District'),
    path('Status_update_Talluk/<str:action>/<int:id>', views.Tallukactivation.as_view(), name='Status_update_Talluk'),
    path('Status_update_City/<str:action>/<int:id>', views.cityactivation.as_view(), name='Status_update_City'),
    path('Status_update_Pincode/<str:action>/<int:id>', views.pincodeactivation.as_view(), name='Status_update_Pincode'),


# ==========================================medium and lanmguge =============================================================================
# ==========================================medium and lanmguge =============================================================================
# ==========================================medium and lanmguge =============================================================================

    path('Add_medium/',views.mediumView.as_view(), name='Add_medium'),
    path('Add_Languge/',views.langView.as_view(), name='Add_Languge'),

    path('view_medium/',views.medium_data_View.as_view(), name='view_medium'),
    path('view_Languge/',views.lang_data_View.as_view(), name='view_Languge'),

    path('edit_medium/<int:id>',views.medium_edit.as_view(), name='edit_medium'),
    path('edit_Languge/<int:id>',views.lang_edit.as_view(), name='edit_Languge'),

    path('delete_medium/<int:id>', views.medium_delete.as_view(), name='delete_medium'),
    path('delete_Languge/<int:id>', views.lang_delete.as_view(), name='delete_Languge'),

    path('Status_update_medium/<str:action>/<int:id>', views.mediumactivation.as_view(), name='Status_update_medium'),
    path('Status_update_languge/<str:action>/<int:id>', views.langugeactivation.as_view(), name='Status_update_languge'),
    # ================================================================================================================================================
    # ================================================================================================================================================
    # ================================================================================================================================================
    # ___________________________religio caste subcaste----------------------------------------
    path('Add_religion/',views.religionView.as_view(), name='Add_religion'),
    path('Add_caste/',views.casteView.as_view(), name='Add_caste'),
    path('Add_subcaste/',views.subcasteView.as_view(), name='Add_subcaste'),

    path('view_Religion/', views.religiondata.as_view(), name='view_Religion'),
    path('view_Caste/', views.castedata.as_view(), name='view_Caste'),
    path('view_Subcaste/',views.subcastedata.as_view(), name='view_Subcaste'),

    path('edit_Religion/<int:id>',views.religiondata_edit.as_view(),name='edit_Religion'),
    path('edit_Caste/<int:id>',views.Castedata_edit.as_view(),name='edit_Caste'),
    path('edit_Subcaste/<int:id>',views.subcastedata_edit.as_view(),name='edit_Subcaste'),

    path('delete_Religion/<int:id>', views.Religion_delete.as_view(), name='delete_Religion'),
    path('delete_Caste/<int:id>', views.Caste_delete.as_view(), name='delete_Caste'),
    path('delete_Subcaste/<int:id>', views.SubCaste_delete.as_view(), name='delete_Subcaste'),

    path('Status_update_Religion/<str:action>/<int:id>', views.Religion_activation.as_view(), name='Status_update_Religion'),
    path('Status_update_Caste/<str:action>/<int:id>', views.Caste_activation.as_view(), name='Status_update_Caste'),
    path('Status_update_Subcaste/<str:action>/<int:id>', views.Subcaste_activation.as_view(), name='Status_update_Subcaste'),

# =========================================================Designation==============================================================
    path('Add_Designation/',views.designationView.as_view(),name='Add_Designation'),
    path('View_Designation/',views.designation_data_view.as_view(),name='View_Designation'),
    path('Edit_Designation/<int:id>',views.designationEdit.as_view(),name='Edit_Designation'),
    path('Delete_Designation/<int:id>',views.designation_delete.as_view(),name='Delete_Designation'),
    path('Activate_Designation/<str:action>/<int:id>',views.Designationactivation.as_view(),name='Activate_Designation'),


#     =========================================================Committee=============================================================
    path('Add_Commitee/',views.View_Add_Committe.as_view(),name='Add_Commitee'),
    path('View_Committe/',views.committe_data_view.as_view(),name='View_Committe'),
    path('Edit_Committe/<int:id>',views.Edit_Committe.as_view(),name='Edit_Committe'),
    path('Delete_Committe/<int:id>',views.delete_committe.as_view(),name='Delete_Committe'),
    path('Activate_Committe/<str:action>/<int:id>',views.Committe_activation.as_view(),name='Activate_Committe'),


# =================================================Fee-Catogory==================================================================
    path('Add_fee_catogory/',views.View_Add_Catogory.as_view(),name='Add_fee_catogory'),
    path('View_fee_catogory/',views.Fee_cat_data_view.as_view(),name='View_fee_catogory'),
    path('Edit_fee_catogory/<int:id>',views.EditFeeCatogory.as_view(),name='Edit_fee_catogory'),
    path('Activation_fee_catogory/<str:action>/<int:id>',views.Fee_cat_Activation.as_view(),name='Activation_fee_catogory'),
    path('Delete_fee_catogory/<int:id>',views.delete_FeeCatogory.as_view(),name='Delete_fee_catogory'),


     path('Add_Entry_type/',views.Add_EntryType.as_view(),name='Add_Entry_type'),
    path('View_Entry_type/',views.Entrytype_data_view.as_view(),name='View_Entry_type'),
    path('Edit_Entry_type/<int:id>', views.editEntrytype.as_view(), name='Edit_Entry_type'),
    path('Delete_Entry_type/<int:id>',views.delete_EntryType.as_view(),name='Delete_Entry_type'),
    path('Activation_Entry_type/<str:action>/<int:id>',views.Entry_type_Activation.as_view(),name='Activation_Entry_type'),




]


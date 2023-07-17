function delete_member_role(user_role_records){
    let current_record = JSON.parse(user_role_records);
    console.log(current_record);
    let url_path = '/member_roles';
    let status = 'Delete';
    Swal.fire({
        title: 'Are you sure?',
        text: "You want to Delete" + " - " + current_record['name'],
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, ' + status
    }).then((result) => {
        if (result['isConfirmed']) {
            $.post(url_path, {
                'member_roles_id': current_record['id'],
                'member_roles_status': current_record['status'],
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
            }, function (data, textStatus) {
                if (data['authStatus']) {
                    window.location.reload();
                    Toast.fire({
                        icon: 'success',
                        title: 'Record Deleted Successfully!'
                    });
                } else {
                    Toast.fire({
                        icon: 'error',
                        title: 'Failed to ' + status + ' Record!'
                    });
                }
            });
        }

    });
}


function delete_agent_firm(user_role_records){
    let current_record = JSON.parse(user_role_records);
    console.log(current_record);
    let url_path = '/firm_name_info/';
    let status = 'Delete';
    Swal.fire({
        title: 'Are you sure?',
        text: "You want to Delete" + " - " + current_record['firm_name'],
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, ' + status
    }).then((result) => {
        if (result['isConfirmed']) {
            $.post(url_path, {
                'agent_firm_id': current_record['id'],
                'member_roles_status': current_record['status'],
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
            }, function (data, textStatus) {
                if (data['authStatus']) {
                    window.location.reload();
                    Toast.fire({
                        icon: 'success',
                        title: 'Record Deleted Successfully!'
                    });
                } else {
                    Toast.fire({
                        icon: 'error',
                        title: 'Failed to ' + status + ' Record!'
                    });
                }
            });
        }

    });
}


function delete_office_staff(user_role_records)
{
   let current_record = JSON.parse(user_role_records);
   console.log(current_record);
   let url_path = '/office_staff';
   let status = 'Delete';
    if (current_record['status']) {
        status = '';
    }
    Swal.fire({
        title: 'Are you sure?',
        text: "You want to Delete" + " - " + current_record['full_name'],
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, ' + status
    }).then((result) => {
        if (result['isConfirmed']) {
            $.post(url_path, {
                'office_staff_records': current_record['id'],
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
            }, function (data, textStatus) {
                if (data['authStatus']) {
                    window.location.reload();
                    Toast.fire({
                        icon: 'success',
                        title: 'Record Deleted Successfully!'
                    });
                } else {
                    Toast.fire({
                        icon: 'error',
                        title: 'Failed to ' + status + ' Record!'
                    });
                }
            });
        }

    });
}
function delete_member_registration(user_role_records){
    let current_record = JSON.parse(user_role_records);
    console.log(current_record);
    let url_path = '/member_registration';
    let status = 'Delete';
    if (current_record['status']) {
        status = '';
    }
    Swal.fire({
        title: 'Are you sure?',
        text: "You want to Delete" + " - " + current_record['full_name'],
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, ' + status
    }).then((result) => {
        if (result['isConfirmed']) {
            $.post(url_path, {
                'member_registration_id': current_record['id'],
                'member_registration_status': current_record['status'],
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
            }, function (data, textStatus) {
                if (data['authStatus']) {
                    window.location.reload();
                    Toast.fire({
                        icon: 'success',
                        title: 'Record Deleted Successfully!'
                    });
                } else {
                    Toast.fire({
                        icon: 'error',
                        title: 'Failed to ' + status + ' Record!'
                    });
                }
            });
        }

    });
}


function delete_member_role_attribute(user_role_records){
    let current_record = JSON.parse(user_role_records);
    console.log(current_record);
    let url_path = '/member_role_attributes';
    let status = 'Delete';
    if (current_record['status']) {
        status = '';
    }
    Swal.fire({
        title: 'Are you sure?',
       text: "You want to Delete"  + " - " + current_record['name'],
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, ' + status
    }).then((result) => {
        if (result['isConfirmed']) {
            $.post(url_path, {
                'selected_member_id': current_record['id'],
                'selected_member_status': current_record['status'],
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
            }, function (data, textStatus) {
                if (data['authStatus']) {
                    window.location.reload();
                    Toast.fire({
                        icon: 'success',
                        title: 'Record Deleted Successfully!'
                    });
                } else {
                    Toast.fire({
                        icon: 'error',
                        title: 'Failed to ' + status + ' Record!'
                    });
                }
            });
        }

    });
}

function delete_financer(user_role_records){
   let current_record = JSON.parse(user_role_records);
    console.log(current_record);
    let url_path = '/financer';
    let status = 'Delete';
    if (current_record['status']) {
        status = '';
    }
    Swal.fire({
        title: 'Are you sure?',
       text: "You want to Delete" + " - " + current_record['full_name'],
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, ' + status
    }).then((result) => {
        if (result['isConfirmed']) {
            $.post(url_path, {
                'financer_id': current_record['id'],
                'financer_status': current_record['status'],
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
            }, function (data, textStatus) {
                if (data['authStatus']) {
                    window.location.reload();
                    Toast.fire({
                        icon: 'success',
                        title: 'Record Deleted Successfully!'
                    });
                } else {
                    Toast.fire({
                        icon: 'error',
                        title: 'Failed to ' + status + ' Record!'
                    });
                }
            });
        }

    });


}

function delete_staff(user_role_records){
   let current_record = JSON.parse(user_role_records);
    console.log(current_record);
    let url_path = '/staff';
    let status = 'Delete';
    if (current_record['status']) {
        status = '';
    }
    Swal.fire({
        title: 'Are you sure?',
       text: "You want to Delete" + " - " + current_record['full_name'],
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, ' + status
    }).then((result) => {
        if (result['isConfirmed']) {
            $.post(url_path, {
                'staff_id': current_record['id'],
                'financer_status': current_record['status'],
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
            }, function (data, textStatus) {
                if (data['authStatus']) {
                    window.location.reload();
                    Toast.fire({
                        icon: 'success',
                        title: 'Record Deleted Successfully!'
                    });
                } else {
                    Toast.fire({
                        icon: 'error',
                        title: 'Failed to ' + status + ' Record!'
                    });
                }
            });
        }

    });


}

function delete_seizing_agent(user_role_records){
   let current_record = JSON.parse(user_role_records);
    console.log(current_record);
    let url_path = '/seizing_agent';
    let status = 'Delete';
    if (current_record['status']) {
        status = '';
    }
    Swal.fire({
        title: 'Are you sure?',
       text: "You want to Delete" + " - " + current_record['full_name'],
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, ' + status
    }).then((result) => {
        if (result['isConfirmed']) {
            $.post(url_path, {
                'seizing_agent_id': current_record['id'],
                'seizing_agent_status': current_record['status'],
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
            }, function (data, textStatus) {
                if (data['authStatus']) {
                    window.location.reload();
                    Toast.fire({
                        icon: 'success',
                        title: 'Record Deleted Successfully!'
                    });
                } else {
                    Toast.fire({
                        icon: 'error',
                        title: 'Failed to ' + status + ' Record!'
                    });
                }
            });
        }

    });

}

function delete_property_contractor(user_role_records){
    let current_record = JSON.parse(user_role_records);
    console.log(current_record);
    let url_path = '/property_contractor';
    let status = 'Delete';
    if (current_record['status']) {
        status = '';
    }
    Swal.fire({
        title: 'Are you sure?',
       text: "You want to Delete" + " - " + current_record['full_name'],
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, ' + status
    }).then((result) => {
        if (result['isConfirmed']) {
            $.post(url_path, {
                'property_contractor_id': current_record['id'],
                'property_contractor_status': current_record['status'],
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
            }, function (data, textStatus) {
                if (data['authStatus']) {
                    window.location.reload();
                    Toast.fire({
                        icon: 'success',
                        title: 'Record Deleted Successfully!'
                    });
                } else {
                    Toast.fire({
                        icon: 'error',
                        title: 'Failed to ' + status + ' Record!'
                    });
                }
            });
        }

    });

}

function delete_bank_details(user_role_records){
    let current_record = JSON.parse(user_role_records);
    console.log(current_record);
    let url_path = '/inventory/bank_information/';
    let status = 'Delete';
    if (current_record['status']) {
        status = '';
    }
    Swal.fire({
        title: 'Are you sure?',
       text: "You want to Delete" + " - " + current_record['bank_name'],
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, ' + status
    }).then((result) => {
        if (result['isConfirmed']) {
            $.post(url_path, {
                'bank_information_id': current_record['id'],
                'bank_information_status': current_record['status'],
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
            }, function (data, textStatus) {
                if (data['authStatus']) {
                    window.location.reload();
                    Toast.fire({
                        icon: 'success',
                        title: 'Record Deleted Successfully!'
                    });
                } else {
                    Toast.fire({
                        icon: 'error',
                        title: 'Failed to ' + status + ' Record!'
                    });
                }
            });
        }

    });
}

function delete_vehicle_type(user_role_records){
    let current_record = JSON.parse(user_role_records);
    console.log(current_record);
    let url_path = '/vehicles/vehicle_type';
    let status = 'Delete';
    if (current_record['status']) {
        status = '';
    }
    Swal.fire({
        title: 'Are you sure?',
       text: "You want to Delete" + " - " + current_record['name'],
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, ' + status
    }).then((result) => {
        if (result['isConfirmed']) {
            $.post(url_path, {
                'vehicle_types_id': current_record['id'],
                'vehicle_types_status': current_record['status'],
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
            }, function (data, textStatus) {
                if (data['authStatus']) {
                    window.location.reload();
                    Toast.fire({
                        icon: 'success',
                        title: 'Record Deleted Successfully!'
                    });
                } else {
                    Toast.fire({
                        icon: 'error',
                        title: 'Failed to ' + status + ' Record!'
                    });
                }
            });
        }

    });
}

function delete_vehicle(user_role_records){
    let current_record = JSON.parse(user_role_records);
    console.log(current_record);
    let url_path = '/vehicles/vehicle';
    let status = 'Delete';
    if (current_record['status']) {
        status = '';
    }
    Swal.fire({
        title: 'Are you sure?',
        text: "You want to Delete" + " - " + current_record['name'],
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, ' + status
    }).then((result) => {
        if (result['isConfirmed']) {
            $.post(url_path, {
                'assets_id': current_record['id'],
                'assets_status': current_record['status'],
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
            }, function (data, textStatus) {
                if (data['authStatus']) {
                    window.location.reload();
                    Toast.fire({
                        icon: 'success',
                        title: 'Record Deleted Successfully!'
                    });
                } else {
                    Toast.fire({
                        icon: 'error',
                        title: 'Failed to ' + status + ' Record!'
                    });
                }
            });
        }

    });
}
function delete_accessories(user_role_records){
    let current_record = JSON.parse(user_role_records);
    console.log(current_record);
    let url_path = '/vehicles/accessories';
    let status = 'Delete';
    if (current_record['status']) {
        status = '';
    }
    Swal.fire({
        title: 'Are you sure?',
        text: "You want to Delete" + " - " + current_record['name'],
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, ' + status
    }).then((result) => {
        if (result['isConfirmed']) {
            $.post(url_path, {
                'parts_id': current_record['id'],
                'parts_status': current_record['status'],
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
            }, function (data, textStatus) {
                if (data['authStatus']) {
                    window.location.reload();
                    Toast.fire({
                        icon: 'success',
                        title: 'Record Deleted Successfully!'
                    });
                } else {
                    Toast.fire({
                        icon: 'error',
                        title: 'Failed to ' + status + ' Record!'
                    });
                }
            });
        }

    });
}
function delete_accessories_attributes(user_role_records){
    let current_record = JSON.parse(user_role_records);
    console.log(current_record);
    let url_path = '/vehicles/accessories_attributes';
    let status = 'Delete';
    if (current_record['status']) {
        status = '';
    }
    Swal.fire({
        title: 'Are you sure?',
        text: "You want to Delete" + " - " + current_record['name'],
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, ' + status
    }).then((result) => {
        if (result['isConfirmed']) {
            $.post(url_path, {
                'parts_attributes_id': current_record['id'],
                'parts_attributes_status': current_record['status'],
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
            }, function (data, textStatus) {
                if (data['authStatus']) {
                    window.location.reload();
                    Toast.fire({
                        icon: 'success',
                        title: 'Record Deleteds Successfully!'
                    });
                } else {
                    Toast.fire({
                        icon: 'error',
                        title: 'Failed to ' + status + ' Record!'
                    });
                }
            });
        }

    });
}


function delete_vehicle_type_attribute(user_role_records){
    let current_record = JSON.parse(user_role_records);
    console.log(current_record);
    let url_path = '/vehicles/vehicle_type_attributes';
    let status = 'Delete';
    if (current_record['status']) {
        status = '';
    }
    Swal.fire({
        title: 'Are you sure?',
        text: "You want to Delete" + " - " + current_record['name'],
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, ' + status
    }).then((result) => {
        if (result['isConfirmed']) {
            $.post(url_path, {
                'asset_type_attributes_id': current_record['id'],
                'asset_type_attributes_status': current_record['status'],
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
            }, function (data, textStatus) {
                if (data['authStatus']) {
                    window.location.reload();
                    Toast.fire({
                        icon: 'success',
                        title: 'Record Deleteds Successfully!'
                    });
                } else {
                    Toast.fire({
                        icon: 'error',
                        title: 'Failed to ' + status + ' Record!'
                    });
                }
            });
        }

    });
}

function delete_asset_inventory(user_role_records){
    let current_record = JSON.parse(user_role_records);
    console.log(current_record);
    let url_path = '/inventory/';
    let status = 'Delete';
    if (current_record['status']) {
        status = '';
    }
    Swal.fire({
        title: 'Are you sure?',
        text: "You want to Delete" + " - " + current_record['financer'],
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, ' + status
    }).then((result) => {
        if (result['isConfirmed']) {
            $.post(url_path, {
                'inventory_id': current_record['id'],
                'inventory_status': current_record['status'],
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
            }, function (data, textStatus) {
                if (data['authStatus']) {
                    window.location.reload();
                    Toast.fire({
                        icon: 'success',
                        title: 'Record Deleted Successfully!'
                    });
                } else {
                    Toast.fire({
                        icon: 'error',
                        title: 'Failed to ' + status + ' Record!'
                    });
                }
            });
        }

    });
}
function delete_asset_tariff(user_role_records)
{
 let current_record = JSON.parse(user_role_records);
    console.log(current_record);
    let url_path = '/asset_tariff_charges/';
    let status = 'Delete';
    if (current_record['status']) {
        status = '';
    }
    Swal.fire({
        title: 'Are you sure?',
        text: "You want to Delete" + " - " + current_record['vehicle_type_name'],
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, ' + status
    }).then((result) => {
        if (result['isConfirmed']) {
            $.post(url_path, {
                'tariff_id': current_record['id'],
                'tariff_status': current_record['status'],
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
            }, function (data, textStatus) {
                if (data['authStatus']) {
                    window.location.reload();
                    Toast.fire({
                        icon: 'success',
                        title: 'Record Deleted Successfully!'
                    });
                } else {
                    Toast.fire({
                        icon: 'error',
                        title: 'Failed to ' + status + ' Record!'
                    });
                }
            });
        }

    });
}
function delete_organization_info(user_role_records)
{
 let current_record = JSON.parse(user_role_records);
    console.log(current_record);
    let url_path = '/organization_info/';
    let status = 'Delete';
    if (current_record['status']) {
        status = '';
    }
    Swal.fire({
        title: 'Are you sure?',
        text: "You want to Delete" + " - " + current_record['name'],
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, ' + status
    }).then((result) => {
        if (result['isConfirmed']) {
            $.post(url_path, {
                'organization_id': current_record['id'],
                'organization_status': current_record['status'],
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
            }, function (data, textStatus) {
                if (data['authStatus']) {
                    window.location.reload();
                    Toast.fire({
                        icon: 'success',
                        title: 'Record Deleted Successfully!'
                    });
                } else {
                    Toast.fire({
                        icon: 'error',
                        title: 'Failed to ' + status + ' Record!'
                    });
                }
            });
        }

    });
}


function delete_organization_branch_info(user_role_records)
{
    let current_record = JSON.parse(user_role_records);
    console.log(current_record);
    let url_path = '/organization_info/organization_branch_info/';
    let status = 'Delete';
    if (current_record['status']) {
        status = '';
    }
    Swal.fire({
        title: 'Are you sure?',
        text: "You want to Delete" + " - " + current_record['branch_name'],
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, ' + status
    }).then((result) => {
        if (result['isConfirmed']) {
            $.post(url_path, {
                'organization_branch_id': current_record['id'],
                'organization_branch_status': current_record['status'],
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
            }, function (data, textStatus) {
                if (data['authStatus']) {
                    window.location.reload();
                    Toast.fire({
                        icon: 'success',
                        title: 'Record Deleted Successfully!'
                    });
                } else {
                    Toast.fire({
                        icon: 'error',
                        title: 'Failed to ' + status + ' Record!'
                    });
                }
            });
        }

    });
}

function delete_police_info(user_role_records){
    let current_record = JSON.parse(user_role_records);
    console.log(current_record);
    let url_path = '/organization_info/police_intimation/';
    let status = 'Delete';
    Swal.fire({
        title: 'Are you sure?',
        text: "You want to Delete" + " - " + current_record['full_name'],
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, ' + status
    }).then((result) => {
        if (result['isConfirmed']) {
            $.post(url_path, {
                'police_id': current_record['id'],
                'police_info_status': current_record['status'],
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
            }, function (data, textStatus) {
                if (data['authStatus']) {
                    window.location.reload();
                    Toast.fire({
                        icon: 'success',
                        title: 'Record Deleted Successfully!'
                    });
                } else {
                    Toast.fire({
                        icon: 'error',
                        title: 'Failed to ' + status + ' Record!'
                    });
                }
            });
        }

    });
}




function delete_add_location_info(user_role_records){
    let current_record = JSON.parse(user_role_records);
    console.log(current_record);
    let url_path = '/organization_info/add_location_info/';
    let status = 'Delete';
    Swal.fire({
        title: 'Are you sure?',
        text: "You want to Delete" + " - " + current_record['name'],
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, ' + status
    }).then((result) => {
        if (result['isConfirmed']) {
            $.post(url_path, {
                'location_id': current_record['id'],
                'location_info_status': current_record['status'],
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
            }, function (data, textStatus) {
                if (data['authStatus']) {
                    window.location.reload();
                    Toast.fire({
                        icon: 'success',
                        title: 'Record Deleted Successfully!'
                    });
                } else {
                    Toast.fire({
                        icon: 'error',
                        title: 'Failed to ' + status + ' Record!'
                    });
                }
            });
        }

    });
}



function delete_branch(user_role_records){
   let current_record = JSON.parse(user_role_records);
    console.log(current_record);
    let url_path = '/branch';
    let status = 'Delete';
    if (current_record['status']) {
        status = '';
    }
    Swal.fire({
        title: 'Are you sure?',
       text: "You want to Delete" + " - " + current_record['full_name'],
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, ' + status
    }).then((result) => {
        if (result['isConfirmed']) {
            $.post(url_path, {
                'branch_record_id': current_record['id'],
                'branch_record_status': current_record['status'],
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
            }, function (data, textStatus) {
                if (data['authStatus']) {
                    window.location.reload();
                    Toast.fire({
                        icon: 'success',
                        title: 'Record Deleted Successfully!'
                    });
                } else {
                    Toast.fire({
                        icon: 'error',
                        title: 'Failed to ' + status + ' Record!'
                    });
                }
            });
        }

    });

}


function delete_exit_inventory(record_element) {
 let current_record = JSON.parse(record_element);
    console.log(current_record);
    let url_path = '/inventory/exit_inventory/';
    let status = 'Delete';
    if (current_record['status']) {
        status = '';
    }
    Swal.fire({
        title: 'Are you sure?',
        text: "You want to Delete" + " - " + current_record['asset_inventory'][0]['financer_id'],
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, ' + status
    }).then((result) => {
        if (result['isConfirmed']) {
            $.post(url_path, {
                'exit_inventory_id': current_record['id'],
                'exit_inventory_status': current_record['status'],
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
            }, function (data, textStatus) {
                if (data['authStatus']) {
                    window.location.reload();
                    Toast.fire({
                        icon: 'success',
                        title: 'Record Deleted Successfully!'
                    });
                } else {
                    Toast.fire({
                        icon: 'error',
                        title: 'Failed to ' + status + ' Record!'
                    });
                }
            });
        }

    });
}



function delete_financer_parking(user_role_records) {
 let current_record = JSON.parse(user_role_records);
    console.log(current_record);
    let url_path = '/asset_tariff_charges/financer_parking_days';
    let status = 'Delete';
    if (current_record['status']) {
        status = '';
    }
    Swal.fire({
        title: 'Are you sure?',
        text: "You want to Delete" + " - " + current_record['financer_role'],
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, ' + status
    }).then((result) => {
        if (result['isConfirmed']) {
            $.post(url_path, {
                'parking_days_id': current_record['id'],
                'parking_days_status': current_record['status'],
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
            }, function (data, textStatus) {
                if (data['authStatus']) {
                    window.location.reload();
                    Toast.fire({
                        icon: 'success',
                        title: 'Record Deleted Successfully!'
                    });
                } else {
                    Toast.fire({
                        icon: 'error',
                        title: 'Failed to ' + status + ' Record!'
                    });
                }
            });
        }

    });
}
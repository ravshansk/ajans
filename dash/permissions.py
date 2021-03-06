from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from dash.models import Actor, User

# Define groups
g_owner = Group.objects.get_or_create(name='owner')[0]
g_staff = Group.objects.get_or_create(name='staff')[0]
g_client = Group.objects.get_or_create(name='client')[0]

## Define permissions
#c_user = Permission.objects.filter(codename="add_user")[0]
#r_user = Permission.objects.filter(codename="view_user")[0]
#u_user = Permission.objects.filter(codename="change_user")[0]
#d_user = Permission.objects.filter(codename="delete_user")[0]
#c_actor = Permission.objects.filter(codename="add_actor")[0]
#r_actor = Permission.objects.filter(codename="view_actor")[0]
#u_actor = Permission.objects.filter(codename="change_actor")[0]
#d_actor = Permission.objects.filter(codename="delete_actor")[0]
#r_contact = Permission.objects.filter(codename="view_contact_info")[0]

## Give permissions to groups
#g_owner.permissions.add(c_actor, r_actor, u_actor, d_actor, r_contact, c_user, r_user, u_user, d_user)
#g_staff.permissions.add(c_actor, r_actor, u_actor, r_contact, c_user, r_user, u_user, d_user)
#g_client.permissions.add(r_actor)

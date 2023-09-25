from rest_framework import permissions
from .permissions import IsStaffEditorPermissions

class StaffEditorPermissionMixin():
    permission_classes=[permissions.IsAdminUser,
                                 IsStaffEditorPermissions]
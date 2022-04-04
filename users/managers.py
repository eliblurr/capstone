from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):

    def create_user(self, employee_id, password, **extra_fields):
        """
        Create and save a User with the given employee_id and password.
        """
        if not employee_id:
            raise ValueError('Employee id required')
        
        if extra_fields.get('email', None):
            extra_fields.setdefault('email', self.normalize_email(extra_fields['email']))

        if extra_fields.get('role', None)=='admin':
            extra_fields.setdefault('is_staff', True)
            extra_fields.setdefault('is_superuser', True)
            extra_fields.setdefault('is_active', True)

        user = self.model(employee_id=employee_id, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, employee_id, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('role', 'admin')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        return self.create_user(employee_id, password, **extra_fields)
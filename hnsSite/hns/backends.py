from .models import Users
import logging


class MyAuthBackend(object):
    def authenticate(self, email, password):    
        try:
            user = Users.objects.get(email=email)
            if user.check_password(password):
                return user
            else:
                return None
        except Users.DoesNotExist:
            logging.getLogger("error_logger").error("user with login %s does not exists " % login)
            return None
        except Exception as e:
            logging.getLogger("error_logger").error(repr(e))
            return None

    def get_user(self, user_id):
        try:
            user = Users.objects.get(sys_id=user_id)
            if user.is_active:
                return user
            return None
        except Users.DoesNotExist:
            logging.getLogger("error_logger").error("user with %(user_id)d not found")
            return None

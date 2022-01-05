# class User(object):
#     # route_app_labels = {'auth', 'contenttypes', 'sessions', 'admin'}
#     route_app_labels = {'User'}
#     def db_for_read(self, model, **hints):
#         from django.conf import settings
#         if not settings.DATABASES.has_key('db_app1'):
#             return None
#         if model._meta.app_label == 'app1':
#             return 'User_db'
#         return None

#     def db_for_write(self, model, **hints):
#         from django.conf import settings
#         if not settings.DATABASES.has_key('db_app1'):
#             return None
#         if model._meta.app_label == 'app1':
#             return 'User_db'
#         return None

#     # def allow_relation(self, obj1, obj2, **hints):
#     #     from django.conf import settings
#     #     if not settings.DATABASES.has_key('db_app1'):
#     #         return None
#     #     if obj1._meta.app_label == 'app1' or obj2._meta.app_label == 'app1':
#     #         return True
#     #     return None

#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         if app_label in self.route_app_labels:
#             return db == 'User_db'
#         return None
# class Router:
#     def db_for_read(self, model, **hints): 
#         return 'neighborhood_development_18_db'

#     def db_for_write(self, model, **hints): 
#         return 'neighborhood_development_18_db'

#     def allow_relation(self, obj1, obj2, **hints):
#         db_list = ('neighborhood_development_18_db')
#         if obj1._state.db in db_list and obj2._state.db in db_list: 
#             return True
#         return None

#     def allow_migrate(self, db, app_label, model_name=None, **hints): 
#         return True


class CivicSandboxRouter(object):
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'neighborhood_development_18':
            return 'neighborhood-development'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'neighborhood_development_18':
            return 'neighborhood-development'
        return None

    # def allow_relation(self, obj1, obj2, **hints):
    #     if obj1._meta.app_label in FIRST_EXTERNAL_APPS or \
    #             obj2._meta.app_label in FIRST_EXTERNAL_APPS:
    #         return True
    #     return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        print('hii danny .com')
        if app_label == 'neighborhood_development_18':
            return db == 'neighborhood-development'
        return None
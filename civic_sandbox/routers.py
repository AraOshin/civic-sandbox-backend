class CivicSandboxRouter(object):
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'neighborhood_development_18':
            return 'neighborhood-development'
        if model._meta.app_label == 'transportation_systems_18':
            return 'transportation-systems-main'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'neighborhood_development_18':
            return 'neighborhood-development'
        if model._meta.app_label == 'transportation_systems_18':
            return 'transportation-systems-main'
        return None

    # def allow_relation(self, obj1, obj2, **hints):
    #     if obj1._meta.app_label in FIRST_EXTERNAL_APPS or \
    #             obj2._meta.app_label in FIRST_EXTERNAL_APPS:
    #         return True
    #     return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'neighborhood_development_18':
            return db == 'neighborhood-development'
        if app_label == 'transportation_systems_18':
            return db ==  'transportation-systems-main'
        return None
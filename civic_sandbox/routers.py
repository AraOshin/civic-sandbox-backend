
class CivicSandboxRouter(object):
    db_map = {
        'neighborhood_development_18': 'neighborhood-development',
        'disaster_resilience_18': 'disaster-resilience-disaster',
        'housing_affordability_18': 'housing-affordability',
        }

    def db_for_read(self, model, **hints):
        app_label = model._meta.app_label
    
        if app_label == 'transportation_systems_18':
            if hasattr(model._meta, 'in_db'):
                return model._meta.in_db

        if app_label in self.db_map:
            return self.db_map[app_label]
        
        return None

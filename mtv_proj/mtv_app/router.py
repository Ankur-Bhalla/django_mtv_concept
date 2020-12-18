class CheckerRouter:

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'mtv_app':
            return 'mytestdb'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'mtv_app':
            return 'mytestdb'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'mtv_app' or obj2._meta.app_label == 'mtv_app':
            return True
        elif 'mtv_app' not in [obj1._meta.app_label, obj2._meta.app_label]:
            return True
        return False

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'mtv_app':
            return db == 'mytestdb'
        return None



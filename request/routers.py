
class DatabaseRouter(object):
    """
    A router to control all database operations on models in the
    request application.
    """

    def db_for_read(self, model, **hints):
        """
        Attempts to read request models go to mongo.
        """
        if model._meta.app_label == 'request':
            return 'mongo'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write request models go to mongo.
        """
        if model._meta.app_label == 'request':
            return 'mongo'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the request app is involved.
        """
        # Allow any relation between two models that are both in the request app.
        if obj1._meta.app_label == 'request' and obj2._meta.app_label == 'request':
            return True
        # No opinion if neither object is in the request app (defer to default or other routers).
        elif 'request' not in [obj1._meta.app_label, obj2._meta.app_label]:
            return None
        # Block relationship if one object is in the request app and the other isn't.
        return False

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the request app only appears in the 'mongo'
        database.
        """
        # The request app should be migrated only on the mongo database.
        if app_label == 'request':
            return db == 'mongo'
        # Ensure that all other apps don't get migrated on the mongo database.
        elif db == 'mongo':
            return False
        # No opinion for all other scenarios
        return None

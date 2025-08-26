class LogRouter:
    app_label = "log"

    def db_for_read(self, model, **hints):
        if model._meta.app_label == self.app_label:
            return "log"
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == self.app_label:
            return "log"
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == self.app_label:
            return db == "log"
        return None

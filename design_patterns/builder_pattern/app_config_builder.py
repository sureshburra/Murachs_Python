class AppConfig:
    def __init__(self, db_url, cache_enabled, log_level, workers):
        self.db_url = db_url
        self.cache_enabled = cache_enabled
        self.log_level = log_level
        self.workers = workers


class AppConfigBuilder:
    def __init__(self):
        self._db_url = "sqlite:///app.db"
        self._cache_enabled = True
        self._log_level = "INFO"
        self._workers = 4

    def db_url(self, url):
        self._db_url = url
        return self

    def set_cache_enabled(self, enabled: bool):
        self._cache_enabled = enabled
        return self

    def log_level(self, level):
        self._log_level = level
        return self

    def workers(self, workers: int):
        self._workers = workers
        return self

    def build(self):
        return AppConfig(
            db_url=self._db_url,
            cache_enabled=self._cache_enabled,
            log_level=self._log_level,
            workers=self._workers,
        )


# Usage
#
config = (
    AppConfigBuilder()
    .db_url("postgresql://user:pass@localhost/db")
    .log_level("DEBUG")
    .workers(8)
    .build()
)

print(config.db_url)
print(config.log_level)
print(config.cache_enabled)
print(config.workers)

ROUTES_LIST = (
    ('ALA', 'TSE'), ('TSE', 'ALA'),
    ('ALA', 'MOW'), ('MOW', 'ALA'),
    ('ALA', 'CIT'), ('CIT', 'ALA'),
    ('TSE', 'MOW'), ('MOW', 'TSE'),
    ('TSE', 'LED'), ('LED', 'TSE'),
)

CELERY_BROKER = 'redis://redis:6379'
CELERY_BACKEND = 'redis://redis:6379'

DATABASE_URL = 'database.db'

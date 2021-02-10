ROUTES_LIST = (
    ('ALA', 'TSE'), ('TSE', 'ALA'),
    ('ALA', 'MOW'), ('MOW', 'ALA'),
    ('ALA', 'CIT'), ('CIT', 'ALA'),
    ('TSE', 'MOW'), ('MOW', 'TSE'),
    ('TSE', 'LED'), ('LED', 'TSE'),
)

CELERY_BROKER = 'redis://localhost:6379/0'
CELERY_BACKEND = 'redis://localhost:6379/1'

DATABASE_URL = 'database.db'

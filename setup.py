from setuptools import setup, find_packages

setup(
    name='sheepdog',
    version='0.2.0',
    description='Flask blueprint for herding data submissions',
    url='https://github.com/uc-cdis/sheepdog',
    license='Apache',
    packages=find_packages(),
    install_requires=[
        'boto',
        'psycopg2',
        'cryptography',
        'Envelopes',
        'Flask-Cors',
        'Flask-SQLAlchemy-Session',
        'Flask',
        'fuzzywuzzy',
        'jsonschema',
        'lxml',
        'PyYAML',
        'requests',
        'setuptools',
        'simplejson',
        'authutils',
        'cdispyutils',
        'cdislogging',
        'datamodelutils',
        'dictionaryutils',
        'gdcdatamodel',
        'gdcdictionary',
        'indexclient',
        'signpostclient',
        'psqlgraph',
        'userdatamodel',
    ],
)

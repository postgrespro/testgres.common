try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    version="0.0.2",
    name="testgres.common",
    packages=[
        "testgres.common",
    ],
    package_dir={"testgres.common": "src"},
    description='Testgres common code',
    url='https://github.com/postgrespro/testgres.common',
    long_description_content_type='text/markdown',
    license='PostgreSQL',
    author='Postgres Professional',
    author_email='testgres@postgrespro.ru',
    keywords=['testgres'],
)


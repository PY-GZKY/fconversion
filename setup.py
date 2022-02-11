from setuptools import setup, find_packages

description = '一个用于各类文件相互转换的库'
long_description = '一个用于各类文件相互转换的库'

setup(
    name='fconversion',
    version='1.0.0',
    description=description,
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Framework :: AsyncIO',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Clustering',
        'Topic :: System :: Distributed Computing',
        'Topic :: System :: Monitoring',
        'Topic :: System :: Systems Administration',
    ],
    python_requires='>=3.7',
    author='PY-GZKY',
    author_email='341796767@qq.com',
    url='https://github.com/PY-GZKY/fconversion',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    entry_points="""
        [console_scripts]
        aiorq=aiorq.cli:cli
    """,
    install_requires=[
        'aioredis>=1.1.0,<2.0.0',
        'click>=6.7',
        'pydantic>=1',
        'dataclasses>=0.6;python_version == "3.8"',
        'typing-extensions>=3.7;python_version < "3.8"'
    ],
)

from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'mypkg'

setup(
    name='mypkg',
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='tento',
    maintainer_email='tentoshinz@gmail.com',
    description='robosys task',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'listener = mypkg.listener:main',
            'pubdate = mypkg.pubdate:main',
            'zellers = mypkg.zellers:main',
        ],
    },
)

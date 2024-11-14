from setuptools import find_packages, setup

package_name = 'mypkg'

setup(
    name='mypkg',
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
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
            'talker = mypkg.talker:main',
            #'listener = mypkg.listener:main',
        ],
    },
)

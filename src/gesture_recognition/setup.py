from setuptools import find_packages, setup

package_name = 'gesture_recognition'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
    ('share/ament_index/resource_index/packages',
        ['resource/gesture_recognition']),
    ('share/gesture_recognition', ['package.xml']),
    ('share/gesture_recognition/launch', ['launch/hri_system.launch.py']),
],

    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mirza-huzaifa',
    maintainer_email='mirza-huzaifa@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
entry_points={
    'console_scripts': [
        'gesture_reader = gesture_recognition.gesture_reader:main',
        'robot_controller = gesture_recognition.robot_controller:main',
    ],
},
)

from setuptools import setup

# python setup.py sdist
# twine upload dist/*

setup(name='CyberBook',
      version='0.0.9',
      description='Cyber spellbook for developers.',
      url='https://github.com/ClutchTech/TechBook',
      keywords='cyberbook encoders tools',
      author='Clutch_Reboot',
      author_email='clutchshadow26@gmail.com',
      license='GNU General Public License v3.0',
      packages=[
            'CyberBook.encoders',
            'CyberBook.interpreter',
            'CyberBook.listener',
            'CyberBook.wordlists'
      ],
      zip_safe=False,
      long_description=open('README.md', 'rt').read(),
      long_description_content_type='text/markdown',
      python_requires='>=3.10',
      )

# ocr_python_projet9
# LITReview
## Overview
A django project written as **study case** to be evaluated for validation of the project 6 of the **OpenClassrooms Python training courses**. The purpose is to implement a MVP of a website where memebers wil be able to ask for and share reviews aboout books.
               
## How to install locally with terminal this django project.

- [ ] Ensure you have installed or install on your computer
<a href="https://www.python.org//" target="_blank">Python</a>, 
<a href="https://pypi.org/project/pip/" target="_blank">PIP</a>, 
<a href="https://git-scm.com/" target="_blank">GIT</a>.

- [ ] Create locally directory for the projet and/navigate to it. 
- [ ] Clone the github project repository in this directory:

    ```git clone https://github.com/Chris59-create/ocr_python_projet9.git```
      
- [ ] Create and activate a virtual environment in this directory.

    <a href="https://medium.com/codex/python-version-management-with-pyenv-and-pyenv-virtualenv-linux-ecd6578b7bbf" target="_blank">About virtual environment</a>

- [ ] Install the python packages needed for the project:

   ```pip install -r requirements.txt```

- [ ] Migrate the database:

    ```python manage.py migrate```

- [ ] To be able to use the django built-in database admin site, create a superuser:

    ```python manage.py createsuperuser```

- [ ] Open your server:

    ```python manage.py runserver```
    
- [ ] To access to the LITReview website:

    Navigate in your browser to the link <a href="http://localhost:8000/" target="_blank">localhost:8000/</a>.
      
- [ ] To access to the admin site of the database:
    - Navigate in your browser to the link <a href="http://localhost:8000/admin/" target="_blank">localhost:8000/admin/</a>.
    - Enter the name and the password of the superuser that you created.
      

      


## Credits
Author: Chris59create (Chris59-create)

**Warning: this is a a coding for a training evaluation. The use of this code (Cloning, global or incomplete copy or re use of it) is forbidden.**

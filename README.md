# ocr_python_projet9
# LITReview
## Overview
A django project written as **study case** to be evaluated for validation of the project 6 of the **OpenClassrooms Python training courses**. The purpose is to implement a MVP of a website where memebers wil be able to ask for and share reviews aboout books.
               
## How to install locally with terminal this django project.

- [ ] Ensure you have installed or install on your computer
[Python](https://www.python.org/), 
[PIP](https://pypi.org/project/pip/), 
[GIT](https://git-scm.com/).
- [ ] Create locally a directory or navigate to directory where you want to 
  store the project. 
- [ ] Clone the github project repository in this directory:

    ```git clone https://github.com/Chris59-create/ocr_python_projet9.git```

- [ ] Navigate to the projet subdirectory `cd ocr_python_projet9`.
      
- [ ] Create and activate a virtual environment in this directory.

    [About virtual environment](https://medium.com/codex/python-version-management-with-pyenv-and-pyenv-virtualenv-linux-ecd6578b7bbf)


- [ ] Install the python packages needed for the project:

   ```pip install -r requirements.txt```

- [ ] Navigate to the subdirectory `cd litreview`.

- [ ] Migrate the database:

    ```python manage.py migrate```

- [ ] To be able to use the django built-in database admin site, create a superuser:

    ```python manage.py createsuperuser```

- [ ] Open your server:

    ```python manage.py runserver```
    
- [ ] To access to the LITReview website:

    Navigate in your browser to the link [localhost:8000/](http://localhost:8000/).
      
- [ ] To access to the admin site of the database:
    - Navigate in your browser to the link [localhost:8000/admin/](http://localhost:8000/admin/).
    - Enter the name and the password of the superuser that you created.
      

      


## Credits
Author: Chris59create (Chris59-create)

**Warning: this is a a coding for a training evaluation. The use of this code (Cloning, global or incomplete copy or re use of it) is forbidden.**

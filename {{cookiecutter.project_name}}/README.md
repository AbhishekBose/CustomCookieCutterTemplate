# {{cookiecutter.project_name}}
This is a README file by {{cookiecutter.author}} ({{cookiecutter.email}})

The project is about:
{{cookiecutter.description}}

## Team:
{% if cookiecutter.project_team == 'Great Team' %}
* Max E.Mumm
* Jack Pott

{% elif cookiecutter.project_team == 'Team of Legends' %}
* Armando E. Quito
* Al E.Gater

{% elif cookiecutter.project_team == 'The Other Team' %}
* May B.Dunn
* Justin Thyme
{% endif %}
{% extends 'templates/main_articles.j2' %}

{% block article_content %}

# Access Levels

Access Levels are an aggregated way of granting access to one or more Attributes. All Role permissions are granted using an Access Level.

## Attributes

An Attribute is a specific action that is possible for a specific resource type. Attributes are not granted directly, but are mapped from different Access Levels. In order to perform an action, you need to have an access level that grants you access to a certain attribute.


{% endblock %}

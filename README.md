# The Secret Login

A Flask App using Flask-WTForms that leads to a fun surprise. Day 61 Python Bootcamp


## Usage
This is a basic Flask App that uses Flask-WTForms and Bootstrap to generate a 
simple form. If you login using:

`email: admin@email.com`
`password: 12345678`

You'll be taken to a fun Giffy surprise. If you put in wrong credentials, there 
is a different fun Gif.  The entire point of this app was to use Flask-WTForms
to get easy validation and Bootstrap for styling.

The form is generated using wtf.quick_form(). While it makes form generation very
simple, it does add a layer of complexity to styling. You could be more verbose
and generate the same form like this:

```
<!-- {% block content %}
<div class="container">
	<h1>Login</h1>
	<form method="POST" action="{{ url_for('login') }}" novalidate>
		{{ form.csrf_token }}
		<p>{{ form.email.label }} <br> {{ form.email(size=30) }}</p>
		{% if form.email.errors %}
		<ul class="errors">
			{% for err in form.email.errors %}
			<li><span style="color:red">{{ err }}</span></li>
			{% endfor %}
		</ul>
		{% endif %}
		<p>{{ form.password.label }} <br> {{ form.password(size=30) }}</p>
		{% if form.password.errors %}
		<ul class="errors">
			{% for err in form.password.errors %}
			<li><span style="color:red">{{ err }}</span></li>
			{% endfor %}
		</ul>
		{% endif %}
		{{ form.submit }}
	</form>

</div>
{% endblock %} -->
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
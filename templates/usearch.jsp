{% extends "user_header.html" %}
{% block content %}
<form method="post" action="/search2">
<table align="center" >

<tr><td>
<tr><td> <h2>Results are</h2>
    {% for i in u_s %}
    
    <tr><td colspan=2> <br><h3>Name:	{{i.name}} &nbsp; {{i.lname}}
        <tr><td colspan=2> <br><h3>Email:	{{i.email}}

<input type="hidden" name="mail" value={{i.email}}/>
<tr><td colspan=2><input  class="form-control1"  type="submit" value="Send Friend Reqest"/>				
    {% endfor %}
</form><td>
</table>

{% endblock content%}

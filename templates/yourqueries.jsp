{% extends "uheader.html" %}
{% block content %}
<!-- <%@ include file="uheader.jsp"%>
<%@ page  import="java.sql.*" import="databaseconnection.*"  import="CT.*" %>
<%
    String message=request.getParameter("id");
    if(message!=null && message.equalsIgnoreCase("succ")){
    out.println("<script type=text/javascript>alert('Thank You!!')</script>");
	}
 %> -->
<!--
<%

try{
Connection con = databasecon.getconnection();
Statement st=con.createStatement();
Statement st2=con.createStatement();
String sql="select * from query where uemail='"+session.getAttribute("email")+"' ";
System.out.println(sql);
ResultSet rs=st.executeQuery(sql);
ResultSet rs2=null;
%>
-->	<header>
<h2>Your Questions & Answers</h2>
													</header>
{% for i in queries %}
<!-- <%
int i=0;
while(rs.next()){

%> --><br><br>
<b><font size="+2" color="#3d9c98">Q<%=++i%>)&nbsp;&nbsp;{{ i.queri }}</font></b>
	

<!-- <%
		rs2=st2.executeQuery("select * from interaction where qid='"+rs.getString(1)+"'  and ans!='non' ");
		while(rs2.next()){
%> -->
<!--{% for i in inter %}
<br><br> 
			<font size="+1" color="#4888d7">Ans)&nbsp;&nbsp;{{ inter['ans'] }}</font><br>By: {{ inter['user'] }}))
<!-- <%
	}
}



}
catch(Exception e){
System.out.println("11="+e);
}
%> -->
{% endfor %}-->
{% endfor %}

            </table>


<!-- <%@ include file="ufooter.jsp"%> -->
{% endblock content%}
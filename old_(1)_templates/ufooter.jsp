
											</section>


										</article>

								</div>
							</div>
							<div class="3u 12u(mobile)">
								<div class="sidebar">
<%@ page  import="java.sql.*" import="databaseconnection.*" %>

									<!-- Sidebar -->

										<!-- Recent Posts -->
											
										<!-- Something -->
											<section>
												<h2 class="major"><span><%=session.getAttribute("name")%></span></h2>
												<a href="#" class="image featured"><img src="view.jsp?id=<%=session.getAttribute("email")%>" alt="" /></a>
												<p>
									<form method="post" action="usearch.jsp">
									
										<h4><span>Friend Search</span></h2>
															
											<input type="text" name="email" required>	
											<br>
											<ul class="meta">
											<%String email=(String)session.getAttribute("email");%>

<%
											Connection con9 = databasecon.getconnection();
											Statement st9=con9.createStatement();
											String sql9="select * from frequest where uto='"+email+"' and	 requ='req' ";
											System.out.println(sql9);

											ResultSet rs9=st9.executeQuery(sql9);
											int c9=0;
											while(rs9.next())
											{
													c9++;
											}

											%>
											<%
											if(c9>0)
		
											{
												System.out.println("99999999999999999");
												%>

												<font color="#6666ff"><h3> <a href="freq.jsp"><li class="icon fa-users"><%=c9%> Friend Requests</a></font></h3>
												</h5>
											<%}
											else{
												%>
										<h3><li class="icon fa-users"> No Friend Requests</li><br>
										<%}
											%>


															<ul>	<li class="icon fa-list"><a href="viewf.jsp">View Friends</a></li>
															<ul>	<li class="icon fa-server"><a href="viewint.jsp">View Your Interests</a> </li>
															</ul>
												</form>	</p>

											</section>
														
								</div>
							</div>
						</div>
							</div>
						</div>
					</div>
				</div>

			<!-- Footer -->
							<footer id="footer" class="container">
						
					<div class="row 200%">
						<div class="12u">

							<!-- Contact -->
								<section>
									<h2 class="major"><span>Get in touch</span></h2>
									<ul class="contact">
										<li><a class="icon fa-facebook" href="#"><span class="label">Facebook</span></a></li>
										<li><a class="icon fa-twitter" href="#"><span class="label">Twitter</span></a></li>
										<li><a class="icon fa-instagram" href="#"><span class="label">Instagram</span></a></li>
										<li><a class="icon fa-dribbble" href="#"><span class="label">Dribbble</span></a></li>
										<li><a class="icon fa-google-plus" href="#"><span class="label">Google+</span></a></li>
									</ul>
								</section>

						</div>
					</div>

					<!-- Copyright -->
						<div id="copyright">
							<ul class="menu">
								<li>&copy; All rights reserved</li><li>Design & Developed by: </li>
							</ul>
						</div>

				</footer>

			</div>

		<!-- Scripts -->
			<script src="assets/js/jquery.min.js"></script>
			<script src="assets/js/jquery.dropotron.min.js"></script>
			<script src="assets/js/skel.min.js"></script>
			<script src="assets/js/skel-viewport.min.js"></script>
			<script src="assets/js/util.js"></script>
			<!--[if lte IE 8]><script src="assets/js/ie/respond.min.js"></script><![endif]-->
			<script src="assets/js/main.js"></script>

	</body>
</html>
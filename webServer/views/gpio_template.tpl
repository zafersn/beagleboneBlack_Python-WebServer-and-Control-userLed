<table>
<tr>
	<td>Pin Number</td>
	<td>Current Value</td>
	<td></td>
</tr>	
% for key, value in current_values.iteritems():
	<form action="/toggle?pin={{key}}" method="post">
	<tr>
		<td>{{key}}</td>
		<td>{{value}}</td>
		<td><input type="submit" value="Toggle"/></td>
	</tr>
	</form>
% end	
</table>
<html>
<head>
<style>
table, th, td {
    border: 1px solid black;
    border-collapse: collapse;
}
</style>
</head>
<body>
<h3>Your previous transactions:</h3>
<p></p>
<table style="width:100%">
  <tr>
    <th>ID</th>
    <th>Sender</th> 
    <th>Receiver</th>
    <th>Ammount</th>
    <th>Date</th>
  </tr>
  % for action in transactions:
    <tr>
        <td>{{action.id}}</td>
        <td>{{action.sender_r.name}} {{action.sender_r.surname}}</td> 
        <td>{{action.receiver_r.name}} {{action.receiver_r.surname}}</td>
        <td>{{action.ammount}}</td>
        <td>{{action.transaction_date}}</td>
    </tr>

</table>
</body>
</html>


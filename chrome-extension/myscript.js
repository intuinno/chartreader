url = "http://127.0.0.1:5000/chart";

$('img').each(function(i, obj) {
  var s = $(this).prop("src");
  console.log(s);
  
  var parent = $(this).parent();

  $.post(url, 
  {
    url: s
  },
  function(data, status) {
    debugger;
    parent.append(data['table']);
    
  });
 // $(this).parent().append('<table><caption>' + s + '</caption>   <tr>     <th scope="col">Name</th>    <th scope="col">Age</th>    <th scope="col">Birthday</th>    </tr>    <tr>     <th scope="row">Jackie</th>     <td>5</td>     <td>April 5</td>     </tr>     <tr>     <th scope="row">Beth</th>     <td>8</td>     <td>January 14</td>     </tr> 12</table>');

  
}) 


### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?  

 Python runs on the server and is commonly used for back end development while Javascript runs on the client or browser so it's often used for front end development (although Node.js can be used to write Javascript on the server side)

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.

  1. You can wrap the code attempting to call the missing key in a try-except block to handle the error.
  2. use the .get() method on the dictionary, if the entry doesn't exist it'll just return "None"

- What is a unit test?  

 A unit test is a set of test cases that tests individual components of the code

- What is an integration test?

 Integration testing is a set of test cases that tests how different components of a code interact with eachother

- What is the role of web application framework, like Flask?

 Web application frameworks sit on the server side and listens for requests being made to it be its various clients and responds to them. Amongst other things, web application frameworks do some of the following:
 * handle web requets
 * produce dynamic HTML
 * handle forms
 * handle cookies
 * connect to databases
 * provide user login/logout
 * cache pages for performance

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

  One would use URL parameter for the content that you would see on a page. It's related to the "subject of the page". 

  Query Parameters is more like extra info about the page changes the way you'll see the content but it's not integral to the content itself.

- How do you collect data from a URL placeholder parameter using Flask?
 You would first specify the placeholder using angled brackets in the route itself. Then you can call the function with the placeholder name directly in its parenthesis. Within the code in the function, you can refer directly to the placeholder name. 

- How do you collect data from the query string using Flask?
  You would use the request objects "args" sub-object and use it's .get() method. Within the parenthesis, you would include

- How do you collect data from the body of the request using Flask?
  import "request" object from Flask. The method used on the request object varies by type of data in the request:
    request.form: grabs data from a form
    request.json: grabs data from a json object
    request.file: takes data from a file
    reqeust.data: grabs raw data like binary or text

- What is a cookie and what kinds of things are they commonly used for?
  name-string value pair stored in the browser. The server tells the client to store these bits of data and they're typically used to save data for things like user preferences and authentication so users can stay logged on even after leaving the page and coming back to it.

- What is the session object in Flask?
  Session object in Flask is a storage mechanism powered by cookies that stores bits of data on the client (browser) and allows applications to persist states. Otherwise, http is stateless so it won't retain any information.

- What does Flask's `jsonify()` do?
  jsonify converts string that is in dictionary notation into an actual json object.

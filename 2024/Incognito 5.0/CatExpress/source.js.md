# `source.js`

Not sure why this is recognized as a virus...

```JavaScript
const express = require("express");
const bodyParser = require("body-parser");
const createConnectionWithRetry = require("./db");
const app = express();
const port = 80;

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static("public"));

async function startServer() {
  try {
    const connection = await createConnectionWithRetry();

    app.get("/", (req, res) => {
      res.sendFile(__dirname + "/index.html");
    });

    app.get("/login", (req, res) => {
      res.sendFile(__dirname + "/login.html");
    });

    app.post("/auth", function (request, response) {
      var username = request.body.username;
      var password = request.body.password;
      if (username && password) {
        connection.query(
          "SELECT * FROM accounts WHERE username = ? AND password = ?",
          [username, password],
          function (error, results, fields) {
            if (error) {
              console.error("Error occurred:", error);
              return response.status(500).send("Internal server error");
            }
            if (results.length > 0) {
              response.redirect("/?message=ictf{f4k3_fl4g}");
            } else {
              response.redirect("/?message=Invalid%20credentials");
            }
          },
        );
      } else {
        response.send("Please enter Username and Password!");
      }
    });

    app.listen(port, () => {
      console.log(`Server running at http://localhost:${port}/`);
    });
  } catch (error) {
    console.error("Failed to start the server:", error);
  }
}

startServer();
```

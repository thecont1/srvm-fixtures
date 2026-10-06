const http = require("node:http");
const fs = require("node:fs");
const path = require("node:path");

const port = Number(process.env.PORT || 3000);
const index = path.join(__dirname, "index.html");

const server = http.createServer((_req, res) => {
  res.setHeader("Content-Type", "text/html; charset=utf-8");
  fs.createReadStream(index).pipe(res);
});

server.listen(port, "127.0.0.1", () => {
  console.log(`web ready on http://127.0.0.1:${port}`);
});

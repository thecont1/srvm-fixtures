const http = require("node:http");

const port = Number(process.env.PORT || 3000);

const server = http.createServer((_req, res) => {
  res.setHeader("Content-Type", "text/plain; charset=utf-8");
  res.end("Hello from Node (srvm fixture x5)\n");
});

server.listen(port, "127.0.0.1", () => {
  console.log(`plain node listening on http://127.0.0.1:${port}`);
});

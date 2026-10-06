const port = Number(Deno.env.get("PORT") ?? "8000");

Deno.serve({ port, hostname: "127.0.0.1" }, () =>
  new Response("Hello from Deno (srvm fixture x2)\n")
);

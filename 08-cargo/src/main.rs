use std::io::{Read, Write};
use std::net::{TcpListener, TcpStream};
use std::{env, thread};

const BODY: &str = "Hello from Rust (srvm fixture 08)\n";

fn main() {
    let port = env::var("PORT").unwrap_or_else(|_| "7878".into());
    let listener = TcpListener::bind(format!("127.0.0.1:{port}")).expect("bind 127.0.0.1");
    let port = listener.local_addr().expect("local addr").port();
    println!("Listening on http://127.0.0.1:{port}");

    for stream in listener.incoming() {
        match stream {
            Ok(stream) => {
                thread::spawn(move || respond(stream));
            }
            Err(err) => eprintln!("accept: {err}"),
        }
    }
}

fn respond(mut stream: TcpStream) {
    let mut buf = [0u8; 1024];
    let _ = stream.read(&mut buf);
    let head = format!(
        "HTTP/1.1 200 OK\r\nContent-Type: text/plain; charset=utf-8\r\nContent-Length: {}\r\nConnection: close\r\n\r\n",
        BODY.len()
    );
    let _ = stream.write_all(head.as_bytes());
    let _ = stream.write_all(BODY.as_bytes());
}

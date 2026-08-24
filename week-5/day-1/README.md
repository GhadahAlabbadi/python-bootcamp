# Week 5 - Day 1

## Overview

The first day of Week 5 focused on networking and web fundamentals. The session explained how the Internet and the Web work, how browsers communicate with servers, and how data travels across networks.

The session also introduced DNS, IP addresses, routing, ports, URLs, client-server communication, and endpoint thinking.

---

## Topics Covered

- Internet vs Web
- Packet Switching
- ARPANET
- TCP/IP
- Web Request Journey
- DNS
- Public and Private IP Addresses
- NAT
- Routing and Hops
- Clients and Servers
- URL Structure
- Protocols and Domains
- Ports
- Paths, Query Parameters, and Fragments
- Local Web Server
- Endpoint Thinking

---

## Key Concepts

### Internet vs Web

The Internet is the global network that connects devices around the world.

The Web is a service that runs on top of the Internet and allows users to access websites and web pages through browsers.

### Internet Development

The development of the Internet was reviewed through:

**Packet Switching → ARPANET → TCP/IP → Internet → World Wide Web**

### Packet Switching

Packet switching divides data into smaller packets that travel through the network to reach their destination.

### Web Request Journey

A web request moves through several stages:

**Browser → DNS → Gateway → ISP → Server → Browser**

- The browser prepares the request.
- DNS finds the server's IP address.
- The request leaves the local network through the gateway.
- The ISP routes the request toward the destination.
- The server processes the request.
- The browser receives and renders the response.

### DNS

DNS translates human-readable domain names into IP addresses.

The DNS lookup process can include:

**Browser Cache → OS Cache → DNS Resolver → Root Server → TLD Server → Authoritative Server → IP Address**

### Public and Private IP Addresses

A private IP address is used inside a local network.

A public IP address is used to communicate with the Internet and represents the network to the outside world.

Common private IPv4 ranges include:

- `10.x.x.x`
- `172.16.x.x` to `172.31.x.x`
- `192.168.x.x`

### NAT

NAT allows multiple devices with private IP addresses to access the Internet using a public IP address.

### Routing and Hops

Packets travel through multiple routers before reaching their destination.

A hop represents one routing step along the path.

Network routes can change depending on traffic and network conditions.

### Clients and Servers

A client sends a request for data or a service.

A server receives the request, processes it, and sends a response.

**Client → Request → Server → Response → Client**

Examples of clients include:

- Web browsers
- Mobile applications
- Python scripts
- VS Code extensions

### URL Structure

A URL can contain several parts:

```text
https://www.example.com:443/store/products/laptops?brand=apple&sort=price#reviews
```

- **Protocol** – Defines how communication happens
- **Domain** – Identifies the website or server
- **Port** – Identifies the service
- **Path** – Identifies the requested resource
- **Query** – Provides additional parameters
- **Fragment** – Points to a specific section of the page

### Protocols

Common protocols reviewed during the session included:

- **HTTP** – Hypertext Transfer Protocol
- **HTTPS** – Hypertext Transfer Protocol Secure
- **FTP** – File Transfer Protocol
- **SMTP** – Simple Mail Transfer Protocol
- **SSH** – Secure Shell
- **TLS** – Transport Layer Security

### Ports

Ports identify specific services running on a machine.

Examples:

- HTTP → `80`
- HTTPS → `443`
- SSH → `22`
- Django Development Server → `8000`
- Node.js → `3000`
- PostgreSQL → `5432`

An IP address identifies the machine, while a port identifies the service running on that machine.

### Paths, Query Parameters, and Fragments

A path identifies a requested resource.

A query provides additional parameters that can filter or modify a request.

A fragment points to a specific section within a page and is handled by the browser.

### Endpoint Thinking

An endpoint represents a specific location where a client can send a request to access data or perform an operation.

This concept connects networking fundamentals to:

- REST APIs
- Django Routes
- JavaScript `fetch()`
- GraphQL APIs

---

## Practical Activity

Practiced basic networking commands and inspected local network information.

### Network Configuration

```bash
ipconfig
```

Used to view information such as:

- Private IPv4 address
- Subnet mask
- Default gateway

### Connectivity Testing

```bash
ping youtube.com
```

Used to test network reachability and observe round-trip latency.

### Route Tracing

```bash
tracert google.com
```

Used to observe the hops between the local device and the destination.

### Local Web Server

Started a simple local web server using:

```bash
python -m http.server 8000
```

The server was accessed through:

```text
http://localhost:8000
```

In this example:

- `localhost` refers to the current computer.
- `8000` is the port.
- The browser acts as the client.
- The Python process acts as the server.

---

## Key Takeaways

- Understood the difference between the Internet and the Web.
- Learned how packet switching works.
- Reviewed the development from ARPANET to the modern Web.
- Understood the complete web request journey.
- Learned how DNS translates domains into IP addresses.
- Identified public and private IP addresses.
- Understood NAT, routing, hops, and latency.
- Learned how clients and servers communicate.
- Broke down URLs into their main components.
- Reviewed common networking protocols and ports.
- Practiced `ipconfig`, `ping`, and `tracert`.
- Ran a local web server using Python.
- Connected networking concepts to future API and endpoint topics.

---

**Status:** ✅ Completed

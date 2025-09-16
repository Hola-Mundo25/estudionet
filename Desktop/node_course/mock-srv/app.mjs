import path from "node:path";
import { fileURLToPath } from "node:url";
import AutoLoad from "@fastify/autoload";
import cors from "@fastify/cors";
import websocket from "@fastify/websocket";

const __filename = fileURLToPath(import.meta.url);
console.log (__filename)

const __dirname = path.dirname(__filename);
console.log(__dirname)

const options = {};

export default async function (fastify, opts) {
  // Registrar CORS
  fastify.register(cors, {});
  
  // Registrar WebSocket
  fastify.register(websocket, {});

  // Registrar AutoLoad para cargar plugins
  fastify.register(AutoLoad, {
    dir: path.join(__dirname, "plugins"),
    options: opts, // Asegurarse de que opts sea un objeto
  });

  // Registrar AutoLoad para cargar rutas
  let newrr = fastify.register(AutoLoad, {
    dir: path.join(__dirname, "routes"),
    options: opts // Asegurarse de que opts sea un objeto
  });
}

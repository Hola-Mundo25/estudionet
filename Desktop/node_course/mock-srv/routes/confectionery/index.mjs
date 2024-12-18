// routes/confectionery/index.mjs
"use strict";
const data = [
    {
        id: "B1",
        name: "Chocolate Bar",
        rrp: "22.40",
        info: "Delicious overpriced chocolate.",
    },
    ];

    export default async function (fastify, opts) {
    // Obtener todos los productos
    fastify.get("/", async function (request, reply) {
        return data;
    });

    // Insertar un nuevo producto
    fastify.post("/", async function (request, reply) {
        fastify.mockDataInsert(request, opts.prefix.slice(1), data); // Uso de mockDataInsert
        return data;
    });
}

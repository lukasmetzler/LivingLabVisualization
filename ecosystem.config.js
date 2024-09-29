// ecosystem.config.js

module.exports = {
  apps: [
    {
      name: "frontend",
      script: "frontend/.nuxt/dist/server/index.mjs",
      cwd: "/app",
      instances: 1,
      autorestart: true,
      watch: false,
      env: {
        NODE_ENV: "production",
      },
    },
    // Entferne den folgenden Block, wenn kein Backend vorhanden ist:
    /*
    {
      name: "backend",
      cwd: "backend",
      script: "npm",
      args: "run start",
      watch: false,
      env: {
        NODE_ENV: "production",
        JWT_SECRET: process.env.JWT_SECRET || "test",
        DB_HOST: "postgres_new",
        DB_USER: process.env.DB_USER,
        DB_PASSWORD: process.env.DB_PASSWORD,
        DB_NAME: process.env.DB_NAME,
        DB_PORT: "5432",
      },
    },
    */
  ],
};

// ecosystem.config.js

module.exports = {
  apps: [
    {
      name: "frontend",
      script: "dist/index.html", // Für statische Dateien ist keine Node-Ausführung nötig
      // Alternativ, wenn du einen Server verwenden möchtest, passe entsprechend an
      // Beispiel mit einem statischen Server:
      // script: 'server.js',
      // environment variables if needed
      instances: 1,
      autorestart: true,
      watch: false,
      env: {
        NODE_ENV: "production",
      },
    },
    {
      name: "backend",
      cwd: "/app/backend",
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
  ],
};

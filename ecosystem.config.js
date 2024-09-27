module.exports = {
  apps: [
    {
      name: "frontend",
      cwd: "frontend",
      script: "npm",
      args: "run start", // Passe dies an, falls dein Start-Skript anders heißt
      watch: false,
      env: {
        NODE_ENV: "production",
      },
    },
    {
      name: "backend",
      cwd: "backend",
      script: "npm",
      args: "run start", // Passe dies an, falls dein Start-Skript anders heißt
      watch: false,
      env: {
        NODE_ENV: "production",
        JWT_SECRET: process.env.JWT_SECRET || "test",
        DB_HOST: "postgres_new",
        DB_USER: process.env.POSTGRES_USER,
        DB_PASSWORD: process.env.POSTGRES_PASSWORD,
        DB_NAME: process.env.POSTGRES_DB,
        DB_PORT: "5432",
      },
    },
  ],
};

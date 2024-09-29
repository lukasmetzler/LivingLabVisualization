import colors from "vuetify/es5/util/colors";

export default {
  // Global page headers
  server: {
    port: 3001, // Standard: 3000
    host: "0.0.0.0", // Standard: localhost
  },
  head: {
    titleTemplate: "%s - livinglab",
    title: "livinglab",
    htmlAttrs: {
      lang: "en",
    },
    meta: [
      { charset: "utf-8" },
      { name: "viewport", content: "width=device-width, initial-scale=1" },
      { hid: "description", name: "description", content: "" },
      { name: "format-detection", content: "telephone=no" },
    ],
    link: [{ rel: "icon", type: "image/x-icon", href: "/favicon.ico" }],
  },

  // Global CSS
  css: [],

  // Plugins
  plugins: [],

  // Auto import components
  components: true,

  // Modules for dev and build
  buildModules: [
    // Vuetify module
    "@nuxtjs/vuetify",
  ],

  // Modules
  modules: ["@nuxtjs/axios", "@nuxtjs/auth-next"],

  axios: {
    baseURL: "http://localhost:3001", // Anpassen, falls dein API-Server auf einem anderen Port läuft
  },
  auth: {
    strategies: {
      local: {
        token: {
          property: "token",
          global: true,
          // required: true,
          // type: 'Bearer'
        },
        user: {
          property: "user",
          // autoFetch: true
        },
        endpoints: {
          login: { url: "/api/login", method: "post" },
          logout: false,
          user: false,
        },
      },
    },
  },

  serverMiddleware: [{ path: "/api", handler: "~/server/index.js" }],

  // Vuetify-Konfiguration
  vuetify: {
    customVariables: ["~/assets/variables.scss"],
    theme: {
      dark: false, // Setzt das Theme auf hell
      themes: {
        light: {
          primary: colors.blue.darken2,
          accent: colors.grey.darken3,
          secondary: colors.amber.darken3,
          info: colors.teal.lighten1,
          warning: colors.amber.base,
          error: colors.deepOrange.accent4,
          success: colors.green.accent3,
        },
      },
    },
  },

  // Build-Konfiguration
  build: {},
};

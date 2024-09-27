<template>
  <v-app>
    <v-main>
      <v-container
        fluid
        class="d-flex align-center justify-center"
        style="height: 100vh"
      >
        <v-card class="pa-16" max-width="800" outlined>
          <v-card-text>
            <!-- Logo -->
            <div class="d-flex justify-center mb-6">
              <v-img src="/images/logo2.png" max-width="200" contain></v-img>
            </div>

            <!-- Login Form -->
            <v-form @submit.prevent="login" class="d-flex flex-column">
              <v-text-field
                v-model="username"
                label="Benutzername"
                prepend-icon="mdi-account"
                required
                class="mb-12"
              ></v-text-field>
              <v-text-field
                v-model="password"
                label="Passwort"
                type="password"
                prepend-icon="mdi-lock"
                required
                class="mb-12"
              ></v-text-field>
              <v-btn type="submit" color="primary" block class="mt-6">
                Login
              </v-btn>
            </v-form>

            <!-- Forgot Password Link -->
            <div class="text-center mt-6">
              <nuxt-link to="/forgot-password" class="text--primary">
                Passwort vergessen?
              </nuxt-link>
            </div>
          </v-card-text>
        </v-card>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  data() {
    return {
      username: "",
      password: "",
    };
  },
  methods: {
    async login() {
      try {
        await this.$auth.loginWith("local", {
          data: {
            username: this.username,
            password: this.password,
          },
        });
        this.$router.push("/");
      } catch (error) {
        console.error(error);
        this.$toast.error(
          "Login fehlgeschlagen. Bitte überprüfe deine Anmeldedaten."
        ); // Optional: Verwende ein Toast-System für bessere Benachrichtigungen
      }
    },
  },
};
</script>

<style scoped>
.v-card {
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
}

.text--primary {
  color: var(--v-primary-base) !important;
}

a.text--primary:hover {
  text-decoration: underline;
}
</style>

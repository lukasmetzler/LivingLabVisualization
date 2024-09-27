<template>
  <v-app>
    <v-main>
      <v-container
        fluid
        class="d-flex align-center justify-center"
        style="height: 100vh"
      >
        <v-card class="pa-5" max-width="400" outlined>
          <v-card-text>
            <!-- Logo -->
            <div class="text-center mb-4">
              <v-img src="../images/logo.svg" max-width="150" contain></v-img>
            </div>

            <!-- Reset Password Form -->
            <h2 class="text-center mb-4">Passwort zurücksetzen</h2>

            <v-form @submit.prevent="resetPassword" ref="form" v-model="valid">
              <v-text-field
                v-model="email"
                label="E-Mail"
                type="email"
                prepend-icon="mdi-email"
                required
                :rules="emailRules"
              ></v-text-field>
              <v-btn
                type="submit"
                color="primary"
                block
                class="mt-4"
                :loading="loading"
                :disabled="!valid || loading"
              >
                Passwort zurücksetzen
              </v-btn>
            </v-form>

            <!-- Back to Login Link -->
            <div class="text-center mt-3">
              <nuxt-link to="/login" class="text--primary">
                Zurück zum Login
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
      email: "",
      valid: false,
      loading: false,
      emailRules: [
        (v) => !!v || "E-Mail ist erforderlich",
        (v) => /.+@.+\..+/.test(v) || "E-Mail ist ungültig",
      ],
    };
  },
  methods: {
    async resetPassword() {
      // Überprüfen, ob das Formular gültig ist
      if (!this.$refs.form.validate()) {
        this.$toast.error("Bitte gib eine gültige E-Mail-Adresse ein.");
        return;
      }

      this.loading = true;
      try {
        // Implementiere die Logik zum Zurücksetzen des Passworts
        // Beispiel: Sende eine Anfrage an den Backend-API-Endpunkt
        await this.$axios.post("/api/reset-password", { email: this.email });
        this.$toast.success(
          "Ein Link zum Zurücksetzen des Passworts wurde an deine E-Mail gesendet."
        );
        this.$router.push("/login");
      } catch (error) {
        console.error(error);
        this.$toast.error(
          "Fehler beim Zurücksetzen des Passworts. Bitte versuche es erneut."
        );
      } finally {
        this.loading = false;
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
